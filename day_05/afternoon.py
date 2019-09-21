import PyPDF2

pdfFileObj = open('pdf/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
pageObj.extractText()
print(pageObj.extractText())