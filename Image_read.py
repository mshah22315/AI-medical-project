import os
from PIL import Image

folder_path = r"C:\Users\sahis\Desktop\projects\Medical\png"

images = []

for file_name in os.listdir(folder_path):
    if file_name.lower().endswith('.png'):
        # Full path to the image file
        file_path = os.path.join(folder_path, file_name)

        # Open the image and add to the list
        images.append(Image.open(file_path))

# Print the number of images loaded
print(f"Loaded {len(images)} PNG images.")