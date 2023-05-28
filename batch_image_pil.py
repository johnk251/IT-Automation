from PIL import Image

import os

# Specify the source and destination directories
home_path=os.path.expanduser("~")
source_dir =home_path+ '/images'
destination_dir = '/opt/icons/'

# Specify the desired image size and rotation angle
new_size = (128, 128)
rotation_angle = -90  # Negative angle for clockwise rotation

# Iterate over all files in the source directory
for filename in os.listdir(source_dir):
    # Open the image
    try:
        image_path = os.path.join(source_dir, filename)
        image = Image.open(image_path)
    except  Exception:
        pass
    # Convert the image to JPEG format
    if image.format != 'JPEG':
        image = image.convert('RGB')

    # Rotate the image
    rotated_image = image.rotate(rotation_angle, expand=True)

    # Resize the image
    resized_image = rotated_image.resize(new_size)

    # Save the image in the destination directory
    new_filename = f"{filename}"
    save_path = os.path.join(destination_dir, new_filename)
    resized_image.save(save_path, "JPEG")
