from PyPDF2 import PdfWriter, PdfReader

# Open the input PDF file
with open("input.pdf", "rb") as in_f:
    input_pdf = PdfReader(in_f)
    num_pages = len(input_pdf.pages)

    # Create a new PDF writer
    output_pdf = PdfWriter()

    # Define the cropping dimensions (adjust as needed). (0, 0) is at the bottom left of the PDF page
    x, y, w, h = 80, 140, 460, 650

    # Crop each page
    for i in range(num_pages):
        page = input_pdf.pages[i]
        page.cropbox.upper_left = (x, y)
        page.cropbox.lower_right = (x + w, y + h)
        output_pdf.add_page(page)

    # Save the cropped PDF to a new file
    with open("output.pdf", "wb") as out_f:
        output_pdf.write(out_f)

print(f"Cropped {num_pages} pages and saved to output.pdf")
