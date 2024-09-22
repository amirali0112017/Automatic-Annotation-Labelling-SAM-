import os
import shutil

image_folder = r'E:\Amir\EWTracker\new_EW_dataset'
txt_folder = r'E:\Amir\EWTracker\segmented_txt_files'
output_folder = r'E:\Amir\EWTracker\remaining_images'

# Get the list of image files in the image folder
image_files = os.listdir(image_folder)

# Loop through each image file
for image_file in image_files:
    # Extract the image name without extension
    image_name = os.path.splitext(image_file)[0]
    
    # Construct the path to the corresponding text file
    txt_file = os.path.join(txt_folder, image_name + '.txt')
    
    # Check if the text file exists
    if os.path.exists(txt_file):
        # Copy the image to the output folder
        image_path = os.path.join(image_folder, image_file)
        output_path = os.path.join(output_folder, image_file)
        shutil.copy2(image_path, output_path)
