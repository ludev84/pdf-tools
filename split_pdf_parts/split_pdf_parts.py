from PyPDF2 import PdfReader, PdfWriter
import os


def split_pdf_into_parts(
    pdf_path, n_parts, output_folder="split_pdf_parts/split_files"
):
    # Load the PDF
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    pages_per_part = total_pages // n_parts
    remainder = total_pages % n_parts

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    start = 0
    for i in range(n_parts):
        writer = PdfWriter()

        # Calculate end page (distribute the remainder to last part)
        end = start + pages_per_part + (1 if i < remainder else 0)

        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])

        output_path = os.path.join(output_folder, f"part_{i+1}.pdf")
        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"Saved: {output_path} ({end - start} pages)")
        start = end

    print("Splitting complete.")


# Example usage
if __name__ == "__main__":
    split_pdf_into_parts("split_pdf_parts/input.pdf", n_parts=2)
