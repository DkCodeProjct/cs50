#fpdf Library/Code. Learn how to implement librarys....// That'sIt

from fpdf import FPDF

pdf = FPDF()

pdf.add_page(orientation='portrait', format='a4')
pdf.image("./shirtificate.png", 10,70,190)
pdf.set_font("helvetica",'', size=48)
pdf.set_text_color(0,0,0)
pdf.cell(0, 57, 'Shirtficate', align='c')
pdf.ln(20)

pdf.set_font("helvetica", size=24)
pdf.set_text_color(0,0,0)
pdf.cell(0,213, f' {input("name")} took cs50', align='c')

pdf.output('shirtificate1.pdf')