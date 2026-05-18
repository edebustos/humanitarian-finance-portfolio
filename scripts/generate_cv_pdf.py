from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "docs" / "Ernesto_de_Bustos_CV.pdf"

WIDTH, HEIGHT = A4
MARGIN_X = 42
TOP = HEIGHT - 42
BOTTOM = 40
RED = colors.HexColor("#E03131")
DARK = colors.HexColor("#1f2937")
MUTED = colors.HexColor("#4b5563")
LIGHT = colors.HexColor("#e5e7eb")


def wrap_text(text, max_chars):
    words = text.split()
    lines = []
    current = []
    for word in words:
        candidate = " ".join(current + [word])
        if len(candidate) <= max_chars:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def draw_text(c, text, x, y, size=8.5, color=DARK, font="Helvetica", leading=10.5, max_chars=95):
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap_text(text, max_chars):
        if y < BOTTOM:
            break
        c.drawString(x, y, line)
        y -= leading
    return y


def heading(c, title, x, y):
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(x, y, title.upper())
    c.setStrokeColor(LIGHT)
    c.setLineWidth(0.6)
    c.line(x, y - 4, WIDTH - MARGIN_X, y - 4)
    return y - 16


def bullet(c, text, x, y, max_chars=92, size=8.1):
    c.setFillColor(DARK)
    c.setFont("Helvetica", size)
    lines = wrap_text(text, max_chars)
    if not lines:
        return y
    c.drawString(x, y, "-")
    c.drawString(x + 10, y, lines[0])
    y -= 9.6
    for line in lines[1:]:
        c.drawString(x + 10, y, line)
        y -= 9.6
    return y - 1.5


def role(c, title, org_place, dates, x, y):
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 8.7)
    c.drawString(x, y, title)
    c.setFont("Helvetica", 8.0)
    c.setFillColor(MUTED)
    c.drawRightString(WIDTH - MARGIN_X, y, dates)
    y -= 9.8
    c.drawString(x, y, org_place)
    return y - 12


def tag_line(c, labels, x, y):
    c.setFillColor(colors.HexColor("#f3f4f6"))
    c.roundRect(x, y - 18, WIDTH - (2 * MARGIN_X), 24, 5, fill=1, stroke=0)
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 7.7)
    c.drawCentredString(WIDTH / 2, y - 9, "  |  ".join(labels))
    return y - 32


def header(c):
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(MARGIN_X, TOP, "Ernesto de Bustos")
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(MARGIN_X, TOP - 18, "Senior Humanitarian Finance & Operations Manager")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 7.8)
    c.drawString(MARGIN_X, TOP - 33, "Email: edebustos@duck.com | Phone: (+34) 692793157")
    c.drawString(MARGIN_X, TOP - 44, "LinkedIn: linkedin.com/in/ernesto-de-bustos-136662233 | Portfolio: edebustos.github.io/humanitarian-finance-portfolio/")
    c.drawString(MARGIN_X, TOP - 55, "GitHub: github.com/edebustos/humanitarian-finance-portfolio | Dashboard: edebustos.github.io/humanitarian-finance-portfolio/pages/dashboard.html")
    c.setStrokeColor(RED)
    c.setLineWidth(1.2)
    c.line(MARGIN_X, TOP - 64, WIDTH - MARGIN_X, TOP - 64)
    return TOP - 82


def footer(c, page):
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 7)
    c.drawRightString(WIDTH - MARGIN_X, 24, f"Ernesto de Bustos - CV - Page {page} of 2")


def build_pdf():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=A4)
    c.setTitle("Ernesto de Bustos - Humanitarian Finance and Operations CV")
    c.setAuthor("Ernesto de Bustos")

    y = header(c)
    y = heading(c, "Profile Summary", MARGIN_X, y)
    summary = (
        "Humanitarian finance and operations professional with 15+ years of experience across conflict, "
        "emergency and recovery contexts including Ukraine, Poland, Palestine, Sudan, Syria, Ethiopia, "
        "Venezuela, Colombia and Peru. Strong Red Cross Movement and INGO background combining donor "
        "compliance, grant management, forecasting, CVA operations, branch coordination, ERP literacy, "
        "financial reporting and practical humanitarian analytics."
    )
    y = draw_text(c, summary, MARGIN_X, y, size=8.4, leading=10.2, max_chars=105)
    y -= 5
    y = tag_line(
        c,
        [
            "Humanitarian finance",
            "Operations management",
            "Donor compliance",
            "CVA",
            "Power BI trajectory",
        ],
        MARGIN_X,
        y,
    )

    y = heading(c, "Core Strengths", MARGIN_X, y)
    strengths = [
        "Budget monitoring, BFU, forecasting, cost allocation, liquidity planning and audit readiness.",
        "Institutional donor reporting and compliance across ECHO, EU, GFFO, BMZ, USAID, UNICEF, AECID and related frameworks.",
        "Field operations support covering HR/admin, procurement follow-up, partner finance, branch coordination and documentation control.",
        "CVA implementation experience including RedRose setup, volunteer mobilisation, vulnerability targeting and distribution support.",
    ]
    for item in strengths:
        y = bullet(c, item, MARGIN_X, y)

    y = heading(c, "Selected Professional Experience", MARGIN_X, y - 2)
    y = role(c, "Projects Manager", "Austrian Red Cross - Kyiv, Ukraine", "Apr 2024 - Jan 2025", MARGIN_X, y)
    for item in [
        "Supported financial and operational oversight of an integrated multi-donor master budget of approximately EUR 11M over three years.",
        "Worked across URCS branch support in Donetsk, Zaporizhzhia, Chernihiv, Lviv, Zakarpattia and Chernivtsi.",
        "Provided programme and financial inputs for planning, reporting, forecasting and new proposals.",
    ]:
        y = bullet(c, item, MARGIN_X + 8, y, max_chars=88)

    y = role(c, "Surge Finance Delegate", "German Red Cross - Kyiv, Ukraine and Ramallah, Palestine", "2023 - 2025", MARGIN_X, y)
    for item in [
        "Supported donor financial reporting and budget follow-up for GFFO, BMZ and ECHO-funded humanitarian operations.",
        "Verified supporting documentation, expenditure evidence and payment statements for HQ and donor submission.",
    ]:
        y = bullet(c, item, MARGIN_X + 8, y, max_chars=88)

    y = role(c, "Cash & Voucher Assistance Delegate", "German Red Cross - Lublin, Poland", "Apr 2022 - Mar 2023", MARGIN_X, y)
    for item in [
        "Supported a EUR 1.6M CVA programme for 300 vulnerable Ukrainian refugee families.",
        "Led RedRose CVA platform procurement and operational setup; coordinated distributions with 10-15 volunteers per cycle.",
        "Delivered CVA trainings to 40-60 volunteers per session through larger branch hubs serving smaller branches.",
    ]:
        y = bullet(c, item, MARGIN_X + 8, y, max_chars=88)

    y = role(c, "Country Finance Coordinator Colombia/Venezuela", "INTERSOS - San Cristobal, Venezuela", "May 2021 - Dec 2021", MARGIN_X, y)
    for item in [
        "Coordinated finance follow-up across Venezuela and Colombia operations, including bank accounts, petty cash, budget monitoring and documentation control.",
        "Managed donor-funded portfolio exposure including ECHO, USAID, UNICEF and Stichting Vluchteling funding.",
    ]:
        y = bullet(c, item, MARGIN_X + 8, y, max_chars=88)

    footer(c, 1)
    c.showPage()

    y = header(c)
    y = heading(c, "Additional Humanitarian Experience", MARGIN_X, y)
    compact_roles = [
        ("Country Administrator / Acting Field Coordinator", "Doctors of the World - Amuda / Kobane, Syria", "2018 - 2019", "Managed finance, administration and HR support across two bases for a CAD 2.5M mission; coordinated a finance department of five people and HR processes for approximately 45 staff."),
        ("Food Security Delegate / Acting Head of Mission", "Spanish Red Cross - Port Sudan, Sudan", "2016 - 2018", "Managed programme follow-up, EU reporting, procurement, audits and closure of a EUR 1.2M food security, livelihoods and WASH programme in 28 rural communities."),
        ("Food Security Delegate", "ONG Rescate Internacional - Dire Dawa, Ethiopia", "2009 - 2011", "Managed food security projects funded by AECID, regional Spanish donors and La Caixa; contributed to design of a second AECID agreement of approximately EUR 3M."),
        ("Project / R&D&I Coordinator", "Ezentis and CIDEAL Foundation - Spain / Peru", "2013 - 2016", "Coordinated NGO digitalisation and EU-funded innovation work, including budget planning, milestones, team coordination and technical/financial reporting."),
    ]
    for title, org, dates, desc in compact_roles:
        y = role(c, title, org, dates, MARGIN_X, y)
        y = bullet(c, desc, MARGIN_X + 8, y, max_chars=88)

    y = heading(c, "Portfolio Projects and Analytics Evidence", MARGIN_X, y - 2)
    project_items = [
        "Humanitarian Finance Dashboard Demo: synthetic donor finance, compliance and operational reporting dashboard for management review.",
        "Power BI Humanitarian Analytics: portfolio pack with screenshots, model notes, DAX measures and synthetic humanitarian datasets.",
        "Multi-donor Budget Management: evidence around master budget consolidation, forecasting, donor reporting and branch-level finance support.",
        "CVA Operations Evidence: Poland and Ukraine examples covering targeting, RedRose, volunteer training and operational delivery.",
    ]
    for item in project_items:
        y = bullet(c, item, MARGIN_X, y)

    y = heading(c, "Donor, Country and Systems Exposure", MARGIN_X, y - 2)
    y = draw_text(c, "Donors and frameworks: ECHO, EU, GFFO, BMZ, USAID, UNICEF, AECID, ADA, Neighbour in Need, EU Trust Funds and Stichting Vluchteling.", MARGIN_X, y, size=8.2, leading=10, max_chars=104)
    y = draw_text(c, "Countries and contexts: Ukraine, Poland, Palestine, Sudan, Syria, Ethiopia, Venezuela, Colombia and Peru.", MARGIN_X, y - 2, size=8.2, leading=10, max_chars=104)
    y = draw_text(c, "Systems and analytics: Power BI PL-300 in progress, Advanced Excel MOS-211 in progress, Dynamics 365 exposure, Agresso, Odoo, FundsPro, RedRose, Office 365 and data visualization.", MARGIN_X, y - 2, size=8.2, leading=10, max_chars=104)

    y = heading(c, "Education and Training", MARGIN_X, y - 4)
    education = [
        "MA Innovation and Knowledge Management - Complutense University of Madrid.",
        "MA International Business Administration - Economic & Commercial Center (CECO).",
        "Postgraduate in Food Security Programme Management - Universitat Oberta de Catalunya / FAO.",
        "Bachelor of Economics - Complutense University of Madrid.",
        "HEAT Security Training; Practical Emergency Cash Transfer (PECT); Cash-Based Interventions; IFRC Livelihoods Centre trainings.",
    ]
    for item in education:
        y = bullet(c, item, MARGIN_X, y, max_chars=92)

    y = heading(c, "Languages", MARGIN_X, y - 2)
    y = draw_text(c, "Spanish: native/C2 | English: C1 | Russian: B1 | Arabic: A2", MARGIN_X, y, size=8.2, leading=10, max_chars=104)

    footer(c, 2)
    c.showPage()
    c.save()


if __name__ == "__main__":
    build_pdf()
    print(OUTPUT)
