#!/usr/bin/env python3
"""Generate the 360Prosolutions static product site. Run: python3 build.py"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://360prosolutions.pages.dev"
STORE = "https://360prosolutions.gumroad.com"

CSS = """/* 360Prosolutions — static site styles */
:root{
  --blue:#2563eb; --purple:#7c3aed; --ink:#1e293b; --muted:#64748b;
  --bg:#f8fafc; --card:#ffffff; --radius:14px;
}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  color:var(--ink);background:var(--bg);line-height:1.65}
a{color:var(--blue)}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
.site-header{background:linear-gradient(120deg,var(--blue),var(--purple));color:#fff}
.site-header .wrap{display:flex;align-items:center;justify-content:space-between;padding:16px 20px}
.brand{color:#fff;text-decoration:none;font-weight:800;font-size:1.25rem;letter-spacing:.2px}
.brand span{font-weight:400;opacity:.85}
.nav a{color:#fff;text-decoration:none;margin-left:18px;font-size:.95rem;opacity:.95}
.nav a:hover{opacity:1;text-decoration:underline}
.hero{background:linear-gradient(120deg,var(--blue),var(--purple));color:#fff;padding:64px 0 72px}
.hero h1{font-size:2.4rem;line-height:1.25;margin:0 0 14px;max-width:760px}
.hero p{font-size:1.12rem;opacity:.94;max-width:640px;margin:0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;padding:40px 0 56px}
.card{background:var(--card);border-radius:var(--radius);padding:24px;
  box-shadow:0 2px 10px rgba(30,41,59,.07);display:flex;flex-direction:column}
.card h3{margin:0 0 8px;font-size:1.15rem}
.card p{color:var(--muted);font-size:.95rem;margin:0 0 16px;flex:1}
.card .row{display:flex;align-items:center;justify-content:space-between}
.price{font-weight:800;font-size:1.15rem;color:var(--purple)}
.btn{display:inline-block;background:linear-gradient(120deg,var(--blue),var(--purple));color:#fff;
  text-decoration:none;padding:10px 22px;border-radius:999px;font-weight:700;font-size:.95rem}
.btn:hover{filter:brightness(1.06)}
.btn.big{font-size:1.15rem;padding:16px 44px;margin:8px 0 4px}
.product{padding:44px 0 60px}
.product h1{font-size:2rem;margin:0 0 6px}
.price-tag{display:inline-block;background:#ede9fe;color:#5b21b6;font-weight:800;
  padding:6px 18px;border-radius:999px;margin:10px 0 20px;font-size:1.1rem}
.product .lede{font-size:1.08rem}
.faq{margin-top:36px}
.faq h2{font-size:1.35rem}
details{background:var(--card);border-radius:10px;padding:14px 18px;margin:10px 0;
  box-shadow:0 1px 5px rgba(30,41,59,.06)}
summary{font-weight:700;cursor:pointer}
.buybox{background:var(--card);border-radius:var(--radius);padding:30px;text-align:center;
  box-shadow:0 2px 10px rgba(30,41,59,.07);margin:36px 0}
.buybox .note{color:var(--muted);font-size:.9rem;margin:10px 0 0}
.back{display:inline-block;margin-top:8px}
.site-footer{background:#0f172a;color:#cbd5e1;padding:34px 0;margin-top:20px}
.site-footer a{color:#fff}
.site-footer p{margin:6px 0;font-size:.92rem}
@media(max-width:640px){
  .hero{padding:44px 0 52px}
  .hero h1{font-size:1.7rem}
  .product h1{font-size:1.55rem}
}
"""

ROBOTS = f"""User-agent: *
Allow: /
Sitemap: {BASE}/sitemap.xml
"""

PRODUCTS = [
 dict(slug="raast-qr-toolkit", name="RAAST QR Toolkit", price="$9",
      url=f"{STORE}/l/raast-qr-toolkit", seo="raast qr code generator pakistan",
      tagline="SBP-compliant RAAST QR codes, generated offline in one HTML file.",
      meta="Generate SBP-compliant RAAST QR codes offline. P2P, Merchant and EMVCo formats in one HTML file. $9 one-time.",
      paras=[
        "If you take payments through RAAST in Pakistan, you need a QR code your customers can scan. The RAAST QR Toolkit generates one in seconds — type in your account details, get a scannable QR code, print it or share it.",
        "Everything runs in a single HTML file on your own computer. No internet needed, no account to create, and your details are never uploaded anywhere.",
        "It covers the formats SBP published: P2P QR codes (SBP native tags), Merchant QR codes (PK.SBP.RAAST), and standard EMVCo — plus a payload-to-QR mode for anything custom.",
      ],
      faqs=[
        ("Do I need the internet to use it?",
         "No. The file works fully offline in any modern browser — Chrome, Edge, or Firefox."),
        ("Is it SBP compliant?",
         "Yes. The QR formats follow the RAAST QR specifications published by the State Bank of Pakistan."),
        ("What exactly do I receive?",
         "One HTML file (about 71 KB). Open it, fill in your details, download your QR as an image."),
        ("Who is it for?",
         "Pakistani freelancers, shopkeepers, and small merchants who accept RAAST payments and want a correct, scannable QR code."),
      ]),
 dict(slug="wp-link-doctor", name="WP Link Doctor", price="$29",
      url=f"{STORE}/l/wp-link-doctor", seo="find broken links wordpress plugin",
      tagline="Find every broken link on WordPress and fix each in one click.",
      meta="Find every broken link on your WordPress site and fix each in one click. $29 one-time, no yearly fee.",
      paras=[
        "Broken links quietly hurt a WordPress site — every 404 tells visitors (and Google) the site isn't maintained. WP Link Doctor scans your whole site and lists every broken link it finds.",
        "Fixing is one click per link: create a 301 redirect for your own moved pages, or unlink a dead external link while keeping the text. No editing posts by hand.",
        "$29 once, yours forever. No yearly fee.",
      ],
      faqs=[
        ("Will it slow down my site?",
         "No. Scans run in small batches of 25 links through WP-Cron, in the background."),
        ("What can it fix?",
         "Moved internal pages (301 redirect, one click) and dead external links (one-click unlink, text stays)."),
        ("Is it really a one-time payment?",
         "Yes. $29 once — no subscription, no renewal."),
        ("Do I need technical skills?",
         "No. Install it like any WordPress plugin, press scan, click to fix."),
      ]),
 dict(slug="price-drop-alert-bot", name="Price Drop Alert Bot", price="$22",
      url=f"{STORE}/l/price-drop-alert-bot", seo="price drop alert bot",
      tagline="Get pinged on email, Telegram and WhatsApp when a price drops.",
      meta="Track any product's price and get pinged on email, Telegram and WhatsApp when it drops. $22 one-time.",
      paras=[
        "Add the product pages you care about, set the price you'd happily pay, and the bot watches them for you.",
        "When a price drops to (or below) your target, you get pinged — on email, Telegram, and WhatsApp. No more checking the same page every day.",
        "$22 one-time. Full setup instructions are included.",
      ],
      faqs=[
        ("How do I get alerts?",
         "Email, Telegram, and WhatsApp — pick whichever you actually read."),
        ("Which products can I track?",
         "Any product page you add — paste the link and set your target price."),
        ("Is there a monthly fee?",
         "No. $22 once."),
        ("Do I need technical skills?",
         "No. The included setup guide walks you through it step by step."),
      ]),
 dict(slug="email-to-notion-saver", name="Email-to-Notion Saver", price="$22",
      url=f"{STORE}/l/email-to-notion-saver", seo="save gmail to notion automatically",
      tagline="Turn Gmail emails into Notion tasks automatically.",
      meta="Turn Gmail emails into Notion tasks automatically. Never lose an action item in your inbox again. $22 one-time.",
      paras=[
        "Important emails get buried. The Email-to-Notion Saver turns Gmail messages into Notion tasks automatically, so action items land where you actually track work.",
        "You decide what gets saved — by sender, subject, or label — and each email becomes a task in the Notion database you choose, with the key details carried over.",
        "$22 one-time. Works with your existing Gmail and Notion accounts; setup instructions included.",
      ],
      faqs=[
        ("What do I need?",
         "A Gmail account and a Notion account — the free Notion plan works."),
        ("Do I need to code?",
         "No. Follow the included setup steps."),
        ("Which emails get saved?",
         "You choose — filter by sender, subject keyword, or Gmail label."),
        ("Is there a subscription?",
         "No. $22 once."),
      ]),
 dict(slug="telegram-ai-assistant-bot", name="Telegram AI Assistant Bot", price="$29",
      url=f"{STORE}/l/telegram-ai-assistant-bot", seo="telegram ai assistant bot",
      tagline="Your own ChatGPT inside Telegram, via n8n. Needs your own API keys.",
      meta="Your own ChatGPT inside Telegram via an n8n workflow. $29 one-time. Requires your own Telegram bot token, OpenAI key, and n8n.",
      paras=[
        "This is an n8n workflow you import: it turns a Telegram bot into your own AI assistant, answering right inside Telegram.",
        "Honest limits, up front: you need your own Telegram bot token (free from BotFather), your own OpenAI API key — ChatGPT usage is billed pay-as-you-go by OpenAI, it is not free — and n8n to run the workflow on.",
        "If you already use n8n, setup takes minutes: import the workflow, paste your two keys, and your bot starts answering. $29 one-time.",
      ],
      faqs=[
        ("What do I need to run it?",
         "Three things: a Telegram bot token (free), an OpenAI API key (pay-as-you-go), and n8n."),
        ("Is the AI usage free?",
         "No. OpenAI charges per use on your own key. The $29 is for the workflow, not for AI credits."),
        ("Do I need to code?",
         "No code — but you should be comfortable importing a workflow in n8n."),
        ("Has it been tested?",
         "The workflow has been reviewed and is ready to import; final testing happens with your own keys in your own n8n."),
      ]),
 dict(slug="freelancer-client-os", name="Freelancer Client OS", price="$29",
      url=f"{STORE}/l/freelancer-client-os", seo="freelancer client management software",
      tagline="Clients, projects and invoices in one file. Works offline.",
      meta="Clients, projects and invoices in one file. Works offline, no monthly fee. $29 one-time.",
      paras=[
        "Freelancer Client OS keeps your whole freelance operation in one place: clients, projects, and invoices — no juggling five apps.",
        "It works offline and there's no monthly fee. Your data stays yours, in one file you control.",
        "$29 one-time. Built for freelancers who want the business side handled without another subscription.",
      ],
      faqs=[
        ("What does it track?",
         "Clients, projects, and invoices — the three things every freelancer juggles."),
        ("Does it need the internet?",
         "No. It works offline."),
        ("Is there a monthly fee?",
         "No. $29 once."),
        ("Who is it for?",
         "Freelancers and solo consultants who want one simple system instead of five tools."),
      ]),
 dict(slug="gdrive-explorer", name="GDrive Explorer", price="Free",
      url=f"{STORE}/l/gdrive-explorer", seo="manage multiple google drive accounts",
      tagline="Manage all your Google Drive accounts in one free web app.",
      meta="Free web app: manage all your Google Drive accounts in one window. Also live at gdrive-explorer.pages.dev.",
      paras=[
        "If you juggle several Google Drive accounts, switching between them is a chore. GDrive Explorer puts all your Drives in one window.",
        "Browse, preview, and manage files across accounts without logging in and out. Text files open in a built-in viewer with selectable text and a copy button.",
        "It's free — and it's also live as a web app at gdrive-explorer.pages.dev, so you can use it right in the browser with nothing to install.",
      ],
      faqs=[
        ("Is it really free?",
         "Yes. Free, no account needed."),
        ("Do I install anything?",
         "No — it runs in your browser."),
        ("Can I copy text from files?",
         "Yes — the text viewer lets you select text and has a copy button."),
        ("Where can I use it?",
         "Grab it here, or use it live at gdrive-explorer.pages.dev."),
      ]),
 dict(slug="drive-sync-pro", name="Drive Sync Pro", price="$4.99",
      url=f"{STORE}/l/Drive-Sync-Pro", seo="google drive bulk uploader",
      tagline="Bulk-upload to Google Drive and clone shared folders from a link.",
      meta="Bulk-upload folder structures to Google Drive and clone shared folders from a link — no download. $4.99 one-time.",
      paras=[
        "Drive Sync Pro moves files into Google Drive in bulk: upload whole folder structures at once, or clone a shared folder straight from its link — no downloading to your computer first.",
        "Every transfer is logged in an Excel audit file, so you can see exactly what moved, when, and where.",
        "It runs on your own Google Apps Script — your data never passes through a third-party server. $4.99 one-time.",
      ],
      faqs=[
        ("How does it run?",
         "On your own Google Apps Script account — setup steps are included."),
        ("Does my data go through your servers?",
         "No. Everything runs between you and Google."),
        ("What does the audit log include?",
         "An Excel file listing every transferred file."),
        ("Can it clone shared folders?",
         "Yes — paste a shared folder link and it copies the contents into your Drive, with no download step."),
      ]),
 dict(slug="elementor-pro-gpl", name="Free Elementor Pro 4.3.2 (GPL)", price="Free",
      url=f"{STORE}/l/FreeElementorPro", seo="elementor pro gpl",
      tagline="Elementor Pro page builder under GPL. Pay what you want.",
      meta="Elementor Pro 4.3.2 page builder under GPL. Pay what you want (even $0), unlimited sites, no license key. 35+ downloads.",
      paras=[
        "The Elementor Pro page builder, version 4.3.2, distributed under the GNU General Public License. Same plugin, GPL terms: use it on unlimited sites with no license key.",
        "Pay what you want — including $0. Downloaded 35+ times from the store.",
        "Distributed under the GNU General Public License (GPL). Not affiliated with Elementor.com.",
      ],
      faqs=[
        ("Is this legal?",
         "Yes. GPL-licensed software can be freely redistributed — that's what the license is for."),
        ("Do I need a license key?",
         "No. Install it and use it on as many sites as you like."),
        ("Which version is included?",
         "Version 4.3.2, as listed. Check the store page for the latest file."),
        ("Is this affiliated with Elementor.com?",
         "No. Not affiliated with Elementor.com."),
      ]),
 dict(slug="wp-rocket-gpl", name="WP Rocket 3.23.5.1 (GPL)", price="Free",
      url=f"{STORE}/l/wp-rocket-gpl", seo="wp rocket gpl",
      tagline="WordPress caching plugin under GPL. Pay what you want.",
      meta="WP Rocket 3.23.5.1 caching plugin under GPL. Pay what you want, unlimited sites. Not affiliated with WP Rocket.",
      paras=[
        "WP Rocket 3.23.5.1 — the popular WordPress caching plugin — distributed under the GNU General Public License.",
        "Caching, file optimization, and lazy loading for faster WordPress sites. Pay what you want, use on unlimited sites, no license key.",
        "Distributed under the GNU General Public License (GPL). Not affiliated with WP Rocket.",
      ],
      faqs=[
        ("Is this legal?",
         "Yes. GPL-licensed software can be freely redistributed — that's what the license is for."),
        ("Do I need a license key?",
         "No. Install it and use it on as many sites as you like."),
        ("Which version is included?",
         "Version 3.23.5.1, as listed. Check the store page for the latest file."),
        ("Is this affiliated with WP Rocket?",
         "No. Not affiliated with WP Rocket."),
      ]),
 dict(slug="wp-media-doctor", name="WP Media Doctor", price="$19",
      url=f"{STORE}/l/wp-media-doctor", seo="clean unused wordpress media files",
      tagline="Find and clean unused files in your WordPress media library.",
      meta="Find and safely clean unused media files cluttering your WordPress media library. $19 one-time. From the makers of WP Link Doctor.",
      paras=[
        "WordPress media libraries fill up with images nobody uses — old uploads, duplicates, leftovers from deleted posts. WP Media Doctor finds the files nothing on your site references.",
        "Review the list, then clean with confidence. It's built by the makers of WP Link Doctor, with the same careful approach: nothing is removed without your say-so.",
        "$19 one-time, no yearly fee.",
      ],
      faqs=[
        ("Is it safe?",
         "It only lists unused files — you review the list before anything is removed."),
        ("Will it delete files my site uses?",
         "No. It finds files nothing references; you confirm each cleanup."),
        ("Is it a one-time payment?",
         "Yes. $19 once."),
        ("Who made it?",
         "The makers of WP Link Doctor."),
      ]),
 dict(slug="job-cost-estimator", name="Contractor Job Cost Estimator", price="$39",
      url=f"{STORE}/l/job-cost-estimator", seo="contractor job cost estimator spreadsheet",
      tagline="Estimate → quote → invoice in one Google Sheet.",
      meta="Estimate → quote → invoice in one Google Sheet. Checkbox ticks generate QUO/INV numbers. $39 one-time.",
      paras=[
        "Price every job right. The Contractor Job Cost Estimator takes you from estimate to quote to invoice in a single Google Sheet.",
        "Tick checkboxes as you work — quote numbers (QUO-0001…) and invoice numbers (INV-0001…) generate automatically, so your paperwork stays in order.",
        "It's a Google Sheet, so it works anywhere Sheets does. $39 one-time.",
      ],
      faqs=[
        ("What do I need?",
         "A Google account (free) to copy and use the Sheet."),
        ("How do quote and invoice numbers work?",
         "Tick the checkbox on a row and the next QUO/INV number is assigned automatically."),
        ("Is it really one sheet?",
         "Yes — estimate, quote, and invoice in one file."),
        ("Is it a one-time payment?",
         "Yes. $39 once."),
      ]),
 dict(slug="ai-audit-generator", name="AI Audit Generator", price="$29",
      url=f"{STORE}/l/ai-audit-generator", seo="website audit tool for agencies",
      tagline="1-page website audits with 17 checks and a score out of 100.",
      meta="Win local clients with 1-page website audits: 17 real checks, score out of 100. Google Sheet. $29 one-time.",
      paras=[
        "Walk into any local business with a one-page audit of their website and you have their attention. The AI Audit Generator produces that page.",
        "It runs 17 real checks — SSL, mobile-friendliness, SEO title, tap-to-call, and more — then scores the site out of 100 with a plain-words verdict.",
        "It's a Google Sheet, and buyers get their own copy. $29 one-time.",
      ],
      faqs=[
        ("What does it check?",
         "17 things: SSL, mobile layout, SEO title, tap-to-call buttons, and more."),
        ("What do I get?",
         "Your own copy of the Google Sheet — issued automatically after purchase."),
        ("Do I need to code?",
         "No."),
        ("Is it a one-time payment?",
         "Yes. $29 once."),
      ]),
]

HEADER = """<header class="site-header"><div class="wrap">
<a class="brand" href="index.html">360<span>Prosolutions</span></a>
<nav class="nav"><a href="index.html">All products</a><a href="https://360prosolutions.gumroad.com" target="_blank" rel="noopener">Store</a></nav>
</div></header>"""

FOOTER = f"""<footer class="site-footer"><div class="wrap">
<p><strong>360Prosolutions</strong> — practical tools for creators, developers and freelancers. No fluff, no subscriptions.</p>
<p>Checkout happens on our Gumroad store: <a href="{STORE}" target="_blank" rel="noopener">360prosolutions.gumroad.com</a></p>
</div></footer>"""


def head(title, meta, canonical):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{meta}">
<link rel="canonical" href="{canonical}">
<link rel="stylesheet" href="style.css">
</head>
<body>
"""


def product_page(p):
    paras = "\n".join(f'<p class="lede">{x}</p>' if i == 0 else f"<p>{x}</p>"
                      for i, x in enumerate(p["paras"]))
    faqs = "\n".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in p["faqs"])
    price_label = "Free" if p["price"] == "Free" else f"{p['price']} one-time"
    return (head(f"{p['name']} — {p['seo']} | 360Prosolutions", p["meta"], f"{BASE}/{p['slug']}.html")
        + HEADER
        + f"""<main class="wrap product">
<h1>{p['name']}</h1>
<div class="price-tag">{p['price']}</div>
{paras}
<div class="buybox">
<a class="btn big" href="{p['url']}" target="_blank" rel="noopener">Buy Now — {price_label}</a>
<p class="note">Secure checkout on Gumroad. You get the download link right after payment.</p>
</div>
<section class="faq"><h2>Common questions</h2>
{faqs}
</section>
<p><a class="back" href="index.html">&larr; Back to all products</a></p>
</main>
""" + FOOTER + "</body>\n</html>\n")


def index_page():
    cards = "\n".join(
        f"""<div class="card"><h3>{p['name']}</h3><p>{p['tagline']}</p>
<div class="row"><span class="price">{p['price']}</span>
<a class="btn" href="{p['slug']}.html">View</a></div></div>"""
        for p in PRODUCTS)
    return (head("360Prosolutions — practical tools, no subscriptions",
                 "Practical tools for creators, developers and freelancers — no fluff, no subscriptions. WordPress plugins, QR tools, automations and more.",
                 f"{BASE}/index.html")
        + HEADER
        + """<section class="hero"><div class="wrap">
<h1>Practical tools for creators, developers and freelancers — no fluff, no subscriptions.</h1>
<p>One-time payments. Real tools that do one job well. Every purchase is handled securely through our Gumroad store.</p>
</div></section>
<main class="wrap"><div class="grid">
""" + cards + """
</div></main>
""" + FOOTER + "</body>\n</html>\n")


def sitemap():
    urls = ["index.html"] + [p["slug"] + ".html" for p in PRODUCTS]
    items = "\n".join(
        f"  <url><loc>{BASE}/{u}</loc><lastmod>2026-10-23</lastmod><changefreq>monthly</changefreq></url>"
        for u in urls)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{items}
</urlset>
"""


def main():
    with open(os.path.join(OUT, "style.css"), "w") as f:
        f.write(CSS)
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(ROBOTS)
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(index_page())
    for p in PRODUCTS:
        with open(os.path.join(OUT, p["slug"] + ".html"), "w") as f:
            f.write(product_page(p))
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write(sitemap())
    print("wrote", len(PRODUCTS) + 3, "files")


if __name__ == "__main__":
    main()
