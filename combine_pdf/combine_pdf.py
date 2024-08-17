"""This module merge multiple PDF files into one."""

from pathlib import Path
import os
import PyPDF2
from natsort import natsorted

dirFiles = 'files_to_merge'
dirFilesLen = len([name for name in os.scandir(dirFiles) if os.path.isfile(name)])
pdfWriter = PyPDF2.PdfWriter()
files = {}
dirObj = natsorted(os.scandir(dirFiles), key=lambda e: e.name)

for archivo, iterator in zip(dirObj, range(0, dirFilesLen)):
    p = Path(archivo)
    if p.suffix != '.pdf':
        continue
    # print(p)
    pdfFile = f'pdfFile_{iterator}'
    files[pdfFile] = open(p, 'rb')
    pdfReader = PyPDF2.PdfReader(files[pdfFile])
    for pageNum in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)

pdfOutputFile = open('combine_pdf.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()

# Cerrar archivos pdf
for a in files:
    files[a].close()
    print(files[a].name)
    print(a)