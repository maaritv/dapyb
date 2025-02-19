from fpdf import FPDF
import json


left_and_right_margin=15
top_and_bottom_margin=30
paragraph_font_size=12
header_font_size=16
font='Arial'
imagePath="./images/"

def readJsonFile(json_file_name):
    with open(json_file_name, 'r') as file:
        data = json.load(file)
    return data

def createReportObjectWithHeader(report_header):
    pdf = FPDF()
    pdf.add_page()

    # Add text
    pdf.set_font(font, size=12)
    pdf.set_margins(left_and_right_margin, top_and_bottom_margin, left_and_right_margin)  #vasen, ylä ja oikea
    pdf.set_auto_page_break(True, top_and_bottom_margin) #Käytä alamarginaalia 30
    pdf.cell(200, 10, txt=report_header, ln=True, align='L')
    return pdf

def addLibraryMetricsTable(pdf, library_section_texts, json_data):
    pdf.set_font(font, size=12)
    pdf.cell(200, 10, txt=library_section_texts["late_books"], ln=True, align='L')    
    pdf.cell(200, 10, txt=library_section_texts["lost_books"], ln=True, align='L') 

    # Set font for the table
    pdf.set_font(font, size=10)
    col_width = pdf.w / 2 - (left_and_right_margin*2)  # Half the page width, minus margins
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


def addLibraryStatisticsSection(pdf, title, library_section_texts, metrics_file):
    addSectionHeader(pdf, title)
    pdf.set_font(font, size=paragraph_font_size)
    pdf.cell(200, 10, txt=library_section_texts["statistics_description"], ln=True, align='L')    
    metrics_json_data = readJsonFile(metrics_file) ## readSectionData
    addLibraryMetricsTable(pdf, library_section_texts, metrics_json_data)

def addTextSectionWithImage(pdf, title, content, imageName=None, image_text=None):
    paragraph_line_height=7
    pdf.ln(paragraph_line_height)
    addSectionHeader(pdf, title)
    pdf.set_font(font, size=paragraph_font_size)
    pdf.multi_cell(0, paragraph_line_height, txt=content, align='L')   
    if (imageName):
       pdf.ln(paragraph_line_height)
       #https://pyfpdf.readthedocs.io/en/latest/reference/image/index.html
       image_width=(pdf.w-left_and_right_margin*2)*0.80
       pdf.image(imagePath+imageName, w=image_width, x=(pdf.w-image_width)/2)
       if (image_text):
           pdf.ln(paragraph_line_height/2)
           pdf.set_font(font, size=paragraph_font_size-2)
           pdf.cell(200, paragraph_line_height, txt=image_text, ln=True, align='C')    

def addSectionHeader(pdf, header_text):
    pdf.set_font(font, style="B", size=header_font_size)
    pdf.cell(200, 10, txt=header_text, ln=True, align='L')   

# Save PDF
def printPDFToFile(pdf, file_name):
    pdf.output(file_name)


##Aloitetaan tästä

pdf = createReportObjectWithHeader("Kirjaston vuosiraportti 2024")
static_texts = readJsonFile("library_section_texts.json")
addLibraryStatisticsSection(pdf, static_texts["title_statistics_table"], static_texts, "metrics.json")
addTextSectionWithImage(pdf, static_texts["title_loan_amounts"], static_texts["chapter_loan_amounts"], "lainaukset_sb.png", static_texts["image_loan_amounts"])
addTextSectionWithImage(pdf, static_texts["title_best_categories"], static_texts["chapter_best_categories"], "kategoriat.png", static_texts["image_best_categories"]) 
addTextSectionWithImage(pdf, static_texts["title_data_source_description"], static_texts["chapter_data_source_description"])
addTextSectionWithImage(pdf, static_texts["title_preprocessing_description"], static_texts["chapter_preprocessing_description"])
addTextSectionWithImage(pdf, static_texts["title_data_source_errors_and_uncertainty"], static_texts["chapter_data_source_errors_and_uncertainty"])
addTextSectionWithImage(pdf, static_texts["results_explained"], static_texts["chapter_results_explained"])
printPDFToFile(pdf, "report.pdf")
