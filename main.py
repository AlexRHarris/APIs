from fasthtml.common import *
from datetime import datetime

app, rt = fast_app(
    hdrs=(
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Meta(name="description", content="Phoenix IT Services | Managed IT Support, Cybersecurity & Cloud Solutions for Phoenix, AZ businesses. Fast response, local experts. Get a free quote today."),
        Meta(name="keywords", content="IT services Phoenix, managed IT Phoenix AZ, IT support Phoenix, cybersecurity Phoenix, cloud solutions Phoenix, IT company Scottsdale, IT help desk Phoenix"),
        Meta(name="robots", content="index, follow"),
        Meta(property="og:title", content="Phoenix IT Services | #1 Managed IT Support in Phoenix AZ"),
        Meta(property="og:description", content="Local Phoenix IT experts delivering managed IT, cybersecurity, cloud, and helpdesk services. 24/7 support, fast response times."),
        Meta(property="og:type", content="website"),
        Meta(name="geo.region", content="US-AZ"),
        Meta(name="geo.placename", content="Phoenix, Arizona"),
        Link(rel="canonical", href="https://phoenixitpros.com/"),
        Script(type="application/ld+json", _content='''
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Phoenix IT Pros",
  "description": "Managed IT services, cybersecurity, cloud solutions, and 24/7 helpdesk support for Phoenix area businesses.",
  "url": "https://phoenixitpros.com",
  "telephone": "+1-602-555-0199",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "1 N Central Ave, Suite 900",
    "addressLocality": "Phoenix",
    "addressRegion": "AZ",
    "postalCode": "85004",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 33.4484,
    "longitude": -112.0740
  },
  "areaServed": ["Phoenix", "Scottsdale", "Tempe", "Mesa", "Chandler", "Gilbert", "Glendale"],
  "openingHours": "Mo-Fr 08:00-18:00",
  "priceRange": "$$",
  "sameAs": []
}
        '''),
        Style("""
            :root {
                --blue: #1a56db;
                --blue-dark: #1341b0;
                --orange: #f05a28;
                --gray-dark: #1f2937;
                --gray-mid: #4b5563;
                --gray-light: #f3f4f6;
                --white: #ffffff;
            }
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body { font-family: 'Segoe UI', Arial, sans-serif; color: var(--gray-dark); line-height: 1.6; }
            a { color: var(--blue); text-decoration: none; }
            a:hover { text-decoration: underline; }

            /* NAV */
            nav {
                background: var(--gray-dark);
                padding: 0 2rem;
                display: flex;
                align-items: center;
                justify-content: space-between;
                height: 64px;
                position: sticky; top: 0; z-index: 100;
            }
            .nav-brand { color: #fff; font-size: 1.3rem; font-weight: 700; letter-spacing: -0.5px; }
            .nav-brand span { color: var(--orange); }
            .nav-links { display: flex; gap: 1.5rem; list-style: none; }
            .nav-links a { color: #d1d5db; font-size: 0.95rem; }
            .nav-links a:hover { color: #fff; text-decoration: none; }
            .nav-cta {
                background: var(--orange); color: #fff !important;
                padding: 0.45rem 1.1rem; border-radius: 6px; font-weight: 600;
            }
            .nav-cta:hover { background: #d44e22; }

            /* HERO */
            .hero {
                background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 100%);
                color: #fff;
                padding: 5rem 2rem 4rem;
                text-align: center;
            }
            .hero h1 { font-size: clamp(1.8rem, 4vw, 3rem); font-weight: 800; line-height: 1.2; margin-bottom: 1rem; }
            .hero h1 span { color: var(--orange); }
            .hero p { font-size: 1.15rem; color: #cbd5e1; max-width: 640px; margin: 0 auto 2rem; }
            .hero-btns { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
            .btn-primary {
                background: var(--orange); color: #fff;
                padding: 0.8rem 2rem; border-radius: 8px; font-size: 1rem; font-weight: 700;
                transition: background 0.2s;
            }
            .btn-primary:hover { background: #d44e22; text-decoration: none; }
            .btn-secondary {
                background: transparent; color: #fff;
                padding: 0.8rem 2rem; border-radius: 8px; font-size: 1rem; font-weight: 600;
                border: 2px solid #fff; transition: background 0.2s;
            }
            .btn-secondary:hover { background: rgba(255,255,255,0.1); text-decoration: none; }
            .hero-badges { margin-top: 2.5rem; display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap; }
            .badge {
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.2);
                color: #e2e8f0;
                padding: 0.4rem 1rem; border-radius: 99px; font-size: 0.85rem;
            }

            /* TRUST BAR */
            .trust-bar {
                background: var(--orange);
                padding: 0.75rem 2rem;
                text-align: center;
                color: #fff;
                font-weight: 600;
                font-size: 0.95rem;
                letter-spacing: 0.3px;
            }

            /* SECTIONS */
            section { padding: 4rem 2rem; }
            .container { max-width: 1100px; margin: 0 auto; }
            .section-label { color: var(--blue); font-size: 0.85rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 0.5rem; }
            .section-title { font-size: clamp(1.5rem, 3vw, 2.2rem); font-weight: 800; margin-bottom: 1rem; }
            .section-sub { color: var(--gray-mid); max-width: 600px; margin-bottom: 2.5rem; }

            /* SERVICES */
            .services-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 1.5rem;
            }
            .service-card {
                background: var(--white);
                border: 1px solid #e5e7eb;
                border-radius: 12px;
                padding: 1.75rem;
                transition: box-shadow 0.2s, transform 0.2s;
            }
            .service-card:hover { box-shadow: 0 8px 24px rgba(0,0,0,0.1); transform: translateY(-2px); }
            .service-icon { font-size: 2rem; margin-bottom: 0.75rem; }
            .service-card h3 { font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem; }
            .service-card p { color: var(--gray-mid); font-size: 0.95rem; }

            /* WHY US */
            .why-bg { background: var(--gray-light); }
            .why-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 1.5rem;
            }
            .why-card { background: #fff; border-radius: 12px; padding: 1.5rem; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
            .why-card .stat { font-size: 2.2rem; font-weight: 800; color: var(--blue); }
            .why-card .stat-label { color: var(--gray-mid); font-size: 0.9rem; margin-top: 0.25rem; }

            /* AREAS */
            .areas-list { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem; }
            .area-tag {
                background: var(--blue); color: #fff;
                padding: 0.4rem 1rem; border-radius: 99px; font-size: 0.9rem; font-weight: 500;
            }

            /* TESTIMONIALS */
            .testimonials-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 1.5rem;
            }
            .testimonial {
                background: #fff;
                border-left: 4px solid var(--blue);
                border-radius: 8px;
                padding: 1.5rem;
                box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            }
            .testimonial p { color: var(--gray-dark); font-style: italic; margin-bottom: 1rem; }
            .testimonial .author { font-weight: 700; font-size: 0.9rem; color: var(--blue); }
            .testimonial .stars { color: #f59e0b; font-size: 1rem; margin-bottom: 0.5rem; }

            /* FORM */
            .form-bg { background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 100%); color: #fff; }
            .form-bg .section-label { color: var(--orange); }
            .form-bg .section-title { color: #fff; }
            .form-bg .section-sub { color: #94a3b8; }
            .lead-form {
                background: #fff;
                border-radius: 16px;
                padding: 2.5rem;
                max-width: 580px;
                color: var(--gray-dark);
            }
            .form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
            .form-group { margin-bottom: 1.25rem; }
            .form-group label { display: block; font-weight: 600; font-size: 0.9rem; margin-bottom: 0.4rem; }
            .form-group input, .form-group select, .form-group textarea {
                width: 100%; padding: 0.7rem 1rem;
                border: 1px solid #d1d5db; border-radius: 8px;
                font-size: 1rem; font-family: inherit;
                transition: border-color 0.2s;
            }
            .form-group input:focus, .form-group select:focus, .form-group textarea:focus {
                outline: none; border-color: var(--blue);
                box-shadow: 0 0 0 3px rgba(26,86,219,0.15);
            }
            .form-group textarea { resize: vertical; min-height: 90px; }
            .form-submit {
                width: 100%; background: var(--orange); color: #fff;
                border: none; border-radius: 8px;
                padding: 0.9rem; font-size: 1rem; font-weight: 700;
                cursor: pointer; transition: background 0.2s;
            }
            .form-submit:hover { background: #d44e22; }
            .form-note { font-size: 0.8rem; color: var(--gray-mid); text-align: center; margin-top: 0.75rem; }

            /* SUCCESS */
            .success-msg {
                background: #ecfdf5; border: 1px solid #6ee7b7;
                border-radius: 12px; padding: 2rem; text-align: center; color: #065f46;
            }
            .success-msg h3 { font-size: 1.3rem; margin-bottom: 0.5rem; }

            /* FOOTER */
            footer {
                background: var(--gray-dark); color: #9ca3af;
                padding: 2rem; text-align: center; font-size: 0.9rem;
            }
            footer strong { color: #fff; }
            footer .footer-links { display: flex; gap: 1.5rem; justify-content: center; margin-bottom: 1rem; flex-wrap: wrap; }
            footer .footer-links a { color: #9ca3af; }
            footer .footer-links a:hover { color: #fff; }

            @media (max-width: 640px) {
                .form-row { grid-template-columns: 1fr; }
                .nav-links { display: none; }
            }
        """),
    ),
    title="Phoenix IT Services | #1 Managed IT Support Phoenix AZ",
)

SERVICES = [
    ("🖥️", "Managed IT Services", "Flat-rate, all-inclusive IT management so you can focus on your business — not your tech."),
    ("🔒", "Cybersecurity", "Endpoint protection, threat monitoring, and compliance for Phoenix-area businesses."),
    ("☁️", "Cloud Solutions", "Microsoft 365, Azure, and hybrid cloud migrations tailored to your needs."),
    ("📞", "24/7 Help Desk", "Local Phoenix technicians answering calls fast — average response under 15 minutes."),
    ("🔗", "Network & Infrastructure", "Structured cabling, firewalls, VPNs, and wireless for offices across the Valley."),
    ("💾", "Backup & Disaster Recovery", "Automated backups with rapid restore so downtime never kills your business."),
]

AREAS = ["Phoenix", "Scottsdale", "Tempe", "Mesa", "Chandler", "Gilbert", "Glendale", "Peoria", "Surprise", "Goodyear", "Avondale", "Fountain Hills"]

TESTIMONIALS = [
    ("★★★★★", "Switching to Phoenix IT Pros was the best decision we made. Response time is incredible and they actually fix issues the first time.", "Maria S., Office Manager — Scottsdale Law Firm"),
    ("★★★★★", "We had a ransomware scare and their team contained it within the hour. Can't imagine handling IT security without them.", "James R., CEO — Mesa Manufacturing Co."),
    ("★★★★★", "Finally an IT company that speaks plain English. They migrated us to Microsoft 365 with zero downtime.", "Linda K., Director — Chandler Non-Profit"),
]

def nav():
    return Nav(
        A(Span("Phoenix", cls=""), Span(" IT Pros", style="color:var(--orange)"), href="/", cls="nav-brand"),
        Ul(
            Li(A("Services", href="#services")),
            Li(A("Why Us", href="#why")),
            Li(A("Areas", href="#areas")),
            Li(A("Get a Quote", href="#contact", cls="nav-cta")),
            cls="nav-links",
        ),
    )

def hero():
    return Div(
        H1("Phoenix's #1 IT Services Company", Br(), Span("Fast. Local. Reliable.", style="color:var(--orange)")),
        P("Managed IT support, cybersecurity, and cloud solutions for businesses across the Phoenix metro. No contracts. No surprises. Just results."),
        Div(
            A("Get a Free Quote", href="#contact", cls="btn-primary"),
            A("Call (602) 555-0199", href="tel:+16025550199", cls="btn-secondary"),
            cls="hero-btns",
        ),
        Div(
            Span("✅ No Long-Term Contracts", cls="badge"),
            Span("⚡ <15 Min Response Time", cls="badge"),
            Span("🏆 500+ Phoenix Businesses Served", cls="badge"),
            Span("🔒 SOC 2 Compliant", cls="badge"),
            cls="hero-badges",
        ),
        cls="hero",
    )

def trust_bar():
    return Div("📍 Proudly serving Phoenix, Scottsdale, Tempe, Mesa, Chandler & the entire Valley since 2012", cls="trust-bar")

def services_section():
    cards = [
        Div(
            Div(icon, cls="service-icon"),
            H3(title),
            P(desc),
            cls="service-card",
        )
        for icon, title, desc in SERVICES
    ]
    return Section(
        Div(
            P("What We Do", cls="section-label"),
            H2("IT Services Built for Phoenix Businesses", cls="section-title"),
            P("From day-to-day helpdesk support to full cybersecurity strategy, we cover every layer of your IT.", cls="section-sub"),
            Div(*cards, cls="services-grid"),
            cls="container",
        ),
        id="services",
    )

def why_section():
    stats = [
        ("< 15 min", "Average Response Time"),
        ("500+", "Phoenix Clients Served"),
        ("99.9%", "Uptime SLA Guaranteed"),
        ("13 yrs", "Serving the Valley"),
        ("24/7", "Help Desk Coverage"),
        ("4.9 ★", "Google Review Rating"),
    ]
    cards = [
        Div(
            Div(stat, cls="stat"),
            Div(label, cls="stat-label"),
            cls="why-card",
        )
        for stat, label in stats
    ]
    return Section(
        Div(
            P("Why Choose Us", cls="section-label"),
            H2("The Phoenix IT Partner You Can Count On", cls="section-title"),
            P("We're not a national call center. We're your neighbors — local technicians who show up, fix issues fast, and treat your business like our own.", cls="section-sub"),
            Div(*cards, cls="why-grid"),
            cls="container",
        ),
        id="why",
        cls="why-bg",
    )

def areas_section():
    tags = [Span(area, cls="area-tag") for area in AREAS]
    return Section(
        Div(
            P("Service Area", cls="section-label"),
            H2("Serving the Entire Phoenix Metro", cls="section-title"),
            P("We provide on-site and remote IT support throughout the Greater Phoenix area:", cls="section-sub"),
            Div(*tags, cls="areas-list"),
            cls="container",
        ),
        id="areas",
    )

def testimonials_section():
    cards = [
        Div(
            Div(stars, cls="stars"),
            P(f'"{quote}"'),
            Div(author, cls="author"),
            cls="testimonial",
        )
        for stars, quote, author in TESTIMONIALS
    ]
    return Section(
        Div(
            P("Client Reviews", cls="section-label"),
            H2("Trusted by Phoenix Businesses", cls="section-title"),
            Div(*cards, cls="testimonials-grid"),
            cls="container",
        ),
        cls="why-bg",
    )

def contact_form(success=False):
    if success:
        return Div(
            H3("Thanks! We'll be in touch within 1 business hour."),
            P("One of our Phoenix IT specialists will reach out shortly to discuss your needs."),
            cls="success-msg",
        )
    return Form(
        Div(
            Div(Label("First Name"), Input(name="first_name", placeholder="Alex", required=True), cls="form-group"),
            Div(Label("Last Name"), Input(name="last_name", placeholder="Smith", required=True), cls="form-group"),
            cls="form-row",
        ),
        Div(Label("Business Email"), Input(name="email", type="email", placeholder="alex@yourcompany.com", required=True), cls="form-group"),
        Div(Label("Phone Number"), Input(name="phone", type="tel", placeholder="(602) 555-0100"), cls="form-group"),
        Div(Label("Company Name"), Input(name="company", placeholder="ACME Corp", required=True), cls="form-group"),
        Div(
            Label("Number of Employees"),
            Select(
                Option("Select...", value="", disabled=True, selected=True),
                Option("1–10", value="1-10"),
                Option("11–50", value="11-50"),
                Option("51–200", value="51-200"),
                Option("200+", value="200+"),
                name="employees",
            ),
            cls="form-group",
        ),
        Div(
            Label("Service Needed"),
            Select(
                Option("Select a service...", value="", disabled=True, selected=True),
                Option("Managed IT Services", value="managed-it"),
                Option("Cybersecurity", value="cybersecurity"),
                Option("Cloud Solutions", value="cloud"),
                Option("Help Desk Support", value="helpdesk"),
                Option("Network & Infrastructure", value="network"),
                Option("Backup & Disaster Recovery", value="backup"),
                Option("Not sure — need assessment", value="assessment"),
                name="service",
            ),
            cls="form-group",
        ),
        Div(Label("Tell us about your IT challenges (optional)"), Textarea(name="message", placeholder="e.g. We're having issues with slow network speeds and need better security..."), cls="form-group"),
        Button("Get My Free IT Assessment →", type="submit", cls="form-submit"),
        P("No spam, no sales pressure. A local Phoenix IT expert will call you within 1 business hour.", cls="form-note"),
        method="post", action="/contact",
        cls="lead-form",
    )

def contact_section(success=False):
    return Section(
        Div(
            Div(
                P("Free IT Assessment", cls="section-label"),
                H2("Get a Free Quote From Phoenix IT Pros", cls="section-title"),
                P("Tell us about your business and we'll put together a custom IT plan — no obligation, no cost.", cls="section-sub"),
                Ul(
                    Li("✅ Response within 1 business hour"),
                    Li("✅ Custom proposal for your business"),
                    Li("✅ No long-term contracts required"),
                    style="list-style:none; color:#94a3b8; font-size:0.95rem; line-height:2.2",
                ),
                style="max-width:420px",
            ),
            contact_form(success),
            style="display:flex; gap:3rem; flex-wrap:wrap; align-items:flex-start;",
            cls="container",
        ),
        id="contact",
        cls="form-bg",
        style="padding: 5rem 2rem;",
    )

def footer_section():
    return Footer(
        Div(
            A("Services", href="#services"),
            A("Why Us", href="#why"),
            A("Service Areas", href="#areas"),
            A("Contact", href="#contact"),
            A("Privacy Policy", href="/privacy"),
            cls="footer-links",
        ),
        P(Strong("Phoenix IT Pros"), " | 1 N Central Ave Suite 900, Phoenix, AZ 85004 | ", A("(602) 555-0199", href="tel:+16025550199", style="color:#9ca3af")),
        P(f"© {datetime.now().year} Phoenix IT Pros LLC. All rights reserved. Serving Phoenix, Scottsdale, Tempe, Mesa, Chandler & the Greater Phoenix Metro.", style="margin-top:0.5rem; font-size:0.8rem;"),
    )

@rt("/")
def get():
    return Html(
        Head(
            Title("Phoenix IT Services | #1 Managed IT Support Phoenix AZ | Phoenix IT Pros"),
        ),
        Body(
            nav(),
            hero(),
            trust_bar(),
            services_section(),
            why_section(),
            testimonials_section(),
            areas_section(),
            contact_section(),
            footer_section(),
        ),
        lang="en",
    )

@rt("/contact", methods=["POST"])
async def post(req):
    form = await req.form()
    # In production: save to DB, send notification email, trigger CRM webhook
    first = form.get("first_name", "")
    email = form.get("email", "")
    print(f"Lead received: {first} <{email}>")
    return Html(
        Head(Title("Thank You | Phoenix IT Pros")),
        Body(
            nav(),
            Section(
                Div(contact_section(success=True), style="padding:2rem 0"),
                style="background:linear-gradient(135deg,#0f172a 0%,#1e3a5f 100%); min-height:60vh; display:flex; align-items:center;",
            ),
            footer_section(),
        ),
        lang="en",
    )

@rt("/privacy")
def privacy():
    return Html(
        Head(Title("Privacy Policy | Phoenix IT Pros")),
        Body(
            nav(),
            Section(
                Div(
                    H1("Privacy Policy", style="margin-bottom:1rem"),
                    P("Phoenix IT Pros LLC respects your privacy. Information collected via our contact form is used solely to respond to your inquiry and is never sold to third parties."),
                    P(f"Last updated: {datetime.now().strftime('%B %Y')}", style="margin-top:1rem; color:var(--gray-mid)"),
                    cls="container",
                ),
            ),
            footer_section(),
        ),
        lang="en",
    )

serve()
