"""Exercise date selection and actual todo writes without a Home Assistant install."""
import asyncio
import copy
import importlib.util
import sys
import types
import unittest
from dataclasses import dataclass
from datetime import date
from enum import StrEnum, IntFlag
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'custom_components/venvlearning'
def module(name, **values):
    m = types.ModuleType(name)
    m.__dict__.update(values)
    sys.modules[name] = m
    return m
class HAError(Exception): pass
class ClientError(Exception): pass
class BaseCoordinator:
    def __init__(self, hass, *args, **kwargs): self.hass, self.data = hass, None
    def async_set_updated_data(self, data): self.data = data
    async def async_request_refresh(self): self.data = await self._async_update_data()
class CoordinatorEntity:
    def __init__(self, coordinator): self.coordinator = coordinator
class Status(StrEnum):
    COMPLETED = 'completed'
    NEEDS_ACTION = 'needs_action'
class Feature(IntFlag): UPDATE_TODO_ITEM = 1
@dataclass
class Item:
    uid: str = None
    summary: str = None
    status: Status = None
    due: date = None
    description: str = None
module('aiohttp', ClientError=ClientError)
module('homeassistant')
module('homeassistant.components')
module('homeassistant.components.todo', TodoItem=Item, TodoItemStatus=Status, TodoListEntity=type('TodoListEntity', (), {}), TodoListEntityFeature=Feature)
module('homeassistant.helpers')
module('homeassistant.helpers.update_coordinator', DataUpdateCoordinator=BaseCoordinator, CoordinatorEntity=CoordinatorEntity, UpdateFailed=HAError)
module('homeassistant.exceptions', ConfigEntryAuthFailed=HAError, HomeAssistantError=HAError)
module('school', __path__=[str(ROOT)])
module('school.api', InvalidAuth=type('InvalidAuth', (Exception,), {}))
def load(name):
    spec=importlib.util.spec_from_file_location('school.'+name, ROOT/(name+'.py'))
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m
Coordinator=load('coordinator').VenvCoordinator
todo_mod=load('todo')
Todo=todo_mod.StudentTodo
Assignments=todo_mod.StudentAssignments

class Client:
    def __init__(self): self.today='2026-10-17'; self.completed={}; self.turned_in={}; self.calls=[]; self.fail=False
    async def agenda(self, start=None, end=None):
        if self.fail: raise ClientError()
        self.calls.append((start,end))
        first, last = (start.isoformat(),end.isoformat()) if start else ('2026-10-10','2026-11-21')
        days=['2026-10-16','2026-10-19','2027-02-01']
        students=[]
        for student in ('ellie','lillie'):
            items=[dict(uid=f'{student}|{d}|math',student_id=student,date=d,subject='math',summary='Math',description='Lesson',completed=self.completed.get((student,d),False)) for d in days if first<=d<=last]
            assignments=[dict(uid=f'assignment|5|{student}',assignment_id=5,student_id=student,date='2026-10-19',subject='math',summary='Fractions',description='Do 1-10',completed=self.turned_in.get(student,False),locked=student=='lillie',status='graded' if student=='lillie' else 'assigned',score=9 if student=='lillie' else None,possible=10)]
            students.append({'id':student,'display_name':student,'grade':'4','items':items,'assignments':assignments})
        return {'today':self.today,'start':first,'end':last,'students':students}
    async def complete(self,item,completed): self.completed[item['student_id'],item['date']]=completed
    async def complete_assignment(self,item,completed): self.turned_in[item['student_id']]=completed

class DateTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.entry=types.SimpleNamespace(entry_id='entry',options={})
        def update(entry,options): entry.options=options
        self.hass=types.SimpleNamespace(config_entries=types.SimpleNamespace(async_update_entry=update))
        self.client=Client();self.c=Coordinator(self.hass,self.entry,self.client)
        self.c.data=await self.c._async_update_data()
        self.todos=[Todo(self.c,self.entry,s) for s in self.c.data['students']]

    async def test_same_date_for_both_students_and_correct_write(self):
        await self.c.async_select_date(date(2026,10,16))
        for todo in self.todos:
            self.assertEqual(todo.todo_items[0].due,date(2026,10,16))
        await self.todos[0].async_update_todo_item(Item(uid='ellie|2026-10-16|math',status=Status.COMPLETED))
        self.assertTrue(self.client.completed['ellie','2026-10-16'])
        self.assertNotIn(('ellie','2026-10-19'),self.client.completed)
        self.assertEqual(self.todos[0].todo_items[0].status,Status.COMPLETED)
        self.assertEqual(self.todos[1].todo_items[0].status,Status.NEEDS_ACTION)
        await self.todos[0].async_update_todo_item(Item(uid='ellie|2026-10-16|math',status=Status.NEEDS_ACTION))
        self.assertFalse(self.client.completed['ellie','2026-10-16'])

    async def test_future_outside_cache_keeps_calendar_window(self):
        await self.c.async_select_date(date(2027,2,1))
        self.assertEqual(self.todos[0].todo_items[0].due,date(2027,2,1))
        self.assertTrue(any(t['date']=='2026-10-19' for t in self.c.student('ellie')['items']))
        self.assertEqual(self.client.calls[-1],(date(2027,2,1),date(2027,2,1)))

    async def test_weekend_and_today_rollover(self):
        self.assertEqual(self.todos[0].todo_items,[])
        await self.c.async_select_date(date(2026,10,16))
        await self.c.async_select_date(None)
        self.assertNotIn('school_date',self.entry.options)
        self.client.today='2026-10-19'
        await self.c.async_request_refresh()
        self.assertEqual(self.todos[0].todo_items[0].due,date(2026,10,19))

    async def test_selection_restores_and_failure_keeps_previous_day(self):
        await self.c.async_select_date(date(2026,10,16))
        restored=Coordinator(self.hass,self.entry,self.client)
        restored.data=await restored._async_update_data()
        self.assertEqual(restored.selected_date,date(2026,10,16))
        self.client.fail=True
        with self.assertRaises(HAError): await self.c.async_select_date(date(2027,2,1))
        self.assertEqual(self.c.selected_date,date(2026,10,16))
        self.assertEqual(self.entry.options['school_date'],'2026-10-16')

class AssignmentTests(DateTests):
    async def test_check_off_turns_in_and_graded_is_locked(self):
        ellie,lillie=[Assignments(self.c,self.entry,s) for s in self.c.data['students']]
        self.assertEqual(ellie.todo_items[0].summary,'Math: Fractions')
        await ellie.async_update_todo_item(Item(uid='assignment|5|ellie',status=Status.COMPLETED))
        self.assertTrue(self.client.turned_in['ellie'])
        self.assertEqual(ellie.todo_items[0].status,Status.COMPLETED)
        self.assertEqual(lillie.todo_items[0].summary,'Math: Fractions (9/10)')
        with self.assertRaises(HAError): await lillie.async_update_todo_item(Item(uid='assignment|5|lillie',status=Status.NEEDS_ACTION))

if __name__=='__main__': unittest.main()

