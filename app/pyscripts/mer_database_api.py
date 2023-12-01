import requests
import json

def update_files(material_id, replace_text, text_to_append, new_material_type):
    GET_ENDPOINT = f'http://127.0.0.1:8090/api/collections/MERdata/records/?filter=(material_id="{material_id}")'
    
    headers = {"Content-Type": "application/json"}
    response = requests.get(GET_ENDPOINT, headers=headers)
    if response.status_code != 200:
        return "Error: Server Response"

    records = response.json()
    if not records or not records['items']:
        return "Error: File doesn't exist in MER database"  # Custom message for non-existent material_id

    record = records['items'][0]
    current_title = record.get('title', '')
    
    if replace_text:
        updated_title = current_title.replace(replace_text, text_to_append)
    else:
        updated_title = current_title + text_to_append
    
    data = {'title': updated_title, 'material_type': new_material_type}
    PATCH_ENDPOINT = f'http://127.0.0.1:8090/api/collections/MERdata/records/{record["id"]}'
    
    response = requests.patch(PATCH_ENDPOINT, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        return "Success"
    else:
        print(response.content.decode())
        return "Error: Update Failed"