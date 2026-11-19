import json
from pathlib import Path

file_name=Path("excerise.json")

def save_contacts(contacts,file=file_name):
    with open(file,'w',encoding='utf-8') as f:
        json.dump(contacts,f,indent=3)



def load_contacts(file_n=file_name):

    try:
        with open(file_n,'r',encoding='utf-8') as file:
            extracted_contacts=json.load(file)
    except json.JSONDecodeError:
            return {}
    if not extracted_contacts:
        return {}

    if isinstance(extracted_contacts,dict):
        return {}
    return extracted_contacts


contacts=[
    {"name":"Asha",
     "PHONE":"123454323"
    },
    {
        "name":"Gajendra",
        "PHONE":"91564433"
    }
           ]
save_contacts(contacts)

print(load_contacts())