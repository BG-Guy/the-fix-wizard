#!/usr/bin/env python3
"""
FCP fix: adds inline critical CSS + preloads tw.css + loads custom.css async.

What this does:
  - Inserts a ~400-byte <style> with critical initial states (body bg, sp-hero
    bg, loader cover, navbar height, reveal opacity:0, mobile-menu hidden,
    faq-answer hidden) so the browser can paint correctly before tw.css downloads.
  - Adds rel="preload" as="style" for tw.css so the browser starts fetching it
    at top priority the moment it parses <head>.
  - Converts custom.css to async loading (rel="preload" + onload trick) —
    safe because all its critical initial states are now in the inline block.
"""

import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

CRITICAL_CSS = '<style>:root{--nav-h:150px}*,*::before,*::after{box-sizing:border-box}body{font-family:Inter,sans-serif;color:#3a4560;background:#fff;line-height:1.65;overflow-x:hidden}body.no-scroll{overflow:hidden}a{text-decoration:none;color:inherit}.reveal{opacity:0;transform:translateY(28px)}.sp-hero,.hero{background-color:#091236;color:#fff}.mobile-menu{position:fixed;top:0;left:-100%;z-index:101;width:min(320px,88vw);height:100vh;background:#0d1b4b}.mobile-overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:100;opacity:0;visibility:hidden}.faq-answer{max-height:0;overflow:hidden}#navbar{position:fixed;top:0;left:0;right:0;z-index:100;height:var(--nav-h)}.loader{position:fixed;inset:0;background:#0d1b4b;z-index:9999;display:flex;align-items:center;justify-content:center}@media(max-width:768px){:root{--nav-h:96px}}</style>'


def fix_file(filepath):
    with open(filepath) as f:
        content = f.read()

    # Skip if already patched
    if CRITICAL_CSS[:40] in content:
        return False

    changed = False

    # 1. Insert inline critical CSS right before the first <link> tag
    first_link = content.find('<link ')
    if first_link != -1 and CRITICAL_CSS not in content:
        content = content[:first_link] + CRITICAL_CSS + '\n    ' + content[first_link:]
        changed = True

    # 2. Add preload hint for tw.css (right before the existing <link rel="stylesheet" href="...tw.css">)
    #    Extract the tw.css href from the existing link
    tw_pattern = re.compile(r'(<link rel="stylesheet" href="([^"]*tw\.css)">)')
    m = tw_pattern.search(content)
    if m:
        full_tag = m.group(1)
        tw_href  = m.group(2)
        preload  = f'<link rel="preload" href="{tw_href}" as="style">\n    '
        if f'preload" href="{tw_href}"' not in content:
            content = content.replace(full_tag, preload + full_tag, 1)
            changed = True

    # 3. Convert custom.css from blocking to async
    custom_pattern = re.compile(r'<link rel="stylesheet" href="([^"]*custom\.css)">')
    m = custom_pattern.search(content)
    if m:
        old_tag   = m.group(0)
        cust_href = m.group(1)
        new_tag   = (
            f'<link rel="preload" href="{cust_href}" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n'
            f'    <noscript><link rel="stylesheet" href="{cust_href}"></noscript>'
        )
        if 'onload' not in old_tag:
            content = content.replace(old_tag, new_tag, 1)
            changed = True

    if changed:
        with open(filepath, 'w') as f:
            f.write(content)
    return changed


if __name__ == '__main__':
    patched = skipped = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != 'node_modules']
        for fname in filenames:
            if fname != 'index.html':
                continue
            fpath = os.path.join(dirpath, fname)
            if fix_file(fpath):
                patched += 1
            else:
                skipped += 1

    # Also patch partials/head.html (used by build.js for the homepage)
    head = os.path.join(ROOT, 'partials', 'head.html')
    if os.path.exists(head) and fix_file(head):
        print('  ✓  partials/head.html patched')

    print(f'  ✓  {patched} HTML files patched, {skipped} skipped (already done)')
    print('\nDone. Run: node build.js && ./node_modules/.bin/tailwind -i css/input.css -o css/tw.css --minify')
