# All copy below comes from Denis's "Pro Podium Events - Website Copy Updates" PDF (Nov 26, 2026).
HERITAGE = "Delivering precision event mobility and B2B operational excellence since 2019."
TAGLINE_FULL = "Pro Podium Events — The Support Behind Every Great Event."

SERVICES = [
  dict(id="executive-vip", name="Executive & VIP Transportation",
       headline="Discreet, Precision Mobility for Principals, Talent, and C-Suite Leaders",
       sub="Seamless point-to-point and dedicated charter logistics engineered for high-profile schedules.",
       body="When timelines are non-negotiable and privacy is paramount, Pro Podium Events delivers white-glove ground transportation tailored to executives, dignitaries, artists, and VIP guests. Operating with late-model luxury sedans, flagship SUVs, and executive Sprinters, our vetted chauffeurs are trained in defensive driving, diplomatic protocol, and strict NDA compliance. Every vehicle is staged ahead of schedule and monitored in real time by our central dispatch command.",
       features=["Late-model black-on-black fleet", "Chauffeurs in formal business attire", "Real-time GPS & flight tracking", "NDA-compliant discretion"],
       media="Black luxury SUV staged outside a private jet terminal or five-star hotel at dusk."),
  dict(id="on-site-coordinators", name="On-Site Event Coordinators",
       headline="Boots-on-the-Ground Command for Complex Event Logistics",
       sub="Dedicated transportation directors bridging the gap between venue operations, security, and fleet dispatch.",
       body="Even the best fleet fails without disciplined curb management. Our On-Site Event Coordinators embed directly into your production team to manage load-in/load-out zones, credentialed access, staging lots, and last-minute manifest changes. From multi-hotel corporate summits to restricted stadium perimeters, we serve as the single point of accountability on the tarmac and at the venue gates.",
       features=["Dedicated curb and staging management", "Direct liaison with venue security and police", "Live manifest adjustments", "Unified communication with dispatch"],
       media="Event coordinator with a headset and tablet managing vehicle staging outside a major convention center or arena."),
  dict(id="airport-greeters", name="Airport Greeters & FBO Meet-and-Greet",
       headline="First-Class Arrival & Departure Management at Commercial Terminals and Private FBOs",
       sub="Eliminating airport friction from tarmac to vehicle.",
       body="Your guest’s event experience begins the moment they land. Pro Podium Events deploys uniformed Airport Greeters across commercial baggage claims, international customs exits, and private FBO terminals. We track incoming tails and commercial flights to the minute, coordinate luggage handling, and escort principals directly to their waiting vehicles—ensuring zero wait times and effortless transitions.",
       features=["Custom digital or branded signage", "Commercial terminal & private FBO coverage", "Real-time flight & tail-number monitoring", "Luggage porter coordination"],
       media="Uniformed greeter holding a tablet or welcome sign inside a modern airport terminal or private FBO lounge."),
  dict(id="group-transportation", name="Group Transportation & Shuttle Logistics",
       headline="Scalable, Synchronized Movement for Delegations, Crews, and Corporate Groups",
       sub="High-capacity fleet solutions designed for efficiency, punctuality, and route optimization.",
       body="Moving 50 or 5,000 attendees requires engineered routing and disciplined timing. Pro Podium Events designs and executes custom shuttle loops, hotel-to-venue transfers, and off-site dinner movements using executive Sprinters, mini-coaches, and full-size motorcoaches. We analyze traffic patterns, road closures, and venue drop-off restrictions to keep your program running strictly on schedule.",
       features=["Custom route planning & traffic mitigation", "Sprinter vans, mini-coaches & motorcoaches", "Scheduled shuttle loops & manifests", "Dedicated group dispatchers"],
       media="Lined-up fleet of luxury black Sprinter vans and executive coaches ready for group departure."),
]
SVC = {s["name"]: s["id"] for s in SERVICES}

EVENTS_HEADLINE = "Proven Execution Across the World’s Most Demanding Stages"
EVENTS_INTRO = "Since 2019, Pro Podium Events has operated behind the scenes of global motorsports, championship tournaments, premier music festivals, and high-level international summits. Explore our active event deployments."

def E(title, short, overview, spot_label=None, spot=None, media=None, details=None, contacts=None, details_title="2027 Event Details", anchor=None):
    return dict(title=title, short=short, overview=overview, spot_label=spot_label, spot=spot, media=media,
                details=details or [], contacts=contacts or [], details_title=details_title, anchor=anchor)

F1_NOTE = ("Notes", "Official F1 2027 calendar (24 races)")
CATS = [
 dict(id="ev-motorsport", file="events/motorsport.html", menu="Motorsport", headline="Motorsport Event Support",
  intro="Race weekends bring highway congestion, road closures, credentialed paddock access and surges of private jet arrivals. Pro Podium Events supports teams, hospitality companies, agencies, broadcasters and VIP hospitality programs across Formula 1 and NASCAR, so every guest moves between airport, hotel and paddock on schedule.",
  services=["Executive & VIP Transportation", "On-Site Event Coordinators", "Airport Greeters & FBO Meet-and-Greet", "Group Transportation & Shuttle Logistics"],
  events=[
   E("Formula 1 — United States Grand Prix (Austin, TX)", "F1 Austin",
     "Hosted at Circuit of The Americas (COTA), Austin’s F1 weekend demands mastery over severe highway congestion, credentialed paddock access, and private FBO surges at Austin-Bergstrom (AUS). Pro Podium Events manages VIP hospitality transfers, team logistics, and downtown hotel staging throughout race week.",
     "Race Champions Spotlight (Austin)", ["Most Wins (COTA): Lewis Hamilton (5 wins)", "Recent Circuit Winners: Max Verstappen, Charles Leclerc, Carlos Sainz, Valtteri Bottas"],
     "Aerial or trackside photo of Circuit of The Americas in Austin during race weekend.",
     [("Dates", "October 22–24, 2027"), ("Location", "Austin, TX — Circuit of The Americas (COTA)"), F1_NOTE], ["f1austin@propodiumevents.com"], anchor="f1-austin"),
   E("Formula 1 — Miami Grand Prix (Miami Gardens, FL)", "F1 Miami",
     "Set around the Miami International Autodrome at Hard Rock Stadium, the Miami GP blends high-security VIP movements, South Beach hospitality shuttles, and multi-airport arrivals (MIA, FLL, OPF). Our team coordinates tight police-escorted windows and luxury fleet staging across Miami-Dade and Broward counties.",
     "Race Champions Spotlight (Miami)", ["Recent Circuit Winners: Max Verstappen, Lando Norris, Oscar Piastri"],
     "Photo of the Miami Grand Prix circuit with palm trees and hospitality suites.",
     [("Dates", "April 30 – May 2, 2027"), ("Location", "Miami, FL"), F1_NOTE], ["f1miami@propodiumevents.com"], anchor="f1-miami"),
   E("Formula 1 — Canadian Grand Prix (Montreal, Canada)", "F1 Montreal",
     "Held at Circuit Gilles Villeneuve on Île Notre-Dame, the Canadian Grand Prix turns downtown Montreal into a race-week festival, with bridge and island access restrictions, packed Old Montreal and downtown hotels, and private jet arrivals at Montréal–Trudeau (YUL). Pro Podium Events provides bilingual (English/French) on-site coordinators, VIP hospitality transfers, and executive fleet staging between the airport, downtown hotels, and the circuit.",
     "Race Champions Spotlight (Montreal)", ["Most Wins: Lewis Hamilton and Michael Schumacher (7 wins each)", "Recent Circuit Winners: Max Verstappen, George Russell"],
     "Photo of Circuit Gilles Villeneuve on Île Notre-Dame with the Montreal skyline in the background.",
     [("Dates", "May 21–23, 2027 (Sprint weekend)"), ("Location", "Montreal, Canada — Circuit Gilles Villeneuve"), ("Notes", "Official F1 2027 calendar (round 7)")], ["f1montreal@propodiumevents.com"], anchor="f1-montreal"),
   E("Formula 1 — Las Vegas Grand Prix (Las Vegas, NV)", "F1 Las Vegas",
     "Racing down the iconic Las Vegas Strip at night creates unprecedented road closures and security perimeters. Pro Podium Events specializes in navigating Strip barricade protocols, private jet arrivals at Harry Reid (LAS) and Henderson, and 24-hour VIP nightlife and paddock transfers.",
     "Race Champions Spotlight (Las Vegas)", ["Recent Circuit Winners: Max Verstappen, George Russell"],
     "Nighttime photo of the Las Vegas Strip illuminated with F1 track barriers and luxury hospitality.",
     [("Dates", "November 18–20, 2027"), ("Location", "Las Vegas, NV"), F1_NOTE], ["f1lasvegas@propodiumevents.com"], anchor="f1-las-vegas"),
   E("Formula 1 — Mexico City Grand Prix (Mexico City, Mexico)", "F1 Mexico City",
     "At Autódromo Hermanos Rodríguez, high-volume VIP attendance and strict metropolitan security protocols require bilingual on-site coordinators and armored or executive fleet options. We manage seamless transfers between Polanco, Reforma, AICM/Toluca airports, and the circuit.",
     "Race Champions Spotlight (Mexico City)", ["Most Wins (Modern Era): Max Verstappen (5 wins)", "Recent Circuit Winners: Carlos Sainz, Max Verstappen, Lewis Hamilton"],
     "Photo of the Foro Sol stadium section at Autódromo Hermanos Rodríguez packed with fans.",
     [("Dates", "October 29–31, 2027"), ("Location", "Mexico City, Mexico"), F1_NOTE], ["f1mexico@propodiumevents.com"], anchor="f1-mexico-city"),
   E("Formula 1 — São Paulo Grand Prix (Interlagos, Brazil)", "F1 São Paulo",
     "Autódromo José Carlos Pace (Interlagos) presents one of the most dynamic logistical environments in global motorsport. Our local ground command manages executive transfers, security-vetted chauffeurs, and helipad/airport connections across Congonhas (CGH), Guarulhos (GRU), and Catarina Executive Airport.",
     "Race Champions Spotlight (Interlagos)", ["Most Wins: Alain Prost (6 wins)", "Recent Circuit Winners: Max Verstappen, George Russell, Lewis Hamilton"],
     "Photo of the Interlagos Senna S curve during a race weekend.",
     [("Dates", "November 5–7, 2027 (Sprint weekend)"), ("Location", "São Paulo, Brazil"), F1_NOTE], ["f1saopaulo@propodiumevents.com"], anchor="f1-sao-paulo"),
   E("NASCAR Cup Series & Major Race Weekends", "NASCAR",
     "From Daytona and Charlotte to Circuit of The Americas (EchoPark Automotive Grand Prix) and Phoenix, Pro Podium Events supports team owners, hospitality companies and agencies, broadcasters, and VIP hospitality suites with high-volume shuttle loops and executive tarmac transfers.",
     "Championship & Marquee Race Winners Spotlight", ["Recent Cup Series Champions: Joey Logano, Ryan Blaney, Kyle Larson, Chase Elliott"],
     "Photo of NASCAR stock cars drafting on a superspeedway or road course.",
     [("Daytona 500", "February 21, 2027 (The Clash: February 13) — Daytona Beach, FL. Season opener of the NASCAR Cup Series"),
      ("COTA", "March 7, 2027 — Austin, TX"),
      ("Las Vegas", "March 21 and October 10, 2027 — Las Vegas Motor Speedway (two races)"),
      ("All-Star Race", "May 23, 2027 — North Wilkesboro, NC"),
      ("Championship Race", "November 14, 2027 — Homestead (Miami), FL. Season finale"),
      ("Charlotte & Phoenix", "TBC (not in the 2027 list)")], ["nascar@propodiumevents.com"], anchor="nascar"),
  ],
  cta="Planning a 2027 race weekend? Tell us your race, your guests and your schedule, and we will plan the ground transportation around it."),

 dict(id="ev-sports", file="events/sports.html", menu="Sports", headline="Major Sporting Events",
  intro="Championship games, World Cup football, golf majors and the biggest days in racing draw corporate hospitality programs, talent and VIP guests from around the world. Pro Podium Events delivers the arrivals, venue transfers and on-site coordination that keep game day running on time.",
  services=["Executive & VIP Transportation", "Airport Greeters & FBO Meet-and-Greet", "On-Site Event Coordinators", "Group Transportation & Shuttle Logistics"],
  events=[
   E("Super Bowl LXI (2027 — SoFi Stadium, Inglewood / Los Angeles, CA)", "Super Bowl LXI",
     "Preparing for Super Bowl LXI in Greater Los Angeles requires multi-county fleet orchestration across LAX, Van Nuys (VNY), Burbank (BUR), Beverly Hills, Downtown LA, and Inglewood. Pro Podium Events provides dedicated brand-activation fleets, red-carpet talent logistics, and 24/7 on-site dispatchers for event agencies, media networks, and corporate hospitality groups.",
     "Championship Spotlight", ["Super Bowl LX Champion (2026): Seattle Seahawks", "Super Bowl LIX Champion (2025): Philadelphia Eagles", "Super Bowl LVIII Champion (2024): Kansas City Chiefs"],
     "Wide exterior photo of SoFi Stadium in Inglewood at twilight.",
     [("Date", "February 14, 2027"), ("Location", "Inglewood (Los Angeles), CA — SoFi Stadium"), ("Notes", "~70,000 in the stadium; the biggest sporting event in the US")], ["superbowl@propodiumevents.com"], anchor="super-bowl"),
   E("FIFA Men's World Cup", "FIFA World Cup",
     "The world's biggest single-sport event brings national team delegations, federation officials, broadcasters, and VIP guests to several host cities at once. Pro Podium Events supports delegations, hospitality companies, and agencies with airport meet-and-greet, executive transfers, and match-day stadium staging across host cities.",
     "Championship Spotlight", ["World Cup 2026 Champion: Spain (1–0 after extra time vs. Argentina, final at New York New Jersey Stadium, July 19, 2026)"],
     "Wide photo of a packed international football stadium at night with executive vehicles staged outside.",
     [("Last edition", "June 11 – July 19, 2026 — Canada, Mexico and the United States (16 stadiums, 48 teams, 104 matches)"),
      ("Next edition", "2030 — Spain, Portugal and Morocco, with centenary matches in Uruguay, Argentina and Paraguay"),
      ("2030 dates", "Centenary matches June 8–9, opening matches June 13–14, final expected July 21, 2030 (proposed schedule, not yet confirmed by FIFA)")],
     ["fifa@propodiumevents.com"], details_title="Event Details (2026 and 2030 Editions)", anchor="fifa-world-cup"),
   E("FIFA Women's World Cup (Brazil 2027)", "FIFA Women's World Cup",
     "Brazil hosts the 2027 FIFA Women's World Cup across eight host cities, with the opening match and the final at the Maracanã in Rio de Janeiro. Pro Podium Events coordinates team delegation, hospitality group, and VIP movements with bilingual on-site coordinators, airport meet-and-greet, and executive transfers between host cities.",
     None, None, "Executive vehicles staged near a large stadium in Rio de Janeiro at sunset.",
     [("Dates", "June 24 – July 25, 2027"), ("Host cities", "Belo Horizonte, Brasília, Fortaleza, Porto Alegre, Recife, Rio de Janeiro, Salvador, São Paulo (Brazil)"),
      ("Opening match & final", "Rio de Janeiro — Estádio do Maracanã (Brazil play the opening match on June 24)"), ("Notes", "64 matches across eight host cities")],
     ["fifawomen@propodiumevents.com"], anchor="fifa-womens-world-cup"),
   E("NBA All-Star Weekend", "NBA All-Star",
     "Executed multi-day VIP mobility for league partners, athletes, and entertainment talent across host arenas, convention centers, and private after-hours venues with tight security perimeters.",
     "All-Star Game MVP / Winning Team Highlights", "Stephen Curry, Damian Lillard, Jayson Tatum, Giannis Antetokounmpo.", None,
     [("Dates", "February 19–21, 2027"), ("Location", "Phoenix, AZ")], ["nbaallstar@propodiumevents.com"], anchor="nba-all-star"),
   E("PGA Tour & Major Golf Championships", "PGA Tour",
     "Provided tournament-long logistics across the PGA circuit—including player courtesy-car coordination, corporate hospitality shuttles, and private FBO transfers at premier championship courses nationwide.",
     "Tournament Champions Highlights", "Scottie Scheffler, Xander Schauffele, Rory McIlroy, Jon Rahm.", None,
     [("The Masters", "April 8–11, 2027 — Augusta, GA"), ("PGA Championship", "May 17–23, 2027 — Frisco, TX (Fields Ranch East, PGA Frisco, near Dallas)"), ("U.S. Open", "June 17–20, 2027 — Pebble Beach, CA")],
     ["pga@propodiumevents.com"], anchor="pga"),
   E("The Kentucky Derby (Churchill Downs — Louisville, KY)", "Kentucky Derby",
     "Managed peak-demand Derby Week operations in Louisville, coordinating private aviation arrivals at SDF and Bowman Field, Millionaires Row VIP drop-offs, and formal gala transfers.",
     "Recent Kentucky Derby Winners", "Sovereignty (2025), Mystik Dan (2024), Mage (2023), Rich Strike (2022).", None,
     [("Date", "May 1, 2027 — 153rd Kentucky Derby (Kentucky Oaks: April 30)"), ("Location", "Louisville, KY — Churchill Downs")], ["kentuckyderby@propodiumevents.com"], anchor="kentucky-derby"),
  ],
  cta="Hosting guests at a 2027 championship? Contact us to plan arrivals, venue transfers and game-day staging."),

 dict(id="ev-festivals", file="events/festivals.html", menu="Festivals & Entertainment", headline="Festivals, Film & Culture",
  intro="Festivals, film premieres and award nights mean street closures, red-carpet timing and artists who cannot wait. Pro Podium Events moves talent, executives and VIP guests between airports, hotels, venues and after-parties with discretion and precision.",
  services=["Executive & VIP Transportation", "On-Site Event Coordinators", "Airport Greeters & FBO Meet-and-Greet", "Group Transportation & Shuttle Logistics"],
  events=[
   E("South by Southwest (SXSW — Austin, TX)", "SXSW",
     "Headquartered in Austin, Pro Podium Events navigates downtown street closures, keynote speaker schedules, brand houses, and private showcase transfers across the Austin Convention Center and entertainment districts.",
     None, None, None, [("Dates", "March 13–21, 2027 (main conference March 15–21)"), ("Location", "Austin, TX")], ["sxsw@propodiumevents.com"], anchor="sxsw"),
   E("Austin City Limits Music Festival (ACL Fest — Zilker Park, Austin, TX)", "ACL Fest",
     "Headquartered in Austin, Pro Podium Events moves artists, VIP guests, and corporate hospitality groups between Austin-Bergstrom (AUS), downtown hotels, and the Zilker Park artist and VIP entrances, working around festival road closures across both weekends.",
     None, None, "Executive Sprinter staged near Zilker Park with the Austin skyline at sunset.",
     [("Dates", "Two weekends in October 2027 (TBC)"), ("Location", "Austin, TX — Zilker Park"), ("Notes", "2027 dates not yet announced on the official festival site; the 2026 edition was October 2–4 and October 9–11")],
     ["acl@propodiumevents.com"], anchor="acl-fest"),
   E("The Oscars (Academy Awards — Los Angeles, CA)", "The Oscars",
     "Pro Podium Events manages white-glove executive transportation, nominee arrivals, and studio executive departures around Hollywood's tightest red-carpet security zones and private after-parties.",
     None, None, "Luxury sedan staged near a red carpet arrival portal at night.",
     [("Date", "March 14, 2027 — 99th Academy Awards"), ("Location", "Los Angeles, CA — Dolby Theatre")], ["oscars@propodiumevents.com"], anchor="oscars"),
   E("Coachella Valley Music and Arts Festival (Indio / Palm Springs, CA)", "Coachella",
     "Executed dedicated artist compound shuttles, headline act transfers, and brand hospitality fleets connecting Palm Springs FBOs (PSP, TRM) directly to the Empire Polo Club.",
     None, None, "Executive Sprinter staged near desert festival grounds at sunset.",
     [("Dates", "April 9–11 and April 16–18, 2027 (two weekends)"), ("Location", "Indio, CA")], ["coachella@propodiumevents.com"], anchor="coachella"),
   E("Cannes Film Festival (Cannes, France)", "Cannes Film Festival",
     "Synchronized French Riviera VIP ground logistics, managing continuous transfers between Nice Côte d'Azur Airport (NCE), luxury Croisette hotels, and red-carpet premieres at Palais des Festivals.",
     None, None, "Black executive sedans lined up along Boulevard de la Croisette in Cannes.",
     [("Dates", "May 11–22, 2027 — 80th edition (anniversary edition)"), ("Location", "Cannes, France")], ["cannes@propodiumevents.com"], anchor="cannes"),
   E("Lollapalooza USA (Grant Park — Chicago, IL)", "Lollapalooza USA",
     "Coordinated high-density downtown Chicago transfers between O’Hare/Midway, Magnificent Mile hotels, and Grant Park artist/VIP entrances.",
     None, None, None, [("Dates", "Late July / early August 2027 (TBC)"), ("Location", "Chicago, IL — Grant Park"), ("Notes", "2027 dates not yet announced")], ["lollapalooza@propodiumevents.com"], anchor="lollapalooza-usa"),
   E("Lollapalooza Brazil (Autódromo de Interlagos — São Paulo, Brazil)", "Lollapalooza Brazil",
     "Managed large-scale festival mobility, artist transport, and corporate hospitality shuttles in São Paulo with bilingual on-site coordinators.",
     None, None, None, [("Dates", "March 19–21, 2027"), ("Location", "São Paulo, Brazil"), ("Notes", "2027 venue TBC (usually Autódromo de Interlagos)")], ["lollapaloozabrazil@propodiumevents.com"], anchor="lollapalooza-brazil"),
   E("Monaco Yacht Show (Port Hercule, Monaco)", "Monaco Yacht Show",
     "Provided high-security transfers for superyacht owners, charter guests, and corporate hospitality guests across Monaco, Nice FBOs, and Monaco Heliport, coordinating tight harbor perimeter access.",
     None, None, "Luxury chauffeur vehicle overlooking Port Hercule filled with superyachts.",
     [("Dates", "September 22–25, 2027"), ("Location", "Monte Carlo, Monaco — Port Hercule")], ["monacoyachtshow@propodiumevents.com"], anchor="monaco-yacht-show"),
  ],
  cta="Bringing artists, talent or VIP guests to a 2027 festival or premiere? Contact us to plan every transfer."),

 dict(id="ev-business", file="events/business.html", menu="Business & Conferences", headline="Corporate Conferences & Trade Shows",
  intro="Global conferences and trade shows move thousands of executives, speakers and delegates on tight schedules. Pro Podium Events runs C-suite transfers, delegate shuttles and airport meet-and-greet so your people arrive ready for the keynote.",
  services=["Group Transportation & Shuttle Logistics", "Executive & VIP Transportation", "Airport Greeters & FBO Meet-and-Greet", "On-Site Event Coordinators"],
  events=[
   E("CES (Consumer Electronics Show — Las Vegas, NV)", "CES",
     "Executed large-scale C-suite shuttles, keynote speaker movements, and booth staff transportation connecting Harry Reid Airport, LVCC, Venetian Expo, and Strip resorts during peak show hours.",
     None, None, "Executive shuttles staged outside the Las Vegas Convention Center.",
     [("Dates", "January 6–9, 2027"), ("Location", "Las Vegas, NV"), ("Notes", "~148,000 attendees (2026)")], ["ces@propodiumevents.com"], anchor="ces"),
   E("World Economic Forum (Davos, Switzerland)", "World Economic Forum",
     "Coordinated all-weather executive ground mobility, armored transfer logistics, and Zurich Airport (ZRH) meet-and-greets for global CEOs and heads of state attending the annual summit.",
     None, None, "Luxury AWD executive vehicles navigating snowy Alpine roads in Davos.",
     [("Dates", "January 18–22, 2027"), ("Location", "Davos, Switzerland"), ("Notes", "~3,000 leaders; CEOs and heads of state")], ["davos@propodiumevents.com"], anchor="davos"),
   E("IMEX America (Las Vegas, NV)", "IMEX America",
     "Managed dedicated trade show delegate shuttles, buyer VIP transfers, and evening networking event mobility across top Las Vegas venues during the flagship MICE industry gathering.",
     None, None, "Executive fleet staged outside the Mandalay Bay Convention Center.",
     [("Dates", "September 28–30, 2027"), ("Location", "Las Vegas, NV — Mandalay Bay"), ("Notes", "6,200+ buyers; key show for event agencies")], ["imex@propodiumevents.com"], anchor="imex"),
   E("TomorrowX (TomorrowX Global Summit)", "TomorrowX",
     "Delivered end-to-end executive transportation for international tech founders, keynote speakers, and venture capital delegations attending tomorrow-tech global panels.",
     None, None, "High-tech modern fleet lined up outside an international innovation summit hall.",
     [("Dates", "Mid-November 2027 (TBC)"), ("Location", "Austin, TX — Moody Center"), ("Notes", "AI, tech and finance summit; 2026 edition was November 17–18 in Austin. 2027 dates not yet announced")],
     ["tomorrowx@propodiumevents.com"], anchor="tomorrowx"),
   E("Money 20/20 USA (Las Vegas, NV)", "Money 20/20 USA",
     "Provided seamless airport-to-hotel transfers, corporate hospitality shuttles, and C-level executive charter services for the world's leading fintech and payments conference.",
     None, None, "Black sedan fleet staged outside The Venetian Resort in Las Vegas.",
     [("Dates", "October 19–21, 2027"), ("Location", "Las Vegas, NV")], ["money2020@propodiumevents.com"], anchor="money2020"),
  ],
  cta="Sending executives or a delegation to a 2027 conference? Contact us to plan shuttles, transfers and airport arrivals."),

 dict(id="ev-government", file="events/government.html", menu="Government & Summits", headline="Diplomatic & Global Summits",
  intro="Intergovernmental summits demand protocol, security and timing measured to the minute. Pro Podium Events supports delegations, support staff and global media with protocol-compliant vehicles, diplomatic greeters and 24/7 dispatch command.",
  services=["Executive & VIP Transportation", "Airport Greeters & FBO Meet-and-Greet", "On-Site Event Coordinators", "Group Transportation & Shuttle Logistics"],
  events=[
   E("G7 & G20 Leaders’ Summits", "G7 & G20",
     "Supported international delegations, bilateral support staff, and global media teams with protocol-compliant vehicles, credentialed access, and secure staging near high-security summit zones.",
     None, None, None,
     [("G7 (53rd)", "Dates TBC (usually June) — United States, city TBC. US holds the 2027 G7 presidency"),
      ("G20", "November 27–28, 2027 — Manchester, UK (Manchester Central). UK holds the 2027 G20 presidency, with meetings across the country all year")],
     ["g7@propodiumevents.com", "g20@propodiumevents.com"], anchor="g7-g20"),
   E("United Nations (UN) General Assembly & Global Conferences", "UN General Assembly",
     "Executed high-security metropolitan logistics during UNGA and affiliated global forums, managing tight Midtown/venue staging windows, diplomatic protocol, and 24/7 dispatch command.",
     None, None, None,
     [("Dates", "82nd session opens September 7, 2027; high-level week from September 21"), ("Location", "New York, NY — UN Headquarters"), ("Notes", "Heads of state from around the world")],
     ["un@propodiumevents.com"], anchor="un-general-assembly"),
  ],
  cta="Supporting a delegation at a 2027 summit? Contact us to plan protocol-ready ground transportation."),
]
CTA_EMAIL = "leo@propodiumevents.com"

PAST_TITLE = "Past Events & Proven Track Record"
PAST_SUB = "Summary Matrix: Historical Productions"
PAST_COLS = ["Event Category", "Flagship Events", "Key Operational Scope", "Highlights & Coverage", "Event Contacts (@propodiumevents.com)"]
PAST_ROWS = [
 ("Sports & Equestrian", "Super Bowl LXI, NASCAR Cup Series, NBA All-Star Weekend, PGA Tour, The Kentucky Derby",
  "VIP Talent Transit, Player Courtesy Fleets, Private FBO Arrivals", "Multi-venue perimeter access, stadium and trackside logistics",
  ["superbowl", "nascar", "nbaallstar", "pga", "kentuckyderby"]),
 ("Music, Culture & Yachting", "SXSW, The Oscars, Coachella, Cannes Film Festival, Lollapalooza (US & Brazil), Monaco Yacht Show",
  "Red-carpet transfers, Desert & Riviera FBO logistics, Superyacht guest transit", "High-density street closure & harbor perimeter management",
  ["sxsw", "oscars", "coachella", "cannes", "lollapalooza", "lollapaloozabrazil", "monacoyachtshow"]),
 ("Business & Global Conferences", "CES, World Economic Forum (Davos), IMEX America, TomorrowX, Money 20/20 USA",
  "C-Suite shuttles, Alpine/Metropolitan dispatch, Trade show perimeter access", "Executive venue transfers & airport meet-and-greet coverage",
  ["ces", "davos", "imex", "tomorrowx", "money2020"]),
 ("Diplomatic & Intergovernmental Summits", "G7 / G20 Summits, UN General Assembly",
  "Protocol motorcades, Diplomatic Greeters, High-security Staging", "Escorted motorcade support & 24/7 central dispatch command",
  ["g7", "g20", "un"]),
]


# ---------- Nov 26 final home copy ("Pro Podium Website Changes" PDF) ----------
SITE_EMAIL = "info@propodiumevents.com"
SITE_PHONE = "(737) 202-7261"
SITE_PHONE_TEL = "+17372027261"

HERO_TITLE = "The ground operations team behind your event."
HERO_TEXT = ("VIP and corporate hospitality arrivals, airport greeters, on-site coordinators and executive transportation, "
             "handled from first arrival to last departure. Trusted at F1, the Super Bowl and the FIFA World Cup since 2019.")
HERO_LINE = ["Since 2019", "United States", "Mexico", "Canada", "Brazil"]

PACKAGES_TITLE = "Three ways we support your event"
PACKAGES = [
    ("VIP & Hospitality Arrival", "Airport and FBO greeters, arrival coordination and a single point of contact for your VIP and corporate hospitality guests."),
    ("Talent & Executive Movement", "Executive vehicles and coordination for artists, speakers and executives. Discreet, punctual and built around your schedule."),
    ("Full Event Ground Operations", "Everything above, plus on-site coordinators, group shuttle logistics and a dedicated lead on the ground for the full run of your event."),
]
PACKAGES_NOTE = "Every package includes a pre-event logistics plan and a post-event report."

HOW_TITLE = "Simple from the first call to the last guest"
HOW_STEPS = [
    ("Share your event.", "Send us the dates, venues and guest list."),
    ("We build your ground plan.", "Arrivals, vehicles, greeters and coordinators, mapped out in detail, at no cost."),
    ("We run it and report back.", "Your team focuses on the show. We handle the movement, then deliver a full report."),
]

WHO_TITLE = "Built for event organizers"
WHO_TEXT = ("Directors of operations, hospitality leads and producers who need every guest welcomed, moved and looked after, "
            "without managing a dozen vendors.")
WHO_ALSO = [
    ("Hospitality companies & agencies", "Executive and VIP transportation, airport greeters and guest welcome for your hosted guests."),
    ("Event-transport companies", "We don't compete with you. We work alongside you as an extension of your team."),
]

EVENTS_HOME_TITLE = "Events we support"
EVENTS_HOME_TEXT = ("Since 2019, Pro Podium Events has supported guest transportation and on-site operations "
                    "at the world's most demanding events.")
# (label, category page id, events)
EVENTS_HOME = [
    ("Motorsport", "ev-motorsport", ["F1 Austin", "F1 Miami", "F1 Montreal", "F1 Las Vegas", "F1 Mexico City", "F1 São Paulo", "NASCAR"]),
    ("Major Sporting Events", "ev-sports", ["Super Bowl", "FIFA World Cup", "FIFA Women's World Cup", "NBA All-Star", "PGA Tour", "Kentucky Derby"]),
    ("Festivals, Film & Culture", "ev-festivals", ["SXSW", "ACL Fest", "The Oscars", "Coachella", "Cannes Film Festival", "Lollapalooza USA", "Lollapalooza Brazil", "Monaco Yacht Show"]),
    ("Corporate Conferences & Trade Shows", "ev-business", ["CES", "World Economic Forum", "IMEX America", "TomorrowX", "Money 20/20 USA"]),
    ("Diplomatic & Global Summits", "ev-government", ["G7 & G20", "UN General Assembly"]),
]
EVENTS_DISCLAIMER = ("Event names are trademarks of their respective owners. "
                     "Pro Podium Events is an independent ground operations provider.")

REVIEWS_TITLE = "What our clients say"
REVIEWS_TEXT = "Worked with Pro Podium Events? We'd love to hear about your experience."
# Only real, approved reviews go here. While the list is empty the list is hidden.
# Each review: {"stars": 5, "text": "...", "name": "...", "title": "...", "event": "..."}
REVIEWS = []
REVIEW_CONSENT = "I agree that Pro Podium Events may display my review on this website."
REVIEW_THANKS = "Thank you! Your review will appear on our site once approved."

NETWORK_TITLE = "Our network"
NETWORK_TEXT = "We work with trusted partners across the U.S. to deliver premium vehicles and guest service."

FINAL_TITLE = "Let's plan your event's ground operations."
FINAL_TEXT = "Tell us about your event and we'll send you a free ground plan."
CTA_BUTTON = "Request a free ground plan"
