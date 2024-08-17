import PyPDF2

pdfFileObj = open('archivo.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print('Number of pages: ', pdfReader.numPages)

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

pdfFileObj.close()