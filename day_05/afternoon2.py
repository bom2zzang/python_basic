import PyPDF2
import re

pdfFileObj = open('pdf/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)

text = str(pageObj.extractText())
quotes = re.findall(r'"[^"]*"', text)
for quote in quotes:
    print(quote)
    print()


    #이거 안됨 뭐야 ..