from PyPDF2 import PdfWriter, PdfReader

def split_pdf_to_pages(filename):
    pdf_reader = PdfReader(open(filename, "rb"))
    for page in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page])
        output_filename = f"{filename.split('.')[0]}_page{page+1}.pdf"
        with open('split_files/'+output_filename, 'wb') as out:
            pdf_writer.write(out)

# from PyPDF2 import PdfFileWriter, PdfFileReader
# DEPRECATED
# def split_pdf_to_pages(filename):
#     pdf_reader = PdfFileReader(open(filename, "rb"))
#     for page in range(pdf_reader.getNumPages()):
#         pdf_writer = PdfFileWriter()
#         pdf_writer.addPage(pdf_reader.getPage(page))
#         output_filename = f"{filename.split('.')[0]}_page{page+1}.pdf"
#         with open(output_filename, 'wb') as out:
#             pdf_writer.write(out)

split_pdf_to_pages('input.pdf')