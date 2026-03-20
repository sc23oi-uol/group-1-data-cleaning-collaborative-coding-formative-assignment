import os
import requests
from datetime import datetime

def import_data(url):
    os.makedirs("data", exist_ok=True)
    filename = "data/dataset_M3.txt"
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    return response.text.splitlines()

def clean_data(data_text_list):
    os.makedirs("output", exist_ok=True)
    filename = "output/cleaned_data_M3.txt"
    cleaned_lines = []
    header = data_text_list[0]
    columns = header.split(",")
    time_index = columns.index("time")
    cleaned_lines.append(header)
    for line in data_text_list[1:]:
        parts = line.split(",")
        try:
            raw_time = parts[time_index]
            dt = datetime.strptime(raw_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            parts[time_index] = dt.strftime("%d-%m-%Y %H:%M:%S")
        except:
            pass
        cleaned_lines.append(",".join(parts))
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(cleaned_lines))
    return cleaned_lines

if __name__ == "__main__":
    url = input()
    data = import_data(url)
    clean_data(data)