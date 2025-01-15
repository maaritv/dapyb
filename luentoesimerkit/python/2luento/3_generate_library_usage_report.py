from fpdf import FPDF
import json

def readJsonFile(json_file_name):
    with open(json_file_name, 'r') as file:
        data = json.load(file)
    return data

def createReportObjectWithHeader(report_header):
    pdf = FPDF()
    pdf.add_page()

    # Add text
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=report_header, ln=True, align='L')
    return pdf

def addLibraryMetricsTable(pdf, library_section_texts, json_data):
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=library_section_texts["late_books"], ln=True, align='L')    
    pdf.cell(200, 10, txt=library_section_texts["lost_books"], ln=True, align='L') 

    # Set font for the table
    pdf.set_font("Arial", size=10)
    col_width = pdf.w / 2 - 10  # Half the page width, minus margins
    row_height = 8
        
    # Add headers
    pdf.cell(col_width, row_height, "Tunnusluku", border=1, align="C")
    pdf.cell(col_width, row_height, "Arvo", border=1, align="C")
    pdf.ln(row_height)
        
    # Add rows
    for key, value in json_data.items():
        pdf.cell(col_width, row_height, library_section_texts[str(key)], border=1, align="L")
        pdf.cell(col_width, row_height, str(value), border=1, align="L")
        pdf.ln(row_height)


def addLibraryStatisticsSection(pdf, library_section_texts, metrics_file):
    addSectionHeader(pdf, "Kirjastotilasto")
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=library_section_texts["statistics_description"], ln=True, align='L')    
    metrics_json_data = readJsonFile(metrics_file) ## readSectionData
    addLibraryMetricsTable(pdf, library_section_texts, metrics_json_data)

def addSectionHeader(pdf, header_text):
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt=header_text, ln=True, align='L')   

# Save PDF
def printPDFToFile(pdf, file_name):
    pdf.output(file_name)


##Aloitetaan tästä
#image_file="library_categories.png"

pdf = createReportObjectWithHeader("Kirjaston kuukausiraportti")
static_texts = readJsonFile("library_section_texts.json")

addLibraryStatisticsSection(pdf, static_texts, "metrics.json")
printPDFToFile(pdf, "report.pdf")
