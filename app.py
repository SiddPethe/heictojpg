import os
import logging
from PIL import Image
from pillow_heif import register_heif_opener # HEIC Converter
import shutil # High Level File operations
from tqdm import tqdm # Progress Bar for loops


def convert_to_jpg(heic_path, jpg_path):
    """Convert each heic file to jpg.

    Args:
        heic_path (str): Path to HEIC File
        jpg_path (str): Path of the converted JPG Image
    """
    try:
        with Image.open(heic_path) as img:
            exif_data = img.info.get("exif")
            # img.convert = ("RGB")
            img.save(jpg_path,"JPEG",quality=95,exif=exif_data)
            print(f"File {heic_path} converted to {jpg_path}")
    except:
        logging.error(F"Error in Converting File: {heic_path}")

def prepare(heic_dir):
    """Prepare target directory and files for conversion

    Args:
        heic_dir (str): Path to the HEIC files to be converted.
    """
    register_heif_opener()

    # Check if dir(path) with HEIC photos exits.
    if not os.path.isdir(heic_dir):
        logging.error(f"Directory with HEIC folder {heic_dir} not found.")
        return

    # Get all HEIC files in dir.
    heic_files = [file for file in os.listdir(heic_dir) if file.lower().endswith(".heic")]
    total_files = len(heic_files)
    if total_files == 0:
        print(f"No HEIC files found in {heic_dir} to convert. ")
        return

    # Create dir to store jpg files.
    jpgs_dir = os.path.join(heic_dir,"ConvertedFiles")
    if os.path.exists(jpgs_dir):
        user_input = input("File named 'ConvertedFiles' already exists. Delete and continue? (y / n):  ")
        if user_input.lower() != 'y':
            print("Conversion aborted !")
            return
        else:
            shutil.rmtree(jpgs_dir)
    os.makedirs(jpgs_dir)

    # Create task list to convert
    tasks = []
    for file_name in heic_files:
        heic_path = os.path.join(heic_dir, file_name)
        jpg_path = os.path.join(jpgs_dir, os.path.splitext(file_name)[0] + ".jpg")

        tasks.append((heic_path,jpg_path))

    for task in tqdm(tasks):
        convert_to_jpg(task[0], task[1])
    

def main():
    """
    Main Function executes
    """
    heic_dir = input("Enter path to Directory with HEIC files to convert: ")
    prepare(heic_dir)

if __name__ == "__main__":
    main()