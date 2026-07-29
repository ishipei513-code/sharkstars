---
name: new-demo
description: Scaffold a new SHARKSTARS demo site (demos/<slug>-01/) by cloning an existing demo as template and adapting it to a new industry. Use when adding a 57th+ industry showcase. Invocation form -- /new-demo <new-slug> <industry-jp> [from=<template-slug>]
disable-model-invocation: true
---

# /new-demo — scaffold a new industry demo

Use this skill to add a new demo under `demos/<slug>-01/`. SHARKSTARS already has 56 demos that all share the same skeleton; this skill clones one of them and adapts the surface text + SEO so the new demo is shippable.

## Arguments

The user invokes the skill in one of these forms:

```
/new-demo chiropractic-01 整体院
/new-demo chiropractic-01 整体院 from=seitai-01
```

Parse:
- **new-slug** (required, kebab-case, must end with `-01`): destination directory under `demos/`.
- **industry-jp** (required): the Japanese industry label, used in copy and SEO meta.
- **from=<template-slug>** (optional, default = closest-matching existing demo, falling back to `cafe-01` which has the most up-to-date scaffolding): source demo to clone.

If arguments are missing, ask the user for them in one round-trip — don't proceed with placeholders.

## Workflow

### Step 1 — Validate

- Reject if `demos/<new-slug>/` already exists. (Do not overwrite.)
- Reject if `<new-slug>` does not match `^[a-z][a-z0-9-]*-01$`.
- Reject if `from=` template does not exist.

### Step 2 — Clone

Copy `demos/<from>/` to `demos/<new-slug>/` recursively. Preserve directory structure (`assist/css/`, `assist/images/`, etc.).

```bash
cp -r demos/<from> demos/<new-slug>
```

### Step 3 — Rewrite SEO surface

In `demos/<new-slug>/index.html`, rewrite the head SEO so it matches the new demo:

- `<title>`: replace template's industry name with `<industry-jp>` brand
- `<meta name="description">`: rewrite to a 1-2 sentence pitch for `<industry-jp>`
- `<link rel="canonical">`: change to `https://sharkstars.jp/demos/<new-slug>/`
- All `og:url`, `twitter:url` to the new canonical
- `og:site_name`: leave as the demo's brand name (you'll choose one in step 4)
- `og:image` URL: point at the new demo's hero image (placeholder OK if unsure)
- JSON-LD `@type` and brand name: pick the most appropriate schema.org type for `<industry-jp>` (e.g., `MedicalBusiness` for clinics, `LocalBusiness` for general, `Restaurant` for food, `BeautySalon` for salons)

### Step 4 — Rewrite visible copy

The demo's body copy is industry-specific. After cloning, the user (and Codex) must replace:
- Hero headline / subhead
- Concept / about section
- Service / menu items
- FAQ items
- Footer brand name

Don't try to invent realistic copy automatically — leave clearly-marked placeholders like `[TODO: <industry-jp>用のキャッチコピー]` so the user knows what to fill in before publishing.

### Step 5 — Owner / contact info

The `<address>` / footer must list **石橋昇平** as the SHARKSTARS representative if any owner field is present. Do not invent a different name or contact. (The PreToolUse `check_owner_name.py` hook will block you if you do.)

### Step 6 — Add to demo index (optional, ask first)

If the main `index.html` has a demo gallery section, ask the user whether to add a thumbnail entry for the new demo. Don't auto-edit the gallery without consent — the gallery has its own ordering convention.

### Step 7 — Verify

Hand off to the `demo-site-reviewer` subagent on the new demo to produce a punch list:

```
Use the demo-site-reviewer agent on demos/<new-slug>/
```

Report the agent's findings to the user before declaring done.

## Output

When complete, report:
- Path created: `demos/<new-slug>/`
- SEO fields rewritten (count)
- Placeholders left for the user to fill (list)
- demo-site-reviewer verdict (PASS / NEEDS FIXES with summary)

## Boundaries

- Do not run the demo through a build step; demos are static HTML.
- Do not commit. The user reviews before committing.
- Do not modify other demos or the main site as a side effect.
