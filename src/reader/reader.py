import csv
import os

class Reader:
    @classmethod
    def read(cls, path):
        #Determines the file type and calls the appropriate read method.
        _, ext = os.path.splitext(path)
        if ext.lower() == '.csv':
            return cls.read_csv(path)
        else:
            return cls.read_other(path)
    
    @classmethod
    def read_csv(cls, path):
        try:
            with open(path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return []

    @classmethod
    def read_other(cls, path):
        print(f"Unsupported file type for: {path}")
        return []
    
