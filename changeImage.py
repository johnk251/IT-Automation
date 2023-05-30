#!/usr/bin/env python3
from PIL import Image

import os

# Specify the source and destination directories
home_path=os.path.expanduser("~")
source_dir =home_path+ '/supplier-data/images'

# Specify the desired image size and rotation angle
new_size = (600, 400)


# Iterate over all files in the source directory
for filename in os.listdir(source_dir):
    # Open the image
    
    if filename.endswith('.tiff'):
            image_path = os.path.join(source_dir, filename)
            image = Image.open(image_path)
            # Convert the image to JPEG format
            image = image.convert('RGB')


            # Resize the image
            resized_image = image.resize(new_size)

            # Save the image in the destination directory
            new_filename =filename.replace(".tiff",".jpeg")
            save_path = os.path.join(source_dir, new_filename)
            resized_image.save(save_path, "JPEG")
            print(f"saved image{save_path}")
