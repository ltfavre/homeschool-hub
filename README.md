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

## Deploy to Cloudflare (Pages)

This app deploys as a **Cloudflare Pages** project. `public/` is the build output directory; `public/_worker.js` is the Pages "advanced mode" worker that serves the `/api/*` D1 endpoints and passes everything else to the static assets. There is intentionally no root `wrangler.jsonc` (a Workers config is invalid for Pages and breaks `npx wrangler deploy`); bindings are managed in the dashboard. `wrangler.dev.jsonc` is used only for local development.

1. Create the D1 database: `npx wrangler d1 create homeschool-hub-db`.
2. Initialize the schema: paste `schema.sql` into the D1 database Console in the dashboard (or run `npx wrangler d1 execute homeschool-hub-db --remote --file=./schema.sql` with a config containing the `database_id`). Subjects are seeded by `schema.sql`.
3. In Workers & Pages, create/connect the Pages project to this GitHub repo with **build command empty** and **build output directory `public`**. Do not use `npx wrangler deploy` as the command.
4. In the Pages project: Settings > Bindings > add a D1 database binding named `DB` pointing to `homeschool-hub-db` (for Production and Preview), then redeploy. Without this, `/api/*` returns errors.
5. Protect the site with **Cloudflare Access** (Zero Trust > Access > Applications), covering the whole site including the `/api/*` write endpoints. There is no authentication yet, so anyone with the URL could otherwise write data.

Local: `npm install && npm run db:init:local && npm run dev`.

## Current API

- `GET /api/health`
- `GET /api/bootstrap`
- `GET /api/lessons?start=YYYY-MM-DD&end=YYYY-MM-DD`
- `POST /api/lessons`
- `GET /api/assignments?start=YYYY-MM-DD&end=YYYY-MM-DD`
- `POST /api/assignments`
- `DELETE /api/lessons/:id`
- `DELETE /api/assignments/:id`

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
