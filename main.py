from fasthtml.common import *
from monsterui.all import *
from datetime import datetime
import json
import os
from pathlib import Path

# Email setup (using Resend - set RESEND_API_KEY env var)
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
OWNER_EMAIL = "alexharris.software@gmail.com"

# Simple JSON storage for leads
LEADS_FILE = Path("leads.json")

def save_lead(data: dict):
    """Save lead to JSON file"""
    leads = []
    if LEADS_FILE.exists():
        leads = json.loads(LEADS_FILE.read_text())
    leads.append({**data, "timestamp": datetime.now().isoformat()})
    LEADS_FILE.write_text(json.dumps(leads, indent=2))

async def send_lead_email(data: dict):
    """Send lead email via Resend if API key available"""
    if not RESEND_API_KEY:
        return

    try:
        from resend import Resend
        client = Resend(api_key=RESEND_API_KEY)

        email_body = f"""
New lead from Phoenix IT Pros website:

Name: {data.get('first_name', '')} {data.get('last_name', '')}
Email: {data.get('email', '')}
Phone: {data.get('phone', '')}
Company: {data.get('company', '')}
Employees: {data.get('employees', '')}
Service: {data.get('service', '')}
Message: {data.get('message', '')}
        """

        client.emails.send({
            "from": "noreply@phoenixitpros.com",
            "to": OWNER_EMAIL,
            "subject": f"New Lead: {data.get('company', 'Unknown Company')}",
            "html": email_body.replace('\n', '<br>'),
        })
    except Exception as e:
        print(f"Email send failed: {e}")

app, rt = fast_app(
    hdrs=(
        Meta(charset="UTF-8"),
        Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        Meta(name="description", content="Phoenix IT Services | Managed IT, AI Workflow Automation, UniFi Cameras & Cybersecurity. Local Phoenix experts, 24/7 support."),
        Meta(name="keywords", content="IT services Phoenix, managed IT Phoenix AZ, AI workflow automation, UniFi installation, Ubiquiti, cybersecurity, cloud solutions"),
    ),
    title="Phoenix IT Services | #1 Managed IT Support Phoenix AZ",
)

@rt("/")
def get():
    return Html(
        Head(Title("Phoenix IT Services | Managed IT & AI Automation")),
        Body(
            # Navigation
            Nav(
                Container(
                    Div(
                        H3("Phoenix IT Pros", cls="text-xl font-bold text-blue-600"),
                        Ul(
                            Li(A("Services", href="#services")),
                            Li(A("Why Us", href="#why")),
                            Li(A("Contact", href="#contact")),
                            cls="flex gap-6",
                        ),
                        cls="flex justify-between items-center",
                    ),
                    cls="py-4",
                ),
                cls="border-b sticky top-0 bg-white z-50",
            ),

            # Hero
            Section(
                Container(
                    Div(
                        H1("Phoenix's #1 IT Services Company", cls="text-5xl font-bold mb-4"),
                        P("Fast. Local. Reliable.", cls="text-2xl text-orange-600 mb-4"),
                        P("Managed IT support, cybersecurity, AI automation, and UniFi installations for Phoenix businesses.", cls="text-lg text-gray-600 mb-6"),
                        Div(
                            A("Get a Free Quote", href="#contact", cls="btn btn-primary"),
                            A("Call (602) 555-0199", href="tel:+16025550199", cls="btn btn-outline"),
                            cls="flex gap-4",
                        ),
                        cls="max-w-2xl",
                    ),
                    cls="py-20 text-center",
                ),
                cls="bg-gradient-to-r from-blue-50 to-blue-100",
            ),

            # Services
            Section(
                Container(
                    H2("Our Services", cls="text-4xl font-bold mb-12 text-center", id="services"),
                    Grid(
                        Card(H3("🖥️ Managed IT", cls="text-xl font-bold"), P("All-inclusive IT support so you focus on your business, not tech.")),
                        Card(H3("🤖 AI Automation", cls="text-xl font-bold"), P("ChatGPT & Claude integrations for customer service, documents, leads.")),
                        Card(H3("📹 UniFi Cameras", cls="text-xl font-bold"), P("Professional Ubiquiti camera installations with 24/7 monitoring.")),
                        Card(H3("🔒 Cybersecurity", cls="text-xl font-bold"), P("Endpoint protection, threat monitoring, compliance for Phoenix businesses.")),
                        Card(H3("☁️ Cloud Solutions", cls="text-xl font-bold"), P("Microsoft 365, Azure, hybrid cloud migrations tailored to you.")),
                        Card(H3("💾 Backup & DR", cls="text-xl font-bold"), P("Automated backups with rapid restore — downtime ends here.")),
                        cols="3",
                    ),
                    cls="py-20",
                ),
            ),

            # Why Us
            Section(
                Container(
                    H2("Why Choose Phoenix IT Pros", cls="text-4xl font-bold mb-12 text-center", id="why"),
                    Grid(
                        Card(H3("< 15 min", cls="text-3xl font-bold text-blue-600"), P("Average Response Time")),
                        Card(H3("500+", cls="text-3xl font-bold text-blue-600"), P("Phoenix Clients Served")),
                        Card(H3("99.9%", cls="text-3xl font-bold text-blue-600"), P("Uptime SLA Guaranteed")),
                        Card(H3("24/7", cls="text-3xl font-bold text-blue-600"), P("Help Desk Support")),
                        cols="4",
                    ),
                    cls="py-20",
                ),
                cls="bg-gray-50",
            ),

            # Contact Form
            Section(
                Container(
                    H2("Get a Free IT Assessment", cls="text-4xl font-bold mb-12 text-center", id="contact"),
                    Form(
                        Grid(
                            Input(name="first_name", placeholder="First Name", required=True),
                            Input(name="last_name", placeholder="Last Name", required=True),
                            cols="2",
                        ),
                        Input(name="email", type="email", placeholder="Email", required=True),
                        Input(name="phone", type="tel", placeholder="Phone Number"),
                        Input(name="company", placeholder="Company Name", required=True),
                        Select(
                            Option("Select # of Employees", disabled=True, selected=True),
                            Option("1-10"),
                            Option("11-50"),
                            Option("51-200"),
                            Option("200+"),
                            name="employees",
                        ),
                        Select(
                            Option("Select a Service", disabled=True, selected=True),
                            Option("Managed IT"),
                            Option("AI Automation"),
                            Option("UniFi Cameras"),
                            Option("Cybersecurity"),
                            Option("Cloud Solutions"),
                            Option("Not sure — need assessment"),
                            name="service",
                        ),
                        Textarea(name="message", placeholder="Tell us about your IT challenges (optional)", rows="4"),
                        Button("Get My Free Assessment", type="submit", cls="btn btn-primary w-full"),
                        P("No spam, no sales pressure. One of our local experts will call you within 1 business hour.", cls="text-sm text-gray-600 text-center"),
                        method="post",
                        action="/contact",
                        cls="max-w-2xl mx-auto space-y-4",
                    ),
                    cls="py-20",
                ),
            ),

            # Footer
            Footer(
                Container(
                    Div(
                        P(Strong("Phoenix IT Pros"), " | 1 N Central Ave Suite 900, Phoenix, AZ 85004"),
                        P(A("(602) 555-0199", href="tel:+16025550199")),
                        P(f"© {datetime.now().year} Phoenix IT Pros LLC. All rights reserved."),
                        cls="text-center text-gray-600",
                    ),
                    cls="py-8 border-t",
                ),
                cls="bg-gray-900 text-white",
            ),
        ),
    )

@rt("/contact", methods=["POST"])
async def post(req):
    """Handle lead form submission"""
    form = await req.form()
    data = dict(form)

    # Save lead to JSON
    save_lead(data)

    # Send email (if Resend configured)
    await send_lead_email(data)

    # Show success message
    return Html(
        Head(Title("Thank You — Phoenix IT Pros")),
        Body(
            Section(
                Container(
                    Card(
                        H2("✅ Thank You!", cls="text-3xl font-bold mb-4"),
                        P("We received your request. One of our Phoenix IT experts will call you within 1 business hour."),
                        P("If you don't hear from us, call us directly at (602) 555-0199", cls="mt-4 text-gray-600"),
                        A("← Back to Home", href="/", cls="btn btn-outline mt-6"),
                        cls="text-center max-w-lg",
                    ),
                    cls="py-20",
                ),
                cls="min-h-screen flex items-center justify-center",
            ),
        ),
    )

@rt("/leads")
def leads():
    """View all captured leads (unprotected - add auth in production!)"""
    if not LEADS_FILE.exists():
        return P("No leads yet.")

    leads_data = json.loads(LEADS_FILE.read_text())
    return Html(
        Head(Title("Leads — Phoenix IT Pros")),
        Body(
            Container(
                H1("Captured Leads"),
                Table(
                    Thead(
                        Tr(
                            Th("Name"), Th("Email"), Th("Company"),
                            Th("Service"), Th("Date"),
                        ),
                    ),
                    Tbody(
                        *[
                            Tr(
                                Td(f"{lead.get('first_name', '')} {lead.get('last_name', '')}"),
                                Td(lead.get('email', '')),
                                Td(lead.get('company', '')),
                                Td(lead.get('service', '')),
                                Td(lead.get('timestamp', '')[:10]),
                            )
                            for lead in reversed(leads_data)
                        ],
                    ),
                    cls="table table-striped",
                ),
                cls="py-10",
            ),
        ),
    )

if __name__ == "__main__":
    serve()
