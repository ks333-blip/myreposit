import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, "r") as f:
        data = json.load(f)

    if len(data) == 0:
        print("JSON file is empty!")
        return

    columns = data[1].keys()

    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)

    print("Converted successfully!")
if __name__ == "__main__":
    json_to_csv("input.json", "output.csv")
