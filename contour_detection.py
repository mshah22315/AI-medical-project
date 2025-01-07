import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from Image_read import image_read  # Assuming this function loads images into the list

# Folder containing input images
folder_path = r"C:\Users\sahis\Desktop\projects\Medical\png\filtered_images"

# List to store images
images = []

# Read images into the list
image_read(folder_path, images)

# Define the output folder for contoured images
output_folder = os.path.join(folder_path, "contoured_images")
os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist

# Define thresholds for medium gray
low_threshold = 100
high_threshold = 150

# Process each image
for file_name in os.listdir(folder_path):
    if file_name.lower().endswith('.png'):
        # Read the image
        image_path = os.path.join(folder_path, file_name)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        if image is None:
            print(f"Error: Could not load image {file_name}")
            continue

        # Apply Gaussian Blur to reduce noise
        blurred = cv2.GaussianBlur(image, (5, 5), 0)

        # Threshold the image
        _, binary = cv2.threshold(blurred, 100, 300, 0,  cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Create an empty image to draw contours
        contour_image = np.zeros_like(image)

        # Draw contours
        for contour in contours:
            # Filter by size (e.g., area > 100 pixels)
            if cv2.contourArea(contour) > 100 and cv2.contourArea(contour) < 5000:
                cv2.drawContours(contour_image, [contour], -1, 255, 1)  # Use 255 for white lines
                
       
        
        # Save the contoured image to the output folder
        output_path = os.path.join(output_folder, f"contoured_{file_name}")
        cv2.imwrite(output_path, contour_image)

        # Optional: Display the results
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 3, 1), plt.title("Original Image"), plt.imshow(image, cmap='gray')
        plt.subplot(1, 3, 2), plt.title("Binary Image"), plt.imshow(binary, cmap='gray')
        plt.subplot(1, 3, 3), plt.title("Detected Contours"), plt.imshow(contour_image, cmap='gray')
        plt.show()

