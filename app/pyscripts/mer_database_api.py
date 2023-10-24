import requests
import json

def update_files(material_id, text_to_append, new_material_type):
    # Construct the endpoint URL using the material_id for filtering
    GET_ENDPOINT = f'http://127.0.0.1:8090/api/collections/MERdata/records/?filter=(material_id="{material_id}")'
    
    headers = {"Content-Type": "application/json"}

    # Step 1: GET request to retrieve the current title using the filter
    response = requests.get(GET_ENDPOINT, headers=headers)
    if response.status_code != 200:
        return False
    
    records = response.json()
    if not records or not records['items']:
        return False
    
    record = records['items'][0]  # Accessing the record correctly
    current_title = record.get('title', '')
    updated_title = current_title + text_to_append
    
    # Data to update
    data = {
        'title': updated_title,
        'material_type': new_material_type
    }

    # Construct the PATCH endpoint URL using the record's ID
    PATCH_ENDPOINT = f'http://127.0.0.1:8090/api/collections/MERdata/records/{record["id"]}'
    
    # Step 2: PATCH request to update the title and material_type
    response = requests.patch(PATCH_ENDPOINT, data=json.dumps(data), headers=headers)
    
    if response.status_code == 200:
        return True
    else:
        # Print the response content to see if there's an error message
        print(response.content.decode())
        return False

# Sample usage:

# items_to_update = [
#     {'material_id': 'WP18377382', 'text_to_append': ' - Appended Text 1', 'new_material_type': 'PROGRAMME'},
#     {'material_id': 'WP81352419', 'text_to_append': ' - Appended Text 2', 'new_material_type': 'LIVE RECORD'},
#     {'material_id': 'WP63731518', 'text_to_append': ' - Appended Text 3', 'new_material_type': 'JUNCTION'},
#     # ... more items
# ]

# for item in items_to_update:
#     success = update_files(item['material_id'], item['text_to_append'], item['new_material_type'])
#     if success:
#         print(f"Successfully updated record with material_id: {item['material_id']}")
#     else:
#         print(f"Failed to update record with material_id: {item['material_id']}")
