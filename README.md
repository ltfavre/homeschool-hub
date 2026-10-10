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
