import os
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import pandas as pd

from ..config import UPLOAD_FOLDER


def extract_wp00_from_excel(file: FileStorage) -> str:
    # Ensure filename is a string
    filename = str(file.filename)
    
    # Create a temporary file path
    file_path = os.path.join(UPLOAD_FOLDER, secure_filename(filename))
    file.save(file_path)

    # Read the Excel file
    df = pd.read_excel(file_path, engine='openpyxl')
    
    # Extract all text that starts with "WP00" from the dataframe and remove spaces
    wp00_texts = []
    for column in df.columns:
        for cell in df[column]:
            if isinstance(cell, str) and cell.startswith("WP00"):
                cleaned_text = cell.replace(" ", "").strip()
                wp00_texts.append(cleaned_text)

    # Create a new dataframe with the extracted texts
    output_df = pd.DataFrame(wp00_texts)

    # Define the output file path
    output_filename = "vullingenWPList.xlsx"
    output_filepath = os.path.join(UPLOAD_FOLDER, output_filename)
    
    # Save the new dataframe to the new Excel file
    output_df.to_excel(output_filepath, index=False, header=False, engine='openpyxl')
    
    return output_filename  # return the name of the created file
