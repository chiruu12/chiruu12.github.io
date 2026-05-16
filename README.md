# chiruu12.github.io

Personal site. Live at [chiruu12.github.io](https://chiruu12.github.io).

Plain HTML + CSS, no frameworks, no build step. 90s retro aesthetic with VT323 and Space Mono fonts.

## Structure

```
.
├── index.html           # Homepage (about, projects, status, blog previews)
├── style.css            # Single stylesheet, shared by all pages
├── achievements.html    # Achievements page
├── resume.pdf           # PDF resume
├── resume.md            # Machine-readable resume (for LLMs)
├── blog/
│   ├── index.html       # Blog listing page
│   └── *.html           # Individual posts
└── projects/
    └── *.html           # Individual project pages
```

## Adding a blog post

1. Create `blog/your-slug.html` (copy an existing post as template)
2. Add a preview entry to `blog/index.html`
3. Add a preview entry to the `section-blog` in `index.html`

## Adding a project page

1. Create `projects/your-project.html` (copy an existing project page as template)
2. Add a `project-card` div to `section-projects` in `index.html`

## Updating the resume

1. Edit `tmp/resume.html` (the source file, not tracked here)
2. Generate PDF: `npx puppeteer-cli print tmp/resume.html resume.pdf --format A4`
3. Copy the PDF into this repo root

## Deploy

Push to `main`. GitHub Pages serves it automatically.

## Design notes

- Monospace everything. VT323 for headings, Space Mono for body.
- Parchment background (`#f0ece4`), no pure white or black backgrounds.
- Dashed `<hr>` separators, bordered project cards, left-bordered blog previews.
- No JavaScript. No build tools. No dependencies beyond Google Fonts.
- Prompt injection joke in the header is intentional.
