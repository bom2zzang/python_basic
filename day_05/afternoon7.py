#워터마크찍기
import PyPDF2
import sys

pdfFile = open(sys.argv[1],'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('pdf/watermark.pdf','rb'))

pdfFirstPage.mergePage(pdfWatermarkReader.getPage(0))

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(pdfFirstPage)

for pageNum in range(1,pdfReader.numPages):
    pageObj=pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)


pdfOutputFile = open(sys.argv[2],'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFile.close()


print("작업완료")