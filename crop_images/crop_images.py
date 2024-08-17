import os
from PIL import Image

# Set the input and output directories
input_dir = 'images_to_crop/'
output_dir = 'images_cropped/'
left = 0
upper = 25
right = 768
lower = 995

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all the files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is an image
    if not (filename.endswith('jpg') or filename.endswith('png')):
        continue
    # Open the image file
    with Image.open(os.path.join(input_dir, filename)) as im:
        # Crop the image
        cropped_im = im.crop((left, upper, right, lower))

        # Save the cropped image to the output directory
        cropped_im.save(os.path.join(output_dir, filename))