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
  external_id TEXT,
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
  external_id TEXT,
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
CREATE UNIQUE INDEX IF NOT EXISTS idx_lessons_external_id ON lessons(external_id) WHERE external_id IS NOT NULL;
CREATE UNIQUE INDEX IF NOT EXISTS idx_assignments_external_id ON assignments(external_id) WHERE external_id IS NOT NULL;

CREATE TABLE IF NOT EXISTS family_daily_tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  source TEXT NOT NULL,
  external_id TEXT NOT NULL,
  user_id TEXT NOT NULL,
  title TEXT NOT NULL,
  due_date TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'pending',
  payload_json TEXT,
  last_synced_at INTEGER NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_family_daily_tasks_source_external_user
  ON family_daily_tasks(source, external_id, user_id);
CREATE INDEX IF NOT EXISTS idx_family_daily_tasks_user_due ON family_daily_tasks(user_id, due_date);

CREATE TABLE IF NOT EXISTS family_sync_log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  source TEXT NOT NULL,
  started_at INTEGER NOT NULL,
  finished_at INTEGER,
  ok INTEGER NOT NULL DEFAULT 0,
  summary_json TEXT,
  error_message TEXT
);

CREATE TABLE IF NOT EXISTS family_users (
  id TEXT PRIMARY KEY,
  username TEXT NOT NULL UNIQUE,
  display_name TEXT NOT NULL,
  role TEXT NOT NULL,
  grade TEXT,
  password_hash TEXT,
  password_salt TEXT,
  active INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS family_sessions (
  token_hash TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  expires_at INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_family_sessions_user_id ON family_sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_family_sessions_expires_at ON family_sessions(expires_at);

CREATE TABLE IF NOT EXISTS family_invites (
  token_hash TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  expires_at INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_family_invites_user_id ON family_invites(user_id);

CREATE TABLE IF NOT EXISTS family_login_limits (
  bucket TEXT PRIMARY KEY,
  attempts INTEGER NOT NULL DEFAULT 0,
  expires_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS family_curriculum_completion (
  user_id TEXT NOT NULL,
  school_date TEXT NOT NULL,
  subject TEXT NOT NULL,
  completed INTEGER NOT NULL DEFAULT 0,
  updated_at INTEGER NOT NULL,
  curriculum TEXT NOT NULL DEFAULT 'khan-primary-v1',
  PRIMARY KEY (user_id, school_date, subject, curriculum)
);
CREATE INDEX IF NOT EXISTS idx_family_curriculum_completion_date ON family_curriculum_completion(school_date);

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
