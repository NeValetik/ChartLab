import pandas as pd
import os

class Reader:
    @classmethod
    def read(cls, path):
        # Determines the file type and calls the appropriate read method.
        _, ext = os.path.splitext(path)
        if ext.lower() == '.csv':
            return cls.read_csv(path)
        elif ext.lower() == '.xlsx':
            return cls.read_xlsx(path)
        else:
            return cls.read_other(path)
    
    @classmethod
    def read_csv(cls, path):
        try:
            # Generating abosolute path to the files
            base_directory = os.path.join(os.path.dirname(__file__), '..', 'data', 'statistic_data')
            full_path = os.path.join(base_directory, path)
            full_path = os.path.abspath(full_path)  # Convert to absolute path
            print(full_path)
            return pd.read_csv(full_path)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return None
    
    @classmethod
    def read_xlsx(cls, path):
        try:
            # Generate absolute path using same base directory as CSV
            base_directory = os.path.join(os.path.dirname(__file__), '..', 'data', 'statistic_data')
            full_path = os.path.join(base_directory, path)
            full_path = os.path.abspath(full_path)
            print(f"Loading Excel file from: {full_path}")
            
            # Read Excel with type consistency safeguards
            return pd.read_excel(
                full_path,
                engine='openpyxl',  # Required for xlsx format
                dtype={'ID': str},  # Preserve leading zeros
                parse_dates=True,   # Auto-detect date columns
                keep_default_na=False
            )
        except FileNotFoundError:
            print(f"Excel file not found: {full_path}")
            return None
        except PermissionError:
            print(f"Permission denied for Excel file: {full_path}")
            return None
        except Exception as e:
            print(f"Error reading Excel file: {str(e)}")
            return None

    @classmethod
    def read_other(cls, path):
        print(f"Unsupported file type for: {path}")
        return []
    
