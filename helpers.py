import io
from PyPDF2 import PdfFileWriter, PdfFileReader

def getData(_file):
    with open(_file) as f:
        dataList = f.read().splitlines() 

    return dataList;

def createNewTemplate(_file, _length):
    template = PdfFileReader(open("template.pdf", "rb"));
    pages = PdfFileWriter();
    page = template.getPage(0);
    for x in range(_length):
        pages.addPage(page)

    filestream = io.BytesIO()
    pages.write(filestream)
    return filestream;

if __name__ == "__main__":
   pass