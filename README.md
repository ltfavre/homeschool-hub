# Homeschool Hub

A lightweight family homeschool dashboard designed for Cloudflare Workers + Static Assets + D1.

## What is already included

- Two student placeholders (4th grade and 7th grade)
- Subjects
- Lessons
- Assignments
- Today's dashboard
- 7-day calendar
- Resource links
- Cloudflare D1 schema
- REST endpoints that can later support bulk imports from lesson-plan spreadsheets/CSVs
- Family agenda APIs used by the Home Assistant dashboard
- VenvLearning daily-task sync (API or adapter endpoint)

## Local setup

1. Install Node.js.
2. Run:

```bash
npm install
npm run db:init:local
npm run dev
```

Wrangler will print the local URL.

## Deploy to Cloudflare

This starter uses the current Cloudflare Workers Static Assets approach rather than an older Workers Sites setup.

1. Create a GitHub repository (suggested name: `homeschool-hub`).
2. Push this project to the repo.
3. In Cloudflare, create/import a Worker project from that GitHub repository.
4. Cloudflare can provision the D1 binding from `wrangler.jsonc`.
5. After the first deployment, initialize the production database:

```bash
npm install
npm run db:init:remote
```

If Cloudflare writes a D1 resource ID into the dashboard instead of the repository, keep the dashboard binding named `DB`.

## Current API

- `GET /api/health`
- `GET /api/bootstrap`
- `GET /api/lessons?start=YYYY-MM-DD&end=YYYY-MM-DD`
- `POST /api/lessons`
- `GET /api/assignments?start=YYYY-MM-DD&end=YYYY-MM-DD`
- `POST /api/assignments`
- `GET /api/family/agenda?date=YYYY-MM-DD[&student=<student-id>]`
- `POST /api/family/venvlearning/sync`

## VenvLearning daily tasks integration

The family agenda (`/agenda` and `/api/family/agenda`) now includes `daily_tasks` sourced from VenvLearning and normalized to:

- `title`
- `user_id` (assignee child)
- `due_date`
- `status`
- `source`
- `external_id`

### Configuration (secrets/env)

Use Cloudflare Worker secrets (or `.dev.vars` for local development):

- `VENVLEARNING_API_BASE_URL` (example: `https://venvlearning.com/api`)
- `VENVLEARNING_API_TOKEN`
- Optional `VENVLEARNING_ADAPTER_URL` (if a direct API is unavailable; should return JSON tasks)
- Optional `VENVLEARNING_STUDENT_MAP` (JSON map from VenvLearning assignee string to local student id)
- Optional `VENVLEARNING_SYNC_TOKEN` (allows non-session sync calls, for Home Assistant automations)

### Sync behavior

- Sync endpoint: `POST /api/family/venvlearning/sync`
- Body (optional): `{ "start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD" }`
- Auth: parent session cookie **or** `Authorization: Bearer <VENVLEARNING_SYNC_TOKEN>` (or `x-venvlearning-sync-token` header)
- Idempotency: upsert by `(source, external_id, user_id)` so repeated syncs do not duplicate tasks
- Observability: worker logs include sync summary/failures and the DB table `family_sync_log` records outcomes

### Home Assistant wiring

1. Keep the family dashboard card pointed at the same Homeschool Hub agenda surface (`/agenda`).
2. Add an HA automation that calls `POST /api/family/venvlearning/sync` on a schedule (for example every 30–60 minutes during school hours).
3. Use `VENVLEARNING_SYNC_TOKEN` in the HA REST call header.
4. Reload the dashboard card; daily tasks appear in the “VenvLearning daily tasks” section in agenda.
5. If you open the hub inside an HA iframe/card, enable cross-site session behavior:
   - `FAMILY_EMBED_IN_HA=1` (defaults cookie SameSite to `None`)
   - Optional explicit override: `FAMILY_SESSION_SAMESITE=None`
   - Optional frame policy override: `FAMILY_ALLOWED_FRAME_ANCESTORS='self' http://homeassistant.local:8123 https://homeassistant.local:8123`
   - Optional partitioned cookie support for modern third-party cookie restrictions: `FAMILY_SESSION_PARTITIONED=1`
   - For local non-HTTPS testing only, you can disable secure-cookie mode: `FAMILY_SESSION_SECURE=0` and set `FAMILY_SESSION_COOKIE_NAME=venv_session`

If VenvLearning authentication or API shape is not available, configure `VENVLEARNING_ADAPTER_URL` to a trusted internal adapter that returns JSON tasks and preserves a stable task id.

## Planned next steps

1. Authentication / parent-only editing.
2. Bulk CSV lesson import.
3. Education.com resource catalog/import workflow.
4. Google Calendar sync/export.
5. Completion checkboxes and grades.
6. Segment/week filters for the 9 x 4-week homeschool structure.
7. Attachments via Google Drive.
8. Student dashboards and gifted-extension tags.
9. Attendance and report-card views.

## Security note

Do not store passwords, API keys, or private credentials in the repository. Use Cloudflare secrets/environment bindings for secrets.
