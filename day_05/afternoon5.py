import PyPDF2
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]


pdfFile = open(sys.argv[1],'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

page = pdfReader.getPage(0)
page.rotateClockwise(90)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)

resultPdfFile = open(sys.argv[2], 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
