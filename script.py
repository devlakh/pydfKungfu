import io
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from helpers import getData, createNewTemplate
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

#Get Data from text file and get the length
dataList = getData("data.txt");
dataLen = len(dataList);

# Create a new PDF in Memory
newTemplateStream = createNewTemplate("template.pdf", dataLen);

# Read The PDF in Memory
templateStream = PdfFileReader(newTemplateStream)

# Get The Template Size
pageSize1 = templateStream.pages[0].mediabox[2]
pageSize2 = templateStream.pages[0].mediabox[3]

#Generate PDF Stream
filestream = io.BytesIO()
c = canvas.Canvas(filestream, pagesize=(pageSize1,pageSize2))

#register Custom Font
pdfmetrics.registerFont(TTFont('dgarden', 'fonts/DarkGardenMK.ttf'));

# Attach Data To Canvas
for data in dataList:
    c.setFont('dgarden', 32);
    c.drawCentredString(420, 405, data)
    c.showPage();
c.save();

# PDF FILE FROM SYSTEM
pdfFile = PdfFileWriter()
# PDF FILE IN MEMORY
pdfStream = PdfFileReader(filestream)

# Add The Pages
for i in range(dataLen):
    page = templateStream.getPage(i)
    pdfFile.addPage(page)
    page.mergePage(pdfStream.getPage(i))

# finally, write "pages" to a real file
outputStream = open("output.pdf", "wb")
pdfFile.write(outputStream)
outputStream.close()