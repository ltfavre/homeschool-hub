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

Project layout: the Worker lives in `src/index.js` and static assets live in `public/` (only that folder is served). `schema.sql` and config stay at the repo root.

### Checklist

1. Push this project to a GitHub repository.
2. Create the D1 database:

```bash
npx wrangler d1 create homeschool-hub-db
```

3. `wrangler.jsonc` intentionally omits `database_id` so Cloudflare can auto-provision the `DB` binding. If it is not auto-provisioned (or deploy complains), add the `database_id` printed above to the `d1_databases` entry:

```jsonc
{ "binding": "DB", "database_name": "homeschool-hub-db", "database_id": "<your-id>" }
```

4. Initialize the production schema:

```bash
npm install
npm run db:init:remote
```

5. In the Cloudflare dashboard go to **Workers & Pages > Create > Import repository**, pick the repo, leave the build command empty, and set the deploy command to `npx wrangler deploy`.
6. Verify locally with `npx wrangler deploy --dry-run`.
7. **Protect the site with Cloudflare Access** (Zero Trust > Access > Applications), covering the whole site including the `POST /api/*` endpoints. There is no authentication yet, so anyone with the URL could otherwise write data.

**Use a Workers project, not Pages.** This app is a Worker (`main` + `assets` in `wrangler.jsonc`). A Cloudflare *Pages* project (shown as the "Cloudflare Pages" check on GitHub) rejects this config and fails immediately. Delete that Pages project and import the repo via Workers & Pages > Create > Workers > Import a repository.

If the dashboard creates the D1 binding instead, keep it named `DB`.

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
