# SEO Agent — The Fix Wizard

This file is the knowledge base for the SEO agent at:
https://claude.ai/code/routines/trig_013DDJTa67jdrM8gzU3EsxZf

When you want to run the agent, go to that URL, paste your task into the
`# YOUR TASK` section at the bottom of the prompt, and hit Run.

---

## About the Business

- **Name:** The Fix Wizard
- **Category:** Home repair / handyman contractor
- **Location:** Serves ALL of New Jersey (all 21 counties)
- **Services:** Garage Door Repair, Drywall Repair, Furniture Assembly, Painting, Door Repair & Replacement, Chimney & Masonry, Light Electrical, Light Plumbing
- **Phone:** (555) 123-4567 | **Email:** hello@handypro.com
- **Hours:** Mon–Sat 7am–7pm
- **Key selling points:** Licensed & insured, same-day available, free estimates, transparent pricing

---

## Site Structure

```
index.html                              — homepage (rebuild: node build.js)
partials/                               — homepage HTML sections
[service]-new-jersey/index.html         — 8 service landing pages
[service]-new-jersey/[slug]/index.html  — 24 SEO blog posts
css/tw.css                              — compiled Tailwind (rebuild: ./node_modules/.bin/tailwind -i css/input.css -o css/tw.css --minify)
css/custom.css                          — animations only
```

CSS paths:
- Service pages → `../css/tw.css` + `../css/custom.css`
- Blog posts → `../../css/tw.css` + `../../css/custom.css`

---

## SEO Rules

### 1. Title Tags
- **50–60 characters** (Google truncates beyond 60)
- Format: `Primary Keyword in New Jersey | The Fix Wizard`
- Lead with the keyword, not the brand name
- Every page must have a **unique** title
- ✅ Good: `Drywall Repair in New Jersey — Patches & Water Damage | The Fix Wizard`
- ❌ Bad: `The Fix Wizard | Home Repair`

### 2. Meta Descriptions
- **145–155 characters**
- Must include: primary keyword + NJ/county location + a clear CTA
- Format: `[Benefit] [service] in [location]. [Trust signal]. [CTA].`
- ✅ Good: `Expert drywall repair across New Jersey. Licensed & insured, same-day available. Free estimate — call or book online.`
- ❌ Bad: `We do drywall repair. Contact us.`

### 3. Heading Hierarchy
- **One H1 per page** — contains the primary keyword
- H2s = major sections, each with a secondary keyword
- H3s = subsections inside H2s
- Never skip levels (H1 → H3 without H2 is wrong)
- ✅ Good H2: `Affordable Drywall Repair in Bergen County`

### 4. NJ Counties — Priority Order

| Priority | County | Key Towns |
|---|---|---|
| 1 | Bergen | Hackensack, Paramus, Fort Lee, Teaneck, Englewood |
| 2 | Essex | Newark, Montclair, Bloomfield, Maplewood, South Orange |
| 3 | Middlesex | New Brunswick, Edison, Woodbridge, Piscataway, Old Bridge |
| 4 | Monmouth | Red Bank, Long Branch, Freehold, Asbury Park, Middletown |
| 5 | Morris | Morristown, Parsippany, Rockaway, Madison, Dover |
| 6 | Hudson | Jersey City, Hoboken, Bayonne, Union City, Weehawken |
| 7 | Union | Elizabeth, Westfield, Summit, Plainfield, Linden |
| 8 | Ocean | Toms River, Lakewood, Brick, Jackson, Barnegat |
| 9 | Somerset | Bridgewater, Somerville, Bound Brook, Raritan |
| 10 | Passaic | Paterson, Clifton, Passaic, Wayne, Pompton Lakes |
| 11–21 | Camden, Burlington, Mercer, Atlantic, Gloucester, Cumberland, Cape May, Warren, Sussex, Hunterdon, Salem | — |

### 5. Keyword Patterns

For every service, target:
- `[service] New Jersey` / `[service] NJ`
- `cheap [service] New Jersey` / `affordable [service] NJ`
- `[service] [County] NJ` (e.g. `drywall repair Bergen County NJ`)
- `[service] near me NJ`
- `best [service] New Jersey`
- `licensed [service] contractor NJ`
- `[service] cost New Jersey` / `[service] price NJ`

### 6. Schema Markup (JSON-LD)

Insert inside `<script type="application/ld+json">` just before `</head>`.

**Homepage → LocalBusiness:**
```json
{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "name": "The Fix Wizard",
  "description": "Professional home repair services across New Jersey",
  "url": "https://thefixwizard.com",
  "telephone": "(555) 123-4567",
  "email": "hello@handypro.com",
  "areaServed": {"@type": "State", "name": "New Jersey"},
  "priceRange": "$$",
  "openingHours": "Mo-Sa 07:00-19:00"
}
```

**Service pages → Service:**
```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "[Service Name]",
  "provider": {"@type": "LocalBusiness", "name": "The Fix Wizard"},
  "areaServed": {"@type": "State", "name": "New Jersey"},
  "description": "[meta description text]"
}
```

**Blog posts → Article + BreadcrumbList:**
```json
[
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "[article title]",
    "author": {"@type": "Organization", "name": "The Fix Wizard"},
    "publisher": {"@type": "Organization", "name": "The Fix Wizard"},
    "datePublished": "YYYY-MM-DD",
    "description": "[meta description]"
  },
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://thefixwizard.com"},
      {"@type": "ListItem", "position": 2, "name": "[Service]", "item": "https://thefixwizard.com/[service]-new-jersey/"},
      {"@type": "ListItem", "position": 3, "name": "[Article Title]", "item": "https://thefixwizard.com/[service]-new-jersey/[slug]/"}
    ]
  }
]
```

**FAQ sections → FAQPage:**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[question text]",
      "acceptedAnswer": {"@type": "Answer", "text": "[answer text]"}
    }
  ]
}
```

### 7. Image Alt Text
- Every `<img>` must have a descriptive `alt` attribute
- Format: `[what is shown] — [service] in [location], NJ`
- ✅ Good: `Technician replacing garage door spring — garage door repair in Bergen County, NJ`
- ❌ Bad: `image.jpg` or empty alt

### 8. Content Quality
- Minimum **300 words** of unique body content per page
- Mention county names naturally (not stuffed)
- Include **price ranges** (helps with cost/cheap/affordable queries)
- Trust signals on every page: licensed, insured, same-day, free estimate
- FAQ sections improve dwell time and target question-based queries
- No duplicate content across pages

### 9. Internal Linking
- Blog posts → link back to parent service page with keyword anchor text
  - ✅ `drywall repair in New Jersey`
  - ❌ `click here`
- Service pages → link to their 3 related blog posts
- County pages → link to parent service page + 1–2 blog posts

### 10. County Landing Page Template

Create at: `/[service]-[county]-new-jersey/index.html`

- **H1:** `[Service] in [County] County, NJ | The Fix Wizard`
- Mention the county **5–8 times** naturally in body text
- Reference **3–5 real towns** in that county
- Note local housing characteristics (age, style, common issues)
- **Minimum 400 words**
- **Meta title:** under 60 chars, include county + service
- **Meta description:** 150 chars, include county + service + CTA
- Add Service schema + LocalBusiness schema
- Link back to parent service page
- Use same CSS/HTML structure as existing service pages

### 11. Location in Every Heading

- H3s should include the location, not just H1
- Format: `[Specific Service] in [County] County, NJ`
- ✅ Good H3: `Garage Door Spring Repair in Bergen County, NJ`
- ❌ Bad H3: `Spring Repair Services`
- This targets long-tail queries and reinforces geo-relevance deeper in the page

### 12. Sub-Area Expansion on County Pages

- Don't just list 3–5 towns — go deeper with neighborhoods, boroughs, townships
- Mention sub-areas naturally in body text: "We serve homeowners across Bergen County — from Hackensack and Paramus to Fort Lee, Englewood, and the surrounding neighborhoods"
- This captures hyperlocal "near me" queries
- Aim for 6–10 specific place names per county page

### 13. On-Page Trust Signals

Every service page and county landing page should include:
- **Star rating with review count** — e.g., `Rated 4.9 on Google (120+ reviews)` — above the fold
- **License number** — displaying the actual NJ contractor license # builds trust and targets `licensed [service] NJ` queries
- **Clickable phone number** — use `<a href="tel:+15551234567">` for every phone mention, not just in the footer
- **Insurance/bonding line** — "Licensed, bonded & insured in New Jersey"
- Place at least one trust signal in the hero section, before the fold

### 14. Semantic Keyword Modifiers

Pair every primary keyword with these modifiers across headings and body text:
- `expert [service] NJ` / `certified [service] contractor NJ`
- `professional [service] New Jersey`
- `top-rated [service] NJ`
- `trusted [service] company NJ`
- Rotate modifiers — don't repeat the same one more than twice per page
- ✅ Good: `Expert Drywall Repair in Bergen County, NJ`
- ✅ Good: `Certified Handyman in New Jersey — Free Estimates`

### 15. Hub-and-Spoke Page Architecture

- **Hub** = service landing page (e.g., `/drywall-repair-new-jersey/`)
- **Spokes** = county pages (e.g., `/drywall-repair-bergen-county-new-jersey/`)
- **Supporting content** = blog posts (e.g., `/drywall-repair-new-jersey/how-to-fix-drywall-water-damage/`)
- Every spoke links back to its hub with keyword anchor text
- Every hub links out to its spokes
- Blog posts link to the hub (not directly to spokes)
- This creates a clear topical cluster that Google can crawl and understand

### 17. Commit Convention

```bash
git config user.email 'seo-agent@thefixwizard.com'
git config user.name 'Fix Wizard SEO Agent'
git add -A
git commit -m "SEO: [short description of what was done]"
git push origin main
```

---

## How to Run the Agent

1. Open the routine: https://claude.ai/code/routines/trig_013DDJTa67jdrM8gzU3EsxZf
2. Edit the prompt — replace `# YOUR TASK` at the bottom with your specific instruction
3. Hit **Run**

Example tasks:
- `Add JSON-LD schema to every blog post that is missing it`
- `Create a Bergen County drywall repair landing page`
- `Fix all title tags over 60 characters across service pages`
- `Refresh meta descriptions on plumbing and electrical pages to target affordable/cheap keywords`
- `Add FAQPage schema to all service pages that have a FAQ section`
