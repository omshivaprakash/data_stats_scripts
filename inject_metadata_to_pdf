import os
import xml.etree.ElementTree as ET
import pikepdf

def inject_metadata_to_pdf(pdf_file, metadata):
    try:
        with pikepdf.open(pdf_file, allow_overwriting_input=True) as pdf:
            # Update the metadata of the PDF
            pdf.docinfo.update(metadata)
            pdf.save(pdf_file)
            print(f"Metadata injected into {pdf_file}")
            return True
    except Exception as e:
        print(f"Error injecting metadata into {pdf_file}: {e}")
        return False

def parse_metadata_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    metadata = {}
    for elem in root:
        metadata[elem.tag] = elem.text  # No leading / in the metadata tag

    return metadata

def process_folders(root_folder):
    subdirectories = []
    pdfs_found = []
    xmls_found = []
    pdfs_injected = []
    missing_pdfs = 0
    missing_xmls = 0

    for dirpath, dirnames, filenames in os.walk(root_folder):
        folder_name = os.path.basename(dirpath)
        subdirectories.append(dirpath)  # Track subdirectories

        # Find the PDF and XML files in the current folder matching the pattern
        pdf_file = None
        xml_file = os.path.join(dirpath, folder_name + "_meta.xml")  # Expecting foldername + _meta.xml

        # Check if the XML file exists
        if os.path.exists(xml_file):
            xmls_found.append(xml_file)
        else:
            print(f"XML metadata file missing in folder: {dirpath}")
            missing_xmls += 1
            continue  # Skip this folder if no metadata file is found

        # Check for PDF that matches the foldername + suffix.pdf
        for file in filenames:
            if file.startswith(folder_name) and file.endswith(".pdf"):
                pdf_file = os.path.join(dirpath, file)
                pdfs_found.append(pdf_file)
                break

        # If both PDF and XML files exist, inject metadata
        if pdf_file:
            metadata = parse_metadata_from_xml(xml_file)
            if inject_metadata_to_pdf(pdf_file, metadata):
                pdfs_injected.append(pdf_file)
        else:
            print(f"PDF file missing for folder: {dirpath}")
            missing_pdfs += 1

    # Output summary
    print("\n--- Summary Report ---")
    print(f"Total subdirectories found: {len(subdirectories)}")
    print(f"Total PDFs found: {len(pdfs_found)}")
    print(f"Total metadata files found: {len(xmls_found)}")
    print(f"Total PDFs injected with metadata: {len(pdfs_injected)}")
    print(f"Missing PDFs: {missing_pdfs}")
    print(f"Missing metadata files: {missing_xmls}")

if __name__ == "__main__":
    root_folder = input("Enter the path to the root folder: ")
    process_folders(root_folder)
