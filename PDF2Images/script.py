"""
Only got it to work on Colab. Run these commands before:
!pip install pdf2image
!sudo apt install poppler-utils

Use this to zip the files and then download them with the GUI:
!zip -r /content/file.zip /content/pdf_images
"""

from pdf2image import convert_from_path
import os


def pdf_to_images(pdf_path, output_folder="pdf_images", dpi=300):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Convert PDF pages to images
    images = convert_from_path(pdf_path, dpi=dpi)

    # Save each image
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i+1}.png")
        image.save(image_path, "PNG")
        print(f"Saved: {image_path}")

    print(f"Total pages converted: {len(images)}")


# Example usage
if __name__ == "__main__":
    pdf_file = "input.pdf"  # Replace with your PDF file path
    pdf_to_images(pdf_file)
