import os
import PyPDF2
from natsort import natsorted

folder = 'files_to_merge'
pdfs = []

for filename in natsorted(os.listdir(folder)):
    if filename.endswith('.pdf'):
        pdfs.append(os.path.join(folder, filename))

merger = PyPDF2.PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("new_merger.pdf")
merger.close()