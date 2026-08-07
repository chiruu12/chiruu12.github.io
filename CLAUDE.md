# chiruu12.github.io

Personal site. Plain HTML + CSS, GitHub Pages deployment.

## File Structure

```
index.html              # Homepage with all sections
style.css               # Global stylesheet (shared via ../style.css from subpages)
achievements.html       # Achievements page
404.html                # Custom 404 (GitHub Pages serves it automatically)
resume.pdf              # Generated PDF (binary, do not edit)
resume.md               # Machine-readable resume for LLMs/agents
blog/index.html         # Blog listing
blog/*.html             # Blog posts
projects/index.html      # Full projects archive (all 10, grouped by status)
projects/*.html         # Project detail pages
genpet.py               # Pixel-cat sprite generator (ASCII grids -> box-shadow CSS)
```

## CSS Classes Reference

**Layout/Nav:**
- `.nav` - top navigation bar (flex, wraps)
- `.site-name` - left-aligned site title link in nav
- `.page-header` - page title area
- `.tagline` - subtitle text under h1

**Content sections (on index.html):**
- `.section-about` - about section (h2 color: accent-blue)
- `.section-projects` - projects section (h2 color: accent-green)
- `.section-status` - current status section (h2 color: accent-orange)
- `.section-blog` - blog previews section (h2 color: accent-red)
- `.section-exp` - experience section (h2 color: accent-blue)

**Components:**
- `.project-card` - bordered card with h3 + p
- `.badge` + `.badge-wip` / `.badge-shipped` / `.badge-pypi` - status badges
- `.blog-post-preview` - left-bordered blog entry (a + .date + p)
- `.date` - timestamp span inside blog previews
- `.status-list` - ul with `> ` prefix items
- `.exp-item` - flex row (role + company + date)
- `.injection-box` - fake terminal prompt joke at top
- `.visitor-counter` - green-on-black counter text

**Projects sections:**
- Homepage `.section-projects` shows only 4 featured cards (Unplug, Hive, Marshal, ArcNet) + `.more-link` to `projects/`.
- `projects/index.html` lists all projects as `.project-card`s grouped under `// on pypi`, `// shipped`, `// work in progress`.

**Easter egg (index.html only):**
- `.pet` - fixed wrapper running one 48s master timeline (`pet-journey`): walk in ->
  sit -> sleep -> wake -> chase the mouse off the right edge. Parked off-screen
  90-100% so the loop restart is invisible.
- `.pet-sprite` `.s-walk` / `.s-sit` / `.s-sleep` / `.s-run` - 26x18 box-shadow pixel
  poses (4px cells, `--pet-color`). Each pose's visibility window (`vis-*`) is
  keyframed to the same 48s timeline.
- `.pet-detail` `.d-walk` / `.d-sit` / `.d-run` - colored overlay layer on top of the
  silhouette: glowing green eyes, pink nose, pink inner ears. `.d-sit` syncs with
  `sit-frames` so the eyes (not the nose) vanish on the blink frame.
- Sub-animations: `walk-frames` (0.5s leg swap + bob), `run-frames` (0.25s gallop),
  `sit-frames` (6s: neutral -> tail flick -> neutral -> blink), `breath` (2.6s scaleY
  on `.s-sleep`), `z-vis`/`z-bob` (floating z's during the sleep window).
- `.pet-mouse` + `.pet-mouse-body` - the mouse. Track element owns the 48s
  `mouse-journey` (transform+opacity); body owns `mouse-frames` (0.18s scurry + red
  eye). Never animate the same property on both - that is the bug class to avoid.
- `.pet-meow` - "mrrp." bubble shown while the cat is clicked (`:active`).
- Hover pauses all animations (that is how you pet it). `prefers-reduced-motion`
  hides both animals.
- The pixel frames are generated, not hand-written. To change any sprite, edit the
  ASCII grids in `genpet.py` (repo root), run `python3 genpet.py`, and splice the
  emitted box-shadow blocks back into `style.css`. Keep it in `style.css`; no JS allowed.

## HTML Templates

### New blog post (`blog/new-post.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>POST TITLE - Chirag Gupta</title>
  <meta name="description" content="SHORT DESCRIPTION">
  <link rel="stylesheet" href="../style.css">
</head>
<body>

<nav class="nav">
  <a href="../" class="site-name">chirag.gupta</a>
  <a href="../">[home]</a>
  <a href="./">[blog]</a>
  <a href="../achievements.html">[achievements]</a>
  <a href="../resume.pdf">[resume]</a>
</nav>

<header class="page-header">
  <h1>POST TITLE</h1>
  <p class="tagline">MONTH YEAR</p>
</header>

<hr>

<p>Content here.</p>

<footer>
  <p><a href="../">[back to home]</a></p>
</footer>

</body>
</html>
```

### New project page (`projects/new-project.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PROJECT NAME - Chirag Gupta</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>

<nav class="nav">
  <a href="../" class="site-name">chirag.gupta</a>
  <a href="../">[home]</a>
  <a href="../blog/">[blog]</a>
  <a href="../achievements.html">[achievements]</a>
  <a href="../resume.pdf">[resume]</a>
</nav>

<header class="page-header">
  <h1>PROJECT NAME <span class="badge badge-wip">[WIP]</span></h1>
  <p class="tagline">One-line description</p>
  <p><a href="https://github.com/chiruu12/REPO">[github]</a></p>
</header>

<hr>

<h2>// what it does</h2>
<p>Description.</p>

<h2>// how it works</h2>
<p>Architecture.</p>

</body>
</html>
```

### Project card (add to `index.html` inside `.section-projects`)

```html
<div class="project-card">
  <h3><a href="projects/SLUG.html">NAME</a> <span class="badge badge-wip">[WIP]</span></h3>
  <p>One-line description.</p>
</div>
```

### Blog preview (add to `index.html` inside `.section-blog`)

```html
<div class="blog-post-preview">
  <a href="blog/SLUG.html">post title</a><span class="date">Month Year</span>
  <p>One-line teaser.</p>
</div>
```

## Navigation (subpages)

From `blog/*.html`: use `../` for root, `./` for blog index, `../projects/` for projects.
From `projects/*.html`: use `../` for root, `../blog/` for blog.

Blog posts link to `[blog]` as `"./"`. Project pages link to `[blog]` as `"../blog/"`.

## Tone and Voice

- First person, direct, casual.
- No AI slop. No em dashes. No emoji. No "leverage" or "cutting-edge" or "passionate about."
- Short sentences. Dry humor is fine. Match existing post voice.
- Section headers use `// name` format (lowercase).

## Deploy

```bash
git add .
git commit -m "description of what changed"
git push origin main
```

GitHub Pages serves from main branch root. Changes go live in ~1 minute.

## Resume Rebuild

The resume sources are tracked in this repo: `resume.html` (public) and `resume-anon.html`
(redacted twin for anonymous review). Keep `resume.md` in sync as the machine-readable copy.
Page size is set via `@page { size: A4 }` in each file's CSS. To regenerate the PDFs:

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=resume.pdf "file://$PWD/resume.html"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=resume-anon.pdf "file://$PWD/resume-anon.html"
```

Verify content + redactions with `pdftotext -layout resume-anon.pdf -` (it must not contain
real names, employers, school, or project names).

## Rules

- Do not add JavaScript, build tools, or frameworks.
- Do not change the 90s retro aesthetic.
- Do not use Tailwind, React, or any CSS framework.
- All styling goes in `style.css`. No inline styles except minor one-offs already present.
- Keep pages lightweight. No images unless essential.
- Every page must link back to home via the nav.
