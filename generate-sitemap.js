'use strict';
const fs   = require('fs');
const path = require('path');

const BASE = 'https://thefixwizard.com';

// Priority by page type
function priority(slug) {
  if (slug === '')                         return '1.0'; // homepage
  if (slug.endsWith('-repair'))            return '0.9'; // city hubs
  if (slug.startsWith('services/'))        return '0.8'; // service category hubs
  if (slug === 'locations')                return '0.7';
  if (/-near-/.test(slug))                 return '0.7'; // city-specific service pages
  return '0.6';                                          // generic service pages
}

function generate(docsDir) {
  const urls = [];

  function walk(dir, base) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      if (!entry.isDirectory()) continue;
      const slug = base ? `${base}/${entry.name}` : entry.name;
      const indexPath = path.join(dir, entry.name, 'index.html');
      if (fs.existsSync(indexPath)) {
        urls.push(slug);
      }
      walk(path.join(dir, entry.name), slug);
    }
  }

  // Homepage
  urls.push('');
  walk(docsDir, '');

  const today = new Date().toISOString().slice(0, 10);

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map(slug => `  <url>
    <loc>${BASE}/${slug}${slug ? '/' : ''}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${slug === '' ? 'weekly' : 'monthly'}</changefreq>
    <priority>${priority(slug)}</priority>
  </url>`).join('\n')}
</urlset>
`;

  const outPath = path.join(path.dirname(docsDir), 'sitemap.xml');
  fs.writeFileSync(outPath, xml, 'utf8');
  // Also copy to docs/
  fs.writeFileSync(path.join(docsDir, 'sitemap.xml'), xml, 'utf8');
  console.log(`✓ sitemap.xml — ${urls.length} URLs`);
}

if (require.main === module) {
  generate(path.join(__dirname, 'docs'));
}

module.exports = { generate };
