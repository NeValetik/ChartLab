import pandas as pd
import os

class Reader:
    def _get_full_path(cls, path):
        base_directory = os.path.join(os.path.dirname(__file__), '..', 'data', 'statistic_data')
        full_path = os.path.join(base_directory, path)
        return os.path.abspath(full_path)

    def read(cls, path):
        _, ext = os.path.splitext(path)
        ext = ext.lower()
        
        if ext == '.csv':
            return cls.read_csv(path)
        elif ext == '.xlsx':
            return cls.read_xlsx(path)
        elif ext == '.json':
            return cls.read_json(path)
        elif ext == '.xml':
            return cls.read_xml(path)
        else:
            return cls.read_other(path)
    
    def read_csv(cls, path):
        try:
            full_path = cls._get_full_path(path)
            print(full_path)
            return pd.read_csv(full_path)
        except Exception as e:
            print(f"Error reading CSV file: {str(e)}")
            return None

    def read_xlsx(cls, path):
        try:
            full_path = cls._get_full_path(path)
            print(f"Loading Excel file from: {full_path}")
            return pd.read_excel(
                full_path,
                engine='openpyxl',
                dtype={'ID': str},
                parse_dates=True,
                keep_default_na=False
            )
        except Exception as e:
            print(f"Error reading Excel file: {str(e)}")
            return None

    def read_json(cls, path):
        try:
            full_path = cls._get_full_path(path)
            print(f"Loading JSON file from: {full_path}")
            return pd.read_json(full_path)
        except Exception as e:
            print(f"Error reading JSON file: {str(e)}")
            return None

    def read_xml(cls, path):
        try:
            full_path = cls._get_full_path(path)
            print(f"Loading XML file from: {full_path}")
            return pd.read_xml(full_path)
        except Exception as e:
            print(f"Error reading XML file: {str(e)}")
            return None

    def read_other(cls, path):
        print(f"Unsupported file type for: {path}")
        return None