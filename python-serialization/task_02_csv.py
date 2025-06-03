#!/usr/bin/python3
import csv 
import json

def convert_csv_to_json(CSV_filename):
    # Open the CSV file for reading
    with open(CSV_filename, encoding="utf-8") as f:
        csv_reader = csv.DictReader(f)
        data = list(csv_reader)

    # Open data.json and write JSON data
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

    return True
