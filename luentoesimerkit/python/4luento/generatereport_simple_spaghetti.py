from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

# Add text
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="PDF Report with Image", ln=True, align='C')

# Add image
pdf.image("houses.png", x=50, y=30, w=100)

# Save PDF
pdf.output("report.pdf")
