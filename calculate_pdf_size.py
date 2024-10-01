import os
import math  # Import the math module

def calculate_pdf_size(root_folder):
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(root_folder):
        folder_name = os.path.basename(dirpath)
        pdf_file = folder_name + ".pdf"
        
        # Check if the matching PDF file exists in the folder
        if pdf_file in filenames:
            file_path = os.path.join(dirpath, pdf_file)
            total_size += os.path.getsize(file_path)

    return total_size

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

if __name__ == "__main__":
    root_folder = input("Enter the path to the root folder: ")
    total_size = calculate_pdf_size(root_folder)
    print(f"Total size of PDF files: {convert_size(total_size)}")
