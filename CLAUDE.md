# The Fix Wizard — Project Guidelines for Claude

## Business

- **Name:** The Fix Wizard
- **Phone:** (551) 350-4951
- **Email:** thefixwizard@gmail.com
- **Website:** https://thefixwizard.com
- **Hours:** Mon–Sat 7am–7pm
- **Trust signals (always include):** Licensed & insured · Same-day available · Free estimates

## Service Area

Primary: Cherry Hill, NJ (Camden County)
Also serves:
- Haddonfield, NJ · Voorhees, NJ · Marlton, NJ (Camden County)
- Moorestown, NJ · Mount Laurel, NJ (Burlington County)
- Philadelphia, PA · Wayne, PA · West Chester, PA · King of Prussia, PA
- Wilmington, DE
- Trenton, NJ · Princeton, NJ · Atlantic City, NJ

Do NOT reference any cities outside this list. The business is South Jersey / Greater
Philadelphia radius — never mention North Jersey cities (Newark, Hoboken, Jersey City, etc.)

## Services

Two categories live in `services-data.json`:

**Chimney & Masonry (18 services):** inspections, sweeps, tuckpointing, crown repair/rebuild,
cap installation, flashing repair, liner installation, waterproofing, damper installation,
creosote cleaning, animal removal, firebox repair/rebuild, chase cover replacement, leak repair,
chimney waterproofing.

**Handyman (27 services):** ceiling fan installation, drywall patching, faucet replacement,
bathroom exhaust fan, attic ladder replacement, baseboard molding, blinds/curtain rods,
cabinet repair/hardware, fascia repair, fence repair, floating shelves, and more.

## Brand & Design

### Colors
| Token        | Hex     | Usage                         |
|--------------|---------|-------------------------------|
| navy-950     | #091236 | Hero backgrounds, footer, CTA |
| navy-900     | #0d1b4b | Navbar, mobile menu, accents  |
| navy-800     | #152468 | Dark cards                    |
| navy-700     | #1e3480 | Hover states                  |
| orange       | #FF6B35 | Primary accent, CTAs, icons   |
| orange-light | #FF8C42 | Hover orange                  |
| orange-dark  | #e55a22 | Active/pressed orange         |
| Body text    | #3a4560 | Main paragraph text           |
| Background   | #ffffff | Page base                     |

### Fonts
- **Cinzel** (serif, weights 600 & 900) — headings, H1s, brand moments
- **Inter** (sans-serif, weights 300–900) — body, UI, labels, captions

### Tone of Voice
Fun and professional. Confident but not stuffy. Speak directly to homeowners — explain
the real-world consequence of a problem, not just what the service is. Use short sentences.
Avoid jargon. It's OK to be slightly conversational ("Your damper is bleeding heat out the
chimney right now") while staying trustworthy.

## Site Structure

```
build.js                  — master build script, run with: node build.js
services-data.json        — SOURCE OF TRUTH for all service content + SEO copy
generate-locations.js     — builds city hub pages → docs/[city]-repair/
generate-service-pages.js — builds service hubs + detail pages → docs/
partials/                 — homepage HTML sections (assembled by build.js)
docs/                     — ALL generated output (do not edit directly)
```

### URL Patterns
- City hub:         `/cherry-hill-repair/`
- Service category: `/handyman-services-near-cherry-hill/`
- Service detail:   `/ceiling-fan-installation-near-cherry-hill/`

### Critical Rule
**Never edit files inside `docs/` directly.** Every `node build.js` wipes and regenerates
that entire folder. All content and copy changes go in `services-data.json`. All
structural/layout changes go in `generate-service-pages.js` or `generate-locations.js`.
After any change: `node build.js` → then commit `docs/` to git.

## SEO Strategy

### Keyword Formula
The site targets: `[service] near [city]` and `[service] near [city, state]`

Examples:
- "ceiling fan installation near Cherry Hill"
- "chimney repair near Moorestown NJ"
- "handyman services near Voorhees"
- "drywall repair near Philadelphia"

Every H1 must contain the service name + "near [City, State]".
Every H2 should naturally embed a related keyword or local reference.
Meta descriptions: 145–155 chars, include service + location + CTA.

### SEO Page Structure (each service detail page)
Every detail page follows this content order:

1. **Hero** — H1: `[Service] Near [City, State]`, hero subtitle from `svc.desc`,
   "What's Included" checklist in the sidebar card
2. **Why You Need It** (`h2_why_need` / `why_need`) — address the search intent:
   what problem brings someone to Google? Local climate, age of homes, common triggers.
3. **How We Do It** (`h2_benefits` / `benefits`) — what the installation/repair
   process looks like, what makes professional service better than DIY.
4. **Pricing & Longevity** (`h2_longevity` / `longevity`) — cost range in the local
   market, how long the fix lasts, what maintenance is needed.
5. **What Happens If You Wait** (`h2_consequences` / `consequences`) — real
   consequences of ignoring the problem. Safety risks, cost escalation, home damage.
   Name specific nearby cities where relevant for local SEO signals.
6. **CTA Banner** — phone number + "Free Quote" button
7. **Footer**

### Content Quality Rules
- Minimum ~250 words of unique body copy per service detail page
- Mention at least 2–3 nearby city names naturally within the copy
- Include a price range in the longevity section (helps "cost" search queries)
- Every page must have trust signals: licensed, insured, same-day, free estimate
- H2s are SEO-optimized headings — make them compelling and keyword-adjacent,
  not generic ("Why You Need It" → "South Jersey Summers Are Brutal — Cut AC Bills")

### Content Override System (services-data.json)
Each service slug in `content{}` can override any section:
```json
"ceiling-fan-installation": {
  "meta_desc":       "...",   // full meta description (use {cityState} placeholder)
  "h2_why_need":     "...",   // H2 heading for section 1
  "why_need":        "...",   // body text for section 1
  "h2_benefits":     "...",   // H2 heading for section 2
  "benefits":        "...",   // body text for section 2
  "h2_longevity":    "...",   // H2 heading for section 3
  "longevity":       "...",   // body text for section 3
  "h2_consequences": "...",   // H2 heading for section 4
  "consequences":    "..."    // body text for section 4
}
```
Without overrides the generator uses generic fallbacks. Always add overrides for
any service page that matters for SEO.

## Git & Deploy

- Output folder: `docs/` (GitHub Pages source)
- Custom domain: `thefixwizard.com` (CNAME in `docs/CNAME`)
- Push to `main` → GitHub Pages auto-deploys within ~2 minutes
- Commit message format: `SEO: [description]` or `Fix: [description]`
