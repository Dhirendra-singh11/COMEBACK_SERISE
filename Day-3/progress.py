from pathlib import Path
import json


File_PATH=Path("progress.json")

def sav_progress(progress,f_p=File_PATH):
    with open(f_p,"w",encoding='utf-8') as file:
        json.dump(progress,file,indent=2)

def load_progress(fp=File_PATH):
    if not fp.exists():
        return {}

    try:
        with open(fp,"r",encoding="utf-8") as file:
            Load_content=json.load(file)
    except json.JSONDecodeError:
        return {}

    if not isinstance(Load_content,dict):
        return {}

    return Load_content


def mark_day_complete(progress,day):

    clean_day=day.strip()

    updated_progress=progress.copy()
    updated_progress[clean_day]=True



    return updated_progress


def completetion_percentage(progress,target_hours):
    if target_hours<1:
        raise ValueError("Target hourse should be non zero positive number")

    total_completion=sum(1 for i in progress.values() if i==True)

    return  (total_completion/target_hours)*100