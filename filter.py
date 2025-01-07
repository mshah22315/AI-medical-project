import os
from PIL import Image
import numpy as np
from Image_read import images

# Define the folder containing the images
folder_path = r"C:\Users\sahis\Desktop\projects\Medical\png"

# Define the output folder for filtered images
output_folder = os.path.join(folder_path, "filtered_images")
os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist

# Define thresholds for medium gray
low_threshold = 100  # Lower bound for medium gray
high_threshold = 150  # Upper bound for medium gray

# Process each image
for file_name in os.listdir(folder_path):
    if file_name.lower().endswith('.png'):
        # Full path to the image file
        file_path = os.path.join(folder_path, file_name)

        # Open the image and convert to grayscale
        image = Image.open(file_path).convert('L')  # Convert to grayscale
        image_array = np.array(image)

        # Create a mask for medium gray pixels
        medium_gray_mask = (image_array >= low_threshold) & (image_array <= high_threshold)

        # Apply the mask: retain medium gray pixels, set others to black
        filtered_image_array = np.zeros_like(image_array)  # Start with a black image
        filtered_image_array[medium_gray_mask] = image_array[medium_gray_mask]

        # Convert the filtered array back to an image
        filtered_image = Image.fromarray(filtered_image_array)

        # Save the filtered image
        output_file_path = os.path.join(output_folder, f"filtered_{file_name}")
        filtered_image.save(output_file_path)

# Print a message indicating completion
print(f"Filtered images saved to: {output_folder}")
