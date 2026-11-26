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

sys.path.insert(0, BASE)
from content import *

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def mail(addr):
    return f'<a href="mailto:{addr}">{addr}</a>'

def media(desc):
    return f'''<figure class="media-ph">
  <div class="media-ph-box" aria-hidden="true"><span class="star"></span></div>
  <figcaption><strong>Photo placeholder.</strong> {esc(desc)}</figcaption>
</figure>'''

# ---------- page registry ----------
# pid -> (file, title, description)
PAGES = {
    "home": ("index.html", "ProPodium Events & Hospitality | The Support Behind Every Great Event",
             "ProPodium Events delivers precision event mobility and B2B operational excellence since 2019: executive and VIP transportation, on-site event coordinators, airport greeters and group transportation."),
    "about": ("about.html", "About | ProPodium Events & Hospitality",
              "Since 2019, ProPodium Events & Hospitality has supported event organizers, sponsors and event-transport companies at Formula 1, the Super Bowl, the FIFA World Cup and more."),
    "services": ("services.html", "Services | ProPodium Events & Hospitality",
                 "Executive & VIP transportation, on-site event coordinators, airport greeters & FBO meet-and-greet, and group transportation & shuttle logistics."),
    "events": ("events.html", "Events | ProPodium Events & Hospitality",
               EVENTS_INTRO),
}
for c in CATS:
    PAGES[c["id"]] = (c["file"], f'{c["headline"]} | ProPodium Events & Hospitality', c["intro"])
PAGES["past"] = ("events/past-events.html", "Past Events & Proven Track Record | ProPodium Events & Hospitality",
                 "Historical productions supported by ProPodium Events across sports, music and culture, business conferences and diplomatic summits.")
PAGES["partners"] = ("partners.html", "Our Partners | ProPodium Events & Hospitality",
                     "ProPodium Events & Hospitality works alongside experienced companies that share its commitment to reliability and guest experience, including Leo Limos in Austin, TX.")
PAGES["contact"] = ("contact.html", "Contact | ProPodium Events & Hospitality",
                    "Contact ProPodium Events & Hospitality for executive transportation, on-site event coordination, airport greeters and group transportation.")
CAT_BY_ID = {c["id"]: c for c in CATS}
EVENT_PIDS = ["events"] + [c["id"] for c in CATS] + ["past"]

# ---------- shared parts ----------
def header(cur, href):
    def a(pid, text, cls=""):
        cur_attr = ' aria-current="page"' if pid == cur else ""
        return f'<a href="{href(pid)}"{cur_attr}{cls}>{text}</a>'
    sub = "".join(f'<li>{a(c["id"], c["menu"])}</li>' for c in CATS)
    sub = f'<li>{a("events", "All events")}</li>' + sub + f'<li>{a("past", "Past events")}</li>'
    ev_cur = ' class="is-current"' if cur in EVENT_PIDS else ""
    return f'''<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="{href("home")}"><span class="sr-only">{NAME_HTML} home</span>{logo_inline}</a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-links-{cur}">Menu</button>
    <ul class="nav-links" id="nav-links-{cur}">
      <li>{a("home", "Home")}</li>
      <li>{a("about", "About")}</li>
      <li>{a("services", "Services")}</li>
      <li class="has-sub"><a href="{href("events")}"{ev_cur}{' aria-current="page"' if cur == "events" else ""}>Events <span class="caret" aria-hidden="true"></span></a><ul class="sub" aria-label="Events">{sub}</ul></li>
      <li>{a("partners", "Partners")}</li>
      <li><a class="btn btn-gold" href="{href("contact")}"{' aria-current="page"' if cur == "contact" else ""}>Request a quote</a></li>
    </ul>
  </div>
</header>'''

def footer(href):
    cats = "".join(f'<li><a href="{href(c["id"])}">{c["menu"]}</a></li>' for c in CATS)
    return f'''<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <a class="brand" href="{href("home")}"><span class="sr-only">{NAME_HTML} home</span>{logo_inline}</a>
      <p><strong class="footer-tag">The Support Behind Every Great Event.</strong> {HERITAGE}</p>
    </div>
    <div>
      <h4>Explore</h4>
      <ul>
        <li><a href="{href("home")}">Home</a></li>
        <li><a href="{href("about")}">About</a></li>
        <li><a href="{href("services")}">Services</a></li>
        <li><a href="{href("partners")}">Partners</a></li>
        <li><a href="{href("contact")}">Contact</a></li>
      </ul>
    </div>
    <div>
      <h4>Events</h4>
      <ul>{cats}<li><a href="{href("past")}">Past events</a></li></ul>
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

def cta(href):
    return f'''<section class="cta">
  <div class="wrap cta-inner">
    <h2>ProPodium. <span class="muted">Professional support, podium-level service.</span></h2>
    <a class="btn btn-ink" href="{href("contact")}">Request a quote</a>
  </div>
</section>'''

def page_hero(eyebrow, title, text, italic=True):
    cls = "" if italic else ' class="plain"'
    return f'''<section class="page-hero"><div class="wrap">
  <span class="eyebrow">{STAR}{eyebrow}</span>
  <h1>{title}</h1>
  <p{cls}>{text}</p>
</div></section>'''

COUNTRIES = [("United States", "USA"), ("Mexico", "MEX"), ("Canada", "CAN"), ("Brazil", "BRA")]
EVENT_TYPES = ["Corporate events", "Conferences", "Concerts", "Motorsport", "Car and motorcycle shows", "Major sporting events"]
AUDIENCES = [("Event organizers", "Every guest is welcomed, moved, and looked after without a detail missed."),
             ("Sponsors", "Executive and VIP transportation, airport greeters, and guest welcome for your guests."),
             ("Event-transport companies", "We don&rsquo;t compete with you. We work alongside you as an extension of your team.")]
PILLARS = [("Experience", "Supporting some of the world&rsquo;s most demanding events since 2019."),
           ("Reliability", "We know what it takes to deliver when the stakes are high."),
           ("Hospitality-first", "Every guest welcomed, moved, and looked after.")]

def services_cards(href):
    return "".join(f'''<a class="service service-link" href="{href("services", s["id"])}">{STAR}<h3>{esc(s["name"])}</h3><p>{esc(s["sub"])}</p><span class="more">Learn more &rarr;</span></a>''' for s in SERVICES)

def category_cards(href):
    out = ""
    for c in CATS:
        evs = "".join(f'<li><a href="{href(c["id"], e["anchor"])}">{esc(e["short"])}</a></li>' for e in c["events"])
        out += f'''<article class="cat-card">
  <span class="cat-menu">{esc(c["menu"])}</span>
  <h3><a href="{href(c["id"])}">{esc(c["headline"])}</a></h3>
  <ul class="cat-events">{evs}</ul>
  <a class="more" href="{href(c["id"])}">See 2027 events &rarr;</a>
</article>'''
    out += f'''<article class="cat-card cat-past">
  <span class="cat-menu">Track record</span>
  <h3><a href="{href("past")}">{PAST_TITLE}</a></h3>
  <p>Historical productions across sports, music and culture, business conferences and diplomatic summits.</p>
  <a class="more" href="{href("past")}">See past events &rarr;</a>
</article>'''
    return out

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

# ---------- pages ----------
def home(href):
    countries = "".join(f'<li>{c}<small>{code}</small></li>' for c, code in COUNTRIES)
    types = "".join(f"<li>{t}</li>" for t in EVENT_TYPES)
    audiences = "".join(f'<article class="service">{STAR}<h3>{t}</h3><p>{d}</p></article>' for t, d in AUDIENCES)
    pillars = "".join(f'<div class="pillar"><span class="num">0{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(PILLARS))
    return f'''<section class="hero">
  <div class="wrap hero-inner">
    <div class="hero-copy">
      <span class="eyebrow">{NAME_HTML}</span>
      <h1>The support behind every <span class="accent">great event.</span></h1>
      <p class="hero-lead">The operational partner behind some of the world&rsquo;s most demanding events. Since 2019, we have supported event organizers, sponsors, and event-transport companies, making sure every guest is welcomed, moved, and looked after without a detail missed.</p>
      <div class="hero-actions">
        <a class="btn btn-gold" href="{href("contact")}">Request a quote</a>
        <a class="btn btn-ghost" href="{href("events")}">See our events</a>
      </div>
    </div>
    <div class="podium" aria-hidden="true">
      <div class="step step-2">2</div>
      <div class="step step-1"><span class="star"></span>1</div>
      <div class="step step-3">3</div>
    </div>
  </div>
  <div class="facts-strip"><div class="wrap facts">
    <span>{STAR}Since 2019</span><span>{STAR}Executive &amp; VIP transportation</span><span>{STAR}On-site coordination</span><span>{STAR}Airport &amp; FBO meet-and-greet</span><span>{STAR}Group shuttle logistics</span>
  </div></div>
</section>

<section class="section tint" id="what-we-do">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{STAR}What we do</span>
      <h2>Every guest welcomed, moved, and looked after.</h2>
    </div>
    <div class="services">{services_cards(href)}</div>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{STAR}Events</span>
      <h2>{EVENTS_HEADLINE}</h2>
      <p>{EVENTS_INTRO}</p>
    </div>
    <div class="cat-grid">{category_cards(href)}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{STAR}Who we support</span>
      <h2>Event organizers, sponsors, and event-transport companies.</h2>
    </div>
    <div class="services three">{audiences}</div>
  </div>
</section>

<section class="section tint">
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

<section class="section">
  <div class="wrap approach">
    <div class="section-head" style="margin:0"><span class="eyebrow">{STAR}Our approach</span><h2>An extension of your team.</h2></div>
    <blockquote>We don&rsquo;t compete with the companies we support. We work alongside them as an extension of their team, bringing <span class="hl">experience, reliability, and a hospitality-first mindset</span> to every event.</blockquote>
  </div>
  <div class="wrap"><div class="pillars">{pillars}</div></div>
</section>

<section class="section tint">
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

def about(href):
    svc = "".join(f'<li>{STAR}<span><a href="{href("services", s["id"])}">{esc(s["name"])}</a></span></li>' for s in SERVICES)
    return f'''{page_hero("About us", f"About {NAME_HTML}", HERITAGE)}
<section class="section"><div class="wrap about-grid">
  <div class="prose">
    <p class="lead">{NAME_HTML} is the operational partner behind some of the world&rsquo;s most demanding events. Since 2019, we have supported event organizers, sponsors, and event-transport companies, making sure every guest is welcomed, moved, and looked after without a detail missed.</p>
    <p>From Formula 1 in Austin, Miami, and Las Vegas to the Super Bowl, NBA All-Star Game, PGA, Kentucky Derby, SXSW, and the FIFA World Cup, we know what it takes to deliver when the stakes are high.</p>
    <h2>What we do</h2>
    <ul>{svc}</ul>
    <h2>Where we work</h2>
    <p>Across the United States, Mexico, Canada, and Brazil, for corporate events, conferences, concerts, motorsport, car and motorcycle shows, and major sporting events.</p>
    <h2>Our approach</h2>
    <p>We don&rsquo;t compete with the companies we support. We work alongside them as an extension of their team, bringing experience, reliability, and a hospitality-first mindset to every event.</p>
    <p class="signoff">ProPodium Events. The Support Behind Every Great Event.</p>
  </div>
  <aside class="aside" aria-label="At a glance">
    <dl>
      <div><dt>Supporting events since</dt><dd>2019</dd></div>
      <div><dt>Countries</dt><dd>United States, Mexico, Canada, Brazil</dd></div>
      <div><dt>We support</dt><dd>Event organizers, sponsors, and event-transport companies</dd></div>
    </dl>
    <a class="btn btn-ink" href="{href("contact")}">Request a quote</a>
  </aside>
</div></section>
{cta(href)}'''

def services(href):
    jump = "".join(f'<li><a href="{href("services", s["id"])}">{esc(s["name"])}</a></li>' for s in SERVICES)
    blocks = ""
    for i, s in enumerate(SERVICES):
        feats = "".join(f"<li>{STAR}<span>{esc(f)}</span></li>" for f in s["features"])
        blocks += f'''<section class="section svc-block{' tint' if i % 2 == 0 else ''}" id="{s["id"]}">
  <div class="wrap svc-grid{' flip' if i % 2 else ''}">
    <div class="svc-copy">
      <span class="eyebrow">{STAR}{esc(s["name"])}</span>
      <h2>{esc(s["headline"])}</h2>
      <p class="svc-sub">{esc(s["sub"])}</p>
      <p>{esc(s["body"])}</p>
      <h3 class="feat-title">Key features</h3>
      <ul class="features">{feats}</ul>
    </div>
    {media(s["media"])}
  </div>
</section>'''
    return f'''{page_hero("Services", "Our Services", HERITAGE)}
<nav class="jump" aria-label="Services on this page"><div class="wrap"><ul>{jump}</ul></div></nav>
{blocks}
{cta(href)}'''

def events(href):
    return f'''{page_hero("Events", EVENTS_HEADLINE, EVENTS_INTRO, italic=False)}
<section class="section tint"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{STAR}2027 event deployments</span><h2>Explore by category</h2></div>
  <div class="cat-grid light">{category_cards(href)}</div>
</div></section>
{cta(href)}'''

def event_block(e):
    spot = ""
    if e["spot_label"]:
        body = (f'<ul>{"".join(f"<li>{esc(x)}</li>" for x in e["spot"])}</ul>' if isinstance(e["spot"], list)
                else f'<p>{esc(e["spot"])}</p>')
        spot = f'<div class="spotlight"><h3>{STAR}{esc(e["spot_label"])}</h3>{body}</div>'
    rows = "".join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in e["details"])
    label = "Event contacts" if len(e["contacts"]) > 1 else "Event contact"
    contacts = " ".join(mail(c) for c in e["contacts"])
    rows += f'<div><dt>{label}</dt><dd>{contacts}</dd></div>'
    med = media(e["media"]) if e["media"] else ""
    return f'''<article class="event-block" id="{e["anchor"]}">
  <h2>{esc(e["title"])}</h2>
  <div class="event-grid">
    <div class="event-copy">
      <p><strong>Overview.</strong> {esc(e["overview"])}</p>
      {spot}
      {med}
    </div>
    <aside class="details">
      <h3>{esc(e["details_title"])}</h3>
      <dl>{rows}</dl>
    </aside>
  </div>
</article>'''

def category(cid):
    c = CAT_BY_ID[cid]
    def body(href):
        svcs = "".join(f'<li><a href="{href("services", SVC[n])}">{STAR}{esc(n)}</a></li>' for n in c["services"])
        jump = "".join(f'<li><a href="{href(cid, e["anchor"])}">{esc(e["short"])}</a></li>' for e in c["events"])
        others = "".join(f'<li><a href="{href(o["id"])}">{esc(o["menu"])}</a></li>' for o in CATS if o["id"] != cid)
        evs = "".join(event_block(e) for e in c["events"])
        return f'''{page_hero("Events &middot; " + esc(c["menu"]), esc(c["headline"]), esc(c["intro"]), italic=False)}
<nav class="jump" aria-label="Events on this page"><div class="wrap"><ul>{jump}</ul></div></nav>
<section class="section tint svc-strip"><div class="wrap">
  <h2 class="strip-title">Our Services on This Page</h2>
  <ul class="svc-chips">{svcs}</ul>
</div></section>
<section class="section events-list"><div class="wrap">{evs}</div></section>
<section class="cta cat-cta">
  <div class="wrap cta-inner">
    <div><h2>{esc(c["cta"])}</h2><p class="cta-contact">Contact: {mail(CTA_EMAIL)}</p></div>
    <a class="btn btn-ink" href="{href("contact")}">Request a quote</a>
  </div>
</section>
<nav class="section other-cats" aria-label="Other event categories"><div class="wrap">
  <span class="eyebrow">{STAR}More events</span>
  <ul class="chips">{others}<li><a href="{href("past")}">Past events</a></li></ul>
</div></nav>'''
    return body

def past(href):
    head = "".join(f'<th scope="col">{esc(h)}</th>' for h in PAST_COLS)
    rows = ""
    for cat, flag, scope, high, contacts in PAST_ROWS:
        cs = "".join(f'<li>{mail(p + "@propodiumevents.com")}</li>' for p in contacts)
        rows += f'''<tr>
  <th scope="row" data-label="{esc(PAST_COLS[0])}">{esc(cat)}</th>
  <td data-label="{esc(PAST_COLS[1])}">{esc(flag)}</td>
  <td data-label="{esc(PAST_COLS[2])}">{esc(scope)}</td>
  <td data-label="{esc(PAST_COLS[3])}">{esc(high)}</td>
  <td data-label="Event contacts"><ul class="contact-list">{cs}</ul></td>
</tr>'''
    return f'''{page_hero("Events &middot; Track record", PAST_TITLE, EVENTS_INTRO, italic=False)}
<section class="section"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{STAR}Historical productions</span><h2>{PAST_SUB}</h2></div>
  <div class="matrix-wrap"><table class="matrix">
    <thead><tr>{head}</tr></thead>
    <tbody>{rows}</tbody>
  </table></div>
</div></section>
{cta(href)}'''

def partners(href):
    return f'''{page_hero("Partners", "Our Partners", "The support behind every great event is built on trusted relationships.")}
<section class="section tint"><div class="wrap">
  <div class="section-head"><p style="color:var(--ink);font-size:1.15rem">At {NAME_HTML}, we work alongside experienced companies that share our commitment to reliability and guest experience. Our partners help us deliver seamless events across the United States and beyond.</p></div>
  {partner_card()}
  <div class="partner-soon">{STAR}More partners coming soon.</div>
</div></section>
{cta(href)}'''

def contact(href, preview):
    checks = "".join(f'<label><input type="checkbox" name="services" value="{esc(s["name"])}" id="svc-{i}"> {esc(s["name"])}</label>' for i, s in enumerate(SERVICES))
    note = ("This is a preview: the form does not send messages yet." if preview
            else "Sending opens your email app with the details filled in.")
    return f'''{page_hero("Contact", "Request a quote for your event", "The Support Behind Every Great Event.")}
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

BODIES = {"home": home, "about": about, "services": services, "events": events, "past": past, "partners": partners}
for _c in CATS:
    BODIES[_c["id"]] = category(_c["id"])

def body_for(pid, href, preview):
    return contact(href, preview) if pid == "contact" else BODIES[pid](href)

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

def js_router():
    return r'''
(function () {
  var ids = ''' + json.dumps(list(PAGES.keys())) + r''';
  function show() {
    var parts = (location.hash || '#home').slice(1).split('/');
    var id = parts[0], anchor = parts[1];
    if (ids.indexOf(id) < 0) id = 'home';
    ids.forEach(function (p) { document.getElementById('page-' + p).hidden = (p !== id); });
    document.querySelectorAll('.nav-links.open').forEach(function (l) { l.classList.remove('open'); });
    var el = anchor && document.getElementById(anchor);
    if (el) el.scrollIntoView(); else window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', show);
  show();
})();
'''

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:ital,wght@0,500;0,600;0,700;0,800;1,600;1,700&display=swap">'

def jsonld():
    data = {"@context": "https://schema.org", "@type": "Organization", "name": NAME,
            "url": DOMAIN + "/", "logo": DOMAIN + "/assets/img/propodium-icon-512.png",
            "slogan": "The Support Behind Every Great Event.", "foundingDate": "2019",
            "description": PAGES["home"][2]}
    return '<script type="application/ld+json">' + json.dumps(data) + '</script>'

def site_href(depth, cur=None):
    pre = "../" * depth
    def href(pid, anchor=None):
        if pid == cur and anchor:
            return "#" + anchor
        f = PAGES[pid][0]
        url = (pre or "./") if f == "index.html" else pre + f
        return url + ("#" + anchor if anchor else "")
    return href

def a(s): return s.replace("&", "&amp;")

def build_site():
    if os.path.exists(SITE): shutil.rmtree(SITE)
    for d in ["assets/css", "assets/js", "assets/img", "events"]:
        os.makedirs(os.path.join(SITE, d))
    shutil.copy(os.path.join(BASE, "style.css"), os.path.join(SITE, "assets", "css", "style.css"))
    open(os.path.join(SITE, "assets", "js", "main.js"), "w").write(JS_COMMON + JS_FORM_SITE)
    open(os.path.join(SITE, "assets", "img", "propodium-logo.svg"), "w").write(logo_light)
    open(os.path.join(SITE, "assets", "img", "propodium-logo-dark-bg.svg"), "w").write(logo_dark)
    open(os.path.join(SITE, "favicon.svg"), "w").write(icon_svg)
    for src, dst in [("icon-32.png", "favicon-32.png"), ("icon-180.png", "apple-touch-icon.png"),
                     ("icon-512.png", "assets/img/propodium-icon-512.png"), ("logo-dark-1200.png", "assets/img/og-image.png")]:
        shutil.copy(os.path.join(IN, src), os.path.join(SITE, dst))
    for pid, (f, title, desc) in PAGES.items():
        depth = f.count("/")
        pre = "../" * depth
        href = site_href(depth, pid)
        url = DOMAIN + "/" + ("" if f == "index.html" else f)
        html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{a(title)}</title>
<meta name="description" content="{a(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0A1C21">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME_HTML}">
<meta property="og:title" content="{a(title)}">
<meta property="og:description" content="{a(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/img/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{pre}favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">
<link rel="manifest" href="{pre}site.webmanifest">
{FONTS}
<link rel="stylesheet" href="{pre}assets/css/style.css">
{jsonld() if pid == "home" else ""}
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>
{header(pid, href)}
<main id="main">
{body_for(pid, href, False)}
</main>
{footer(href)}
<script src="{pre}assets/js/main.js"></script>
</body>
</html>
'''
        open(os.path.join(SITE, f), "w").write(html)
    open(os.path.join(SITE, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    urls = "".join(f"  <url><loc>{DOMAIN}/{'' if v[0] == 'index.html' else v[0]}</loc></url>\n" for v in PAGES.values())
    open(os.path.join(SITE, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    open(os.path.join(SITE, "site.webmanifest"), "w").write(json.dumps({
        "name": NAME, "short_name": "ProPodium", "start_url": "/", "display": "browser",
        "background_color": "#0A1C21", "theme_color": "#0A1C21",
        "icons": [{"src": "/assets/img/propodium-icon-512.png", "sizes": "512x512", "type": "image/png"},
                  {"src": "/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}]}, indent=2))

def build_preview():
    href = lambda p, anchor=None: "#" + p + ("/" + anchor if anchor else "")
    css = open(os.path.join(BASE, "style.css")).read()
    fav = "data:image/svg+xml;base64," + base64.b64encode(icon_svg.encode()).decode()
    pages = ""
    for pid in PAGES:
        pages += f'<div id="page-{pid}" class="page"{" hidden" if pid != "home" else ""}>\n{header(pid, href)}\n<main>\n{body_for(pid, href, True)}\n</main>\n{footer(href)}\n</div>\n'
    html = f'''<title>ProPodium Events Site</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{a(PAGES["home"][2])}">
<link rel="icon" href="{fav}">
{FONTS}
<style>
{css}
</style>
{pages}
<script>{JS_COMMON}{JS_FORM_PREVIEW}{js_router()}</script>
'''
    open(os.path.join(OUT, "preview.html"), "w").write(html)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    build_site(); build_preview()
    print("ok")
