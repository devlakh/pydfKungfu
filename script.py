import io
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from helpers import getData, createNewTemplate

dataList = getData("data.txt");
dataLen = len(dataList);
newTemplateStream = createNewTemplate("template.pdf", dataLen);

# read your existing PDF
template = PdfFileReader(newTemplateStream)
pageSize1 = template.pages[0].mediabox[2]
pageSize2 = template.pages[0].mediabox[3]

#Generate PDF Stream
filestream = io.BytesIO()
c = canvas.Canvas(filestream, pagesize=(pageSize1,pageSize2))

for data in dataList:
    c.drawCentredString(420, 297, data)
    c.showPage();
c.save();

# PDF FILE FROM SYSTEM
pdfFile = PdfFileWriter()

# PDF FILE IN MEMORY
pdfStream = PdfFileReader(filestream)

# add the "watermark" (which is the new pdf) on the existing page

for i in range(dataLen):
    page = template.getPage(i)
    pdfFile.addPage(page)
    page.mergePage(pdfStream.getPage(i))

# finally, write "pages" to a real file
outputStream = open("output.pdf", "wb")
pdfFile.write(outputStream)
outputStream.close()

print("PDF DONE");