from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def generate_pdf(response, context):

    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Dairy Farm Report", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # TABLE DATA
    data = [
        ["Metric", "Value"],
        ["Total Animals", context['total_animals']],
        ["Total Milk (L)", context['total_milk']],
        ["Total Revenue", context['total_revenue']],
        ["Total Expense", context['total_expense']],
        ["Net Profit", context['profit']],
    ]

    table = Table(data)

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))

    elements.append(table)

    doc.build(elements)