#!/usr/bin/env python3
"""Builds the ProPodium Events & Hospitality site in two forms:
   out/site/      -> multi-page static site (for the ZIP / hosting)
   out/preview.html -> one-file, hash-routed preview (for the Artifact)"""
import os, re, shutil, base64, json, sys

BASE = os.path.dirname(os.path.abspath(__file__))
IN = os.path.join(BASE, "..", "in")
OUT = os.path.join(BASE, "..", "out")
SITE = os.path.join(OUT, "site")

EMAIL = "EMAIL_AQUI"
PHONE = "TELEFONE_AQUI"
DOMAIN = "https://www.propodiumevents.com"
NAME = "ProPodium Events & Hospitality"
NAME_HTML = "ProPodium Events &amp; Hospitality"
TAGLINE = "The support behind every great event."

logo_light = open(os.path.join(IN, "logo-cores.svg")).read()
icon_svg = open(os.path.join(IN, "icone.svg")).read()
# dark-background variant: same paths, brand's dark-ground fills
logo_dark = (logo_light.replace('fill="#0E9F9C"', 'fill="#2CD4CF"')
                       .replace('fill="#14202B"', 'fill="#FFFFFF"')
                       .replace('fill="#F2B705"', 'fill="#FFC61A"')
                       .replace('fill="#5D6B78"', 'fill="#9FB3BD"'))
logo_inline = re.sub(r'<title>.*?</title>', '', logo_dark).replace(' width="297" height="82"', '').replace('role="img" aria-label="ProPodium Events"', 'aria-hidden="true" focusable="false"')

STAR = '<span class="star" aria-hidden="true"></span>'

def ph(v):
    return f'<span class="placeholder">{v}</span>'

# ---------- page bodies (href() maps page ids to real links per output) ----------
def header(cur, href):
    items = [("home", "Home"), ("about", "About"), ("partners", "Partners")]
    lis = "".join(f'<li><a href="{href(i)}"{" aria-current=\"page\"" if i == cur else ""}>{t}</a></li>' for i, t in items)
    return f'''<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="{href("home")}"><span class="sr-only">{NAME_HTML} home</span>{logo_inline}</a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-links-{cur}">Menu</button>
    <ul class="nav-links" id="nav-links-{cur}">{lis}<li><a class="btn btn-gold" href="{href("contact")}"{" aria-current=\"page\"" if cur == "contact" else ""}>Request a quote</a></li></ul>
  </div>
</header>'''

def footer(href):
    return f'''<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <a class="brand" href="{href("home")}"><span class="sr-only">{NAME_HTML} home</span>{logo_inline}</a>
      <p>{TAGLINE} Executive transportation, on-site coordination and guest welcome across the United States, Mexico, Canada, and Brazil.</p>
    </div>
    <div>
      <h4>Explore</h4>
      <ul>
        <li><a href="{href("home")}">Home</a></li>
        <li><a href="{href("about")}">About</a></li>
        <li><a href="{href("partners")}">Partners</a></li>
        <li><a href="{href("contact")}">Contact</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul>
        <li>{ph(EMAIL)}</li>
        <li>{ph(PHONE)}</li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <span>&copy; 2026 {NAME_HTML}. All rights reserved.</span>
    <span>ProPodium. Professional support, podium-level service.</span>
  </div>
</footer>'''

SERVICES = ["Executive and VIP transportation", "On-site event coordinators",
            "Airport greeters and guest welcome", "Group transportation coordination and event setup"]
EVENTS = [("Formula 1", ["Austin", "Miami", "Las Vegas"]), ("Super Bowl", []), ("NBA All-Star Game", []),
          ("PGA", []), ("Kentucky Derby", []), ("SXSW", []), ("FIFA World Cup", [])]
COUNTRIES = [("United States", "USA"), ("Mexico", "MEX"), ("Canada", "CAN"), ("Brazil", "BRA")]
EVENT_TYPES = ["Corporate events", "Conferences", "Concerts", "Motorsport", "Car and motorcycle shows", "Major sporting events"]

def services_html():
    return "".join(f'<article class="service">{STAR}<h3>{s}</h3></article>' for s in SERVICES)

AUDIENCES = [("Event organizers", "Every guest is welcomed, moved, and looked after without a detail missed."),
             ("Sponsors", "Executive and VIP transportation, airport greeters, and guest welcome for your guests."),
             ("Event-transport companies", "We don&rsquo;t compete with you. We work alongside you as an extension of your team.")]
PILLARS = [("Experience", "Supporting some of the world&rsquo;s most demanding events since 2009."),
           ("Reliability", "We know what it takes to deliver when the stakes are high."),
           ("Hospitality-first", "Every guest welcomed, moved, and looked after.")]

def audiences_html():
    return "".join(f'<article class="service">{STAR}<h3>{t}</h3><p>{d}</p></article>' for t, d in AUDIENCES)

def pillars_html():
    return "".join(f'<div class="pillar"><span class="num">0{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(PILLARS))

def partner_card():
    return f'''<article class="partner">
  <div>
    <h3>Leo Limos</h3>
    <div class="meta">Executive Transportation &nbsp;|&nbsp; Austin, TX</div>
    <p>In the market since 2009, Leo Limos provides premium ground transportation for corporate clients, executives, and major events. Its fleet of Executive Sedans, Executive SUVs, and Executive Sprinter Vans is built for VIP guests, from airport transfers to full-event transportation programs.</p>
    <ul class="fleet"><li>Executive Sedans</li><li>Executive SUVs</li><li>Executive Sprinter Vans</li></ul>
  </div>
  <a class="btn btn-ink" href="https://www.leolimos.com" target="_blank" rel="noopener">Visit Leo Limos &rarr;</a>
</article>'''

def home(href):
    events = "".join(
        f'<li><span class="name">{n}</span>' + (f'<span class="where">{"".join(f"<span>{c}</span>" for c in cities)}</span>' if cities else '') + '</li>'
        for n, cities in EVENTS)
    countries = "".join(f'<li>{c}<small>{code}</small></li>' for c, code in COUNTRIES)
    types = "".join(f"<li>{t}</li>" for t in EVENT_TYPES)
    return f'''<section class="hero">
  <div class="wrap hero-inner">
    <div class="hero-copy">
      <span class="eyebrow">{NAME_HTML}</span>
      <h1>The support behind every <span class="accent">great event.</span></h1>
      <p class="hero-lead">The operational partner behind some of the world&rsquo;s most demanding events. Since 2009, we have supported event organizers, sponsors, and event-transport companies, making sure every guest is welcomed, moved, and looked after without a detail missed.</p>
      <div class="hero-actions">
        <a class="btn btn-gold" href="{href("contact")}">Request a quote</a>
        <a class="btn btn-ghost" href="{href("about")}">About ProPodium</a>
      </div>
    </div>
    <div class="podium" aria-hidden="true">
      <div class="step step-2">2</div>
      <div class="step step-1"><span class="star"></span>1</div>
      <div class="step step-3">3</div>
    </div>
  </div>
  <div class="facts-strip"><div class="wrap facts">
    <span>{STAR}Since 2009</span><span>{STAR}On-site coordination</span><span>{STAR}VIP transportation</span><span>{STAR}United States</span><span>{STAR}Mexico</span><span>{STAR}Canada</span><span>{STAR}Brazil</span>
  </div></div>
</section>

<section class="section tint" id="services">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{STAR}What we do</span>
      <h2>Every guest welcomed, moved, and looked after.</h2>
    </div>
    <div class="services">{services_html()}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{STAR}Who we support</span>
      <h2>Event organizers, sponsors, and event-transport companies.</h2>
    </div>
    <div class="services three">{audiences_html()}</div>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{STAR}Track record</span>
      <h2>We know what it takes to deliver when the stakes are high.</h2>
    </div>
    <ul class="events">{events}</ul>
    <p class="events-note">From Formula 1 in Austin, Miami, and Las Vegas to the Super Bowl, NBA All-Star Game, PGA, Kentucky Derby, SXSW, and the FIFA World Cup, we know what it takes to deliver when the stakes are high.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{STAR}Where we work</span>
      <h2>Across the United States, Mexico, Canada, and Brazil.</h2>
    </div>
    <div class="where-grid">
      <div><span class="label">Countries</span><ul class="countries">{countries}</ul></div>
      <div><span class="label">Events we support</span><ul class="chips">{types}</ul></div>
    </div>
  </div>
</section>

<section class="section tint">
  <div class="wrap approach">
    <div class="section-head" style="margin:0"><span class="eyebrow">{STAR}Our approach</span><h2>An extension of your team.</h2></div>
    <blockquote>We don&rsquo;t compete with the companies we support. We work alongside them as an extension of their team, bringing <span class="hl">experience, reliability, and a hospitality-first mindset</span> to every event.</blockquote>
  </div>
  <div class="wrap"><div class="pillars">{pillars_html()}</div></div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{STAR}Our partners</span>
      <h2>The support behind every great event is built on trusted relationships.</h2>
    </div>
    {partner_card()}
    <p style="margin-top:20px"><a href="{href("partners")}" style="font-weight:600">See all partners &rarr;</a></p>
  </div>
</section>

{cta(href)}'''

def cta(href):
    return f'''<section class="cta">
  <div class="wrap cta-inner">
    <h2>ProPodium. <span class="muted">Professional support, podium-level service.</span></h2>
    <a class="btn btn-ink" href="{href("contact")}">Request a quote</a>
  </div>
</section>'''

def about(href):
    svc = "".join(f"<li>{STAR}<span>{s}</span></li>" for s in SERVICES)
    return f'''<section class="page-hero"><div class="wrap">
  <span class="eyebrow">{STAR}About us</span>
  <h1>About {NAME_HTML}</h1>
  <p>{TAGLINE}</p>
</div></section>
<section class="section"><div class="wrap about-grid">
  <div class="prose">
    <p class="lead">{NAME_HTML} is the operational partner behind some of the world&rsquo;s most demanding events. Since 2009, we have supported event organizers, sponsors, and event-transport companies, making sure every guest is welcomed, moved, and looked after without a detail missed.</p>
    <p>From Formula 1 in Austin, Miami, and Las Vegas to the Super Bowl, NBA All-Star Game, PGA, Kentucky Derby, SXSW, and the FIFA World Cup, we know what it takes to deliver when the stakes are high.</p>
    <h2>What we do</h2>
    <ul>{svc}</ul>
    <h2>Where we work</h2>
    <p>Across the United States, Mexico, Canada, and Brazil, for corporate events, conferences, concerts, motorsport, car and motorcycle shows, and major sporting events.</p>
    <h2>Our approach</h2>
    <p>We don&rsquo;t compete with the companies we support. We work alongside them as an extension of their team, bringing experience, reliability, and a hospitality-first mindset to every event.</p>
    <p class="signoff">ProPodium. Professional support, podium-level service.</p>
  </div>
  <aside class="aside" aria-label="At a glance">
    <dl>
      <div><dt>Supporting events since</dt><dd>2009</dd></div>
      <div><dt>Countries</dt><dd>United States, Mexico, Canada, Brazil</dd></div>
      <div><dt>We support</dt><dd>Event organizers, sponsors, and event-transport companies</dd></div>
    </dl>
    <a class="btn btn-ink" href="{href("contact")}">Request a quote</a>
  </aside>
</div></section>
{cta(href)}'''

def partners(href):
    return f'''<section class="page-hero"><div class="wrap">
  <span class="eyebrow">{STAR}Partners</span>
  <h1>Our Partners</h1>
  <p>The support behind every great event is built on trusted relationships.</p>
</div></section>
<section class="section tint"><div class="wrap">
  <div class="section-head"><p style="color:var(--ink);font-size:1.15rem">At {NAME_HTML}, we work alongside experienced companies that share our commitment to reliability and guest experience. Our partners help us deliver seamless events across the United States and beyond.</p></div>
  {partner_card()}
  <div class="partner-soon">{STAR}More partners coming soon.</div>
</div></section>
{cta(href)}'''

def contact(href, preview):
    checks = "".join(f'<label><input type="checkbox" name="services" value="{s}" id="svc-{i}"> {s}</label>' for i, s in enumerate(SERVICES))
    note = ("This is a preview: the form does not send messages yet." if preview
            else "Sending opens your email app with the details filled in.")
    return f'''<section class="page-hero"><div class="wrap">
  <span class="eyebrow">{STAR}Contact</span>
  <h1>Request a quote for your event</h1>
  <p>{TAGLINE}</p>
</div></section>
<section class="section"><div class="wrap contact-grid">
  <div class="contact-info">
    <h2>Planning an event?</h2>
    <p>Tell us about the event, the dates, the number of guests, and the support you need. We work across the United States, Mexico, Canada, and Brazil.</p>
    <dl class="contact-lines">
      <div><dt>Email</dt><dd>{ph(EMAIL)}</dd></div>
      <div><dt>Phone</dt><dd>{ph(PHONE)}</dd></div>
    </dl>
  </div>
  <form class="form" id="contact-form" novalidate>
    <div class="form-row">
      <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="f-company">Company</label><input id="f-company" name="company" autocomplete="organization"></div>
    </div>
    <div class="form-row">
      <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
    </div>
    <div class="form-row">
      <div class="field"><label for="f-event">Event and city</label><input id="f-event" name="event"></div>
      <div class="field"><label for="f-dates">Dates</label><input id="f-dates" name="dates"></div>
    </div>
    <div class="form-row">
      <div class="field"><label for="f-guests">Number of guests</label><input id="f-guests" name="guests" inputmode="numeric"></div>
      <div class="field"><label for="f-airport">Airport arrivals</label><input id="f-airport" name="airport" placeholder="e.g. AUS, MIA, LAS"></div>
    </div>
    <fieldset class="field"><legend>Services needed</legend><div class="checks">{checks}</div></fieldset>
    <div class="field"><label for="f-message">Message</label><textarea id="f-message" name="message"></textarea></div>
    <div><button class="btn btn-gold" type="submit">Send request</button></div>
    <p class="form-note">{note}</p>
    <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
  </form>
</div></section>'''

PAGES = {
    "home": ("ProPodium Events & Hospitality | The support behind every great event",
             "ProPodium Events & Hospitality is the operational partner behind demanding events since 2009: executive and VIP transportation, on-site coordinators, airport greeters and group transportation across the US, Mexico, Canada and Brazil."),
    "about": ("About | ProPodium Events & Hospitality",
              "Since 2009, ProPodium Events & Hospitality has supported event organizers, sponsors and event-transport companies at Formula 1, the Super Bowl, the FIFA World Cup and more."),
    "partners": ("Our Partners | ProPodium Events & Hospitality",
                 "ProPodium Events & Hospitality works alongside experienced companies that share its commitment to reliability and guest experience, including Leo Limos in Austin, TX."),
    "contact": ("Contact | ProPodium Events & Hospitality",
                "Contact ProPodium Events & Hospitality for executive transportation, on-site event coordination and guest welcome in the US, Mexico, Canada and Brazil."),
}
FILES = {"home": "index.html", "about": "about.html", "partners": "partners.html", "contact": "contact.html"}

JS_COMMON = r'''
(function () {
  document.querySelectorAll('.menu-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var list = document.getElementById(btn.getAttribute('aria-controls'));
      var open = list.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
})();
'''

JS_FORM_SITE = r'''
(function () {
  var form = document.getElementById('contact-form');
  if (!form) return;
  var TO = 'EMAIL_AQUI';
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var status = document.getElementById('form-status');
    var name = form.name.value.trim(), email = form.email.value.trim();
    if (!name || !email || !form.email.checkValidity()) {
      status.className = 'form-status error';
      status.textContent = 'Please add your name and a valid email address.';
      return;
    }
    var svc = Array.prototype.slice.call(form.querySelectorAll('input[name="services"]:checked')).map(function (c) { return c.value; });
    var body = 'Name: ' + name + '\nCompany: ' + form.company.value + '\nEmail: ' + email + '\nPhone: ' + form.phone.value +
      '\nEvent and city: ' + form.event.value + '\nDates: ' + form.dates.value + '\nGuests: ' + form.guests.value + '\nAirport arrivals: ' + form.airport.value + '\nServices: ' + svc.join(', ') + '\n\n' + form.message.value;
    window.location.href = 'mailto:' + TO + '?subject=' + encodeURIComponent('Quote request from ' + name) + '&body=' + encodeURIComponent(body);
    status.className = 'form-status';
    status.textContent = 'Your email app should open with the message ready to send.';
  });
})();
'''

JS_FORM_PREVIEW = r'''
(function () {
  var form = document.getElementById('contact-form');
  if (!form) return;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var status = document.getElementById('form-status');
    if (!form.name.value.trim() || !form.email.value.trim() || !form.email.checkValidity()) {
      status.className = 'form-status error';
      status.textContent = 'Please add your name and a valid email address.';
      return;
    }
    status.className = 'form-status';
    status.textContent = 'Preview only: on the live site this message goes to your contact email.';
  });
})();
'''

JS_ROUTER = r'''
(function () {
  var ids = ['home', 'about', 'partners', 'contact'];
  function show() {
    var id = (location.hash || '#home').slice(1);
    if (ids.indexOf(id) < 0) id = 'home';
    ids.forEach(function (p) { document.getElementById('page-' + p).hidden = (p !== id); });
    document.querySelectorAll('.nav-links.open').forEach(function (l) { l.classList.remove('open'); });
    window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', show);
  show();
})();
'''

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:ital,wght@0,500;0,600;0,700;0,800;1,600;1,700&display=swap">'

def jsonld():
    data = {"@context": "https://schema.org", "@type": "Organization", "name": NAME,
            "url": DOMAIN + "/", "logo": DOMAIN + "/assets/img/propodium-icon-512.png",
            "slogan": TAGLINE, "foundingDate": "2009",
            "description": PAGES["home"][1],
            "areaServed": ["United States", "Mexico", "Canada", "Brazil"]}
    return '<script type="application/ld+json">' + json.dumps(data) + '</script>'

def build_site():
    if os.path.exists(SITE): shutil.rmtree(SITE)
    os.makedirs(os.path.join(SITE, "assets", "css")); os.makedirs(os.path.join(SITE, "assets", "js")); os.makedirs(os.path.join(SITE, "assets", "img"))
    shutil.copy(os.path.join(BASE, "style.css"), os.path.join(SITE, "assets", "css", "style.css"))
    open(os.path.join(SITE, "assets", "js", "main.js"), "w").write(JS_COMMON + JS_FORM_SITE)
    open(os.path.join(SITE, "assets", "img", "propodium-logo.svg"), "w").write(logo_light)
    open(os.path.join(SITE, "assets", "img", "propodium-logo-dark-bg.svg"), "w").write(logo_dark)
    open(os.path.join(SITE, "favicon.svg"), "w").write(icon_svg)
    for src, dst in [("icon-32.png", "favicon-32.png"), ("icon-180.png", "apple-touch-icon.png"),
                     ("icon-512.png", "assets/img/propodium-icon-512.png"), ("logo-dark-1200.png", "assets/img/og-image.png")]:
        shutil.copy(os.path.join(IN, src), os.path.join(SITE, dst))
    href = lambda p: "./" if p == "home" else FILES[p]
    for pid, (title, desc) in PAGES.items():
        body = {"home": home, "about": about, "partners": partners}.get(pid)
        main = body(href) if body else contact(href, False)
        url = DOMAIN + "/" + ("" if pid == "home" else FILES[pid])
        html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title.replace("&", "&amp;")}</title>
<meta name="description" content="{desc.replace("&", "&amp;")}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0A1C21">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME_HTML}">
<meta property="og:title" content="{title.replace("&", "&amp;")}">
<meta property="og:description" content="{desc.replace("&", "&amp;")}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/img/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
{jsonld() if pid == "home" else ""}
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>
{header(pid, href)}
<main id="main">
{main}
</main>
{footer(href)}
<script src="assets/js/main.js"></script>
</body>
</html>
'''
        open(os.path.join(SITE, FILES[pid]), "w").write(html)
    open(os.path.join(SITE, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    urls = "".join(f"  <url><loc>{DOMAIN}/{'' if p == 'home' else f}</loc></url>\n" for p, f in FILES.items())
    open(os.path.join(SITE, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    open(os.path.join(SITE, "site.webmanifest"), "w").write(json.dumps({
        "name": NAME, "short_name": "ProPodium", "start_url": "/", "display": "browser",
        "background_color": "#0A1C21", "theme_color": "#0A1C21",
        "icons": [{"src": "/assets/img/propodium-icon-512.png", "sizes": "512x512", "type": "image/png"},
                  {"src": "/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}]}, indent=2))

def build_preview():
    href = lambda p: "#" + p
    css = open(os.path.join(BASE, "style.css")).read()
    fav = "data:image/svg+xml;base64," + base64.b64encode(icon_svg.encode()).decode()
    pages = ""
    for pid in ["home", "about", "partners", "contact"]:
        body = {"home": home, "about": about, "partners": partners}.get(pid)
        main = body(href) if body else contact(href, True)
        pages += f'<div id="page-{pid}" class="page"{" hidden" if pid != "home" else ""}>\n{header(pid, href)}\n<main>\n{main}\n</main>\n{footer(href)}\n</div>\n'
    html = f'''<title>ProPodium Events Site</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{PAGES["home"][1].replace("&", "&amp;")}">
<link rel="icon" href="{fav}">
{FONTS}
<style>
{css}
</style>
{pages}
<script>{JS_COMMON}{JS_FORM_PREVIEW}{JS_ROUTER}</script>
'''
    open(os.path.join(OUT, "preview.html"), "w").write(html)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    build_site(); build_preview()
    print("ok")
