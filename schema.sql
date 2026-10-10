PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  grade TEXT NOT NULL,
  active INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS subjects (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS lessons (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  student_id INTEGER NOT NULL,
  subject_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  lesson_date TEXT NOT NULL,
  segment INTEGER,
  week INTEGER,
  objective TEXT,
  instructions TEXT,
  resource_url TEXT,
  source_name TEXT,
  estimated_minutes INTEGER,
  status TEXT NOT NULL DEFAULT 'planned',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

CREATE TABLE IF NOT EXISTS assignments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  lesson_id INTEGER,
  student_id INTEGER NOT NULL,
  subject_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  due_date TEXT NOT NULL,
  instructions TEXT,
  resource_url TEXT,
  points_possible REAL,
  points_earned REAL,
  status TEXT NOT NULL DEFAULT 'assigned',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (lesson_id) REFERENCES lessons(id),
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

CREATE INDEX IF NOT EXISTS idx_lessons_date ON lessons(lesson_date);
CREATE INDEX IF NOT EXISTS idx_assignments_due ON assignments(due_date);

INSERT OR IGNORE INTO subjects(name) VALUES
('Math'),('Language Arts'),('Grammar'),('Spelling'),('Reading'),
('Science'),('Social Studies'),('Writing'),('Art'),('Technology');

-- Replace these placeholder student names after deployment.
INSERT INTO students(name, grade)
SELECT '4th Grader', '4'
WHERE NOT EXISTS (SELECT 1 FROM students WHERE grade='4');

INSERT INTO students(name, grade)
SELECT '7th Grader', '7'
WHERE NOT EXISTS (SELECT 1 FROM students WHERE grade='7');
