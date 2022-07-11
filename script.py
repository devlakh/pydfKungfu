from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas

# Read Data File
dataList = [];
dataLen = 0;
with open("data.txt") as f:
    dataList = f.read().splitlines() 

dataLen = len(dataList);

# read your existing PDF
template = PdfFileReader(open("cert.pdf", "rb"))
pageSize1 = template.pages[0].mediabox[2]
pageSize2 = template.pages[0].mediabox[3]

filestream = io.BytesIO()
c = canvas.Canvas(filestream, pagesize=(pageSize1,pageSize2))

c.drawCentredString(420, 297, "")
c.save();

pages = PdfFileWriter()

# create a new PDF with Reportlab
# new_pdf = PdfFileReader(filestream)

# add the "watermark" (which is the new pdf) on the existing page
page = template.getPage(0)
pages.addPage(page)
pages.addPage(page)
pages.addPage(page)
# page.mergePage(new_pdf.getPage(0))


# finally, write "pages" to a real file
outputStream = open("pages.pdf", "wb")
pages.write(outputStream)
outputStream.close()

print("\n\nPDF DONE");