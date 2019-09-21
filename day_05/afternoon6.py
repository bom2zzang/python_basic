#파일합치기
import PyPDF2
import sys

pdf1File = open(sys.argv[1],'rb')
pdf2File = open(sys.argv[2],'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open(sys.argv[3],'wb')

pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()

pdf1File.close()
pdf2File.close()

print("작업완료")