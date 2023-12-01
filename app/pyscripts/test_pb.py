import pandas as pd
import requests
import json

def create_material(material_id, title, material_type):
    # Construct the endpoint URL for creating a new record
    POST_ENDPOINT = 'http://127.0.0.1:8090/api/collections/MERdata/records/'

    headers = {"Content-Type": "application/json"}

    # Data to create a new record
    data = {
        'material_id': material_id,
        'title': title,
        'material_type': material_type
    }

    # Step 1: POST request to create a new record
    response = requests.post(POST_ENDPOINT, data=json.dumps(data), headers=headers)

    if response.status_code == 201:
        return True
    else:
        # Print the response content to see if there's an error message
        print(response.content.decode())
        return False



def read_and_process_excel(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        material_id = row['material_id']
        title = row['title']
        material_type = row['material_type']

        # Call the create_material function with the row data
        success = create_material(material_id, title, material_type)
        if not success:
            print(f"Failed to create material for row {index}")

# Example usage
file_path = 'D:\\Applicatie_cache\\meirem\\OneDrive - VRT\\Desktop\\script\\mer-app\\app\\pyscripts\\vullingenDEC23WP - kopie.xlsx'
read_and_process_excel(file_path)
































