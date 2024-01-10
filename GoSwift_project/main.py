# main.py

import csv
from dataset import data
from config import columns_to_keep

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class JsonToCsvConverter(metaclass=SingletonMeta):
    def __init__(self, data, columns_to_keep):
        if not isinstance(data, dict):
            raise ValueError("Data should be a dictionary.")
        if not isinstance(columns_to_keep, list):
            raise ValueError("Columns to keep should be a list.")
        self.data = data
        self.columns_to_keep = columns_to_keep

    def flatten_json(self):
        self.flattened_data = {key: self.data[key] for key in self.columns_to_keep if key in self.data}

    def save_to_csv(self, filename):
        if not filename.endswith('.csv'):
            print("Filename should end with .csv")
            return
        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.columns_to_keep)
                writer.writeheader()
                writer.writerow(self.flattened_data)
        except Exception as e:
            print(f"Error in saving data to CSV: {e}")

# Usage
try:
    converter = JsonToCsvConverter(data, columns_to_keep)
    print("JsonToCsvConverter instantiated successfully.")
    converter.flatten_json()
    print("JSON flattened successfully.")
    converter.save_to_csv('output.csv')
    print("Data saved to CSV successfully.")
except ValueError as e:
    print(e)