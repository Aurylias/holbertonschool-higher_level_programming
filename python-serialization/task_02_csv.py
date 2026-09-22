"""Module to convert CSV to JSON"""
import csv
import json

def convert_csv_to_json(filename):
    """Take a CSV file and write it's content in a JSON file"""
    try:
        with open(filename, "r") as csvFile:
            content = csv.DictReader(csvFile)
            data = list(content)
    except Exception:
        return False

    with open("data.json", "w") as jsonFile:
        try:
            json.dump(data, jsonFile)
            return True
        except Exception:
            return False
