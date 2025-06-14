import pandas as pd
import numpy as np
import os

class Reader:
    def _get_full_path(self, filename=None):
        base_directory = os.path.join(os.path.dirname(__file__), '..', 'data', 'statistic_data')
        if filename is None:
            return base_directory
        full_path = os.path.join(base_directory, filename)
        return os.path.abspath(full_path)

    def read(self, filename):
        ext = None
        directory = self._get_full_path()
        for f in sorted(os.listdir(directory)):
            file_path = os.path.join(directory, f)
            if os.path.isfile(file_path):
                name_part, ext_part = os.path.splitext(f)
                if name_part == filename:
                    ext = ext_part
                    break
        filename += ext
        
        if ext == '.csv':
            return self.read_csv(filename)
        elif ext == '.xlsx':
            return self.read_xlsx(filename)
        elif ext == '.json':
            return self.read_json(filename)
        elif ext == '.xml':
            return self.read_xml(filename)
        else:
            return self.read_other(filename)
    
    def read_csv(self, filename):
        try:
            full_path = self._get_full_path(filename)
            print(f"READ:{full_path}")
            return pd.read_csv(full_path)
        except Exception as e:
            print(f"Error reading CSV file: {str(e)}")
            return None

    def read_xlsx(self, filename):
        try:
            full_path = self._get_full_path(filename)
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

    def read_json(self, filename):
        try:
            full_path = self._get_full_path(filename)
            df = pd.read_json(full_path, convert_dates=False, dtype=False)
            df = df.replace({np.nan: None})
            return df
        except Exception as e:
            print(f"Error reading JSON file: {str(e)}")
            return None

    def read_xml(self, filename):
        try:
            full_path = self._get_full_path(filename)
            df = pd.read_xml(full_path, dtype={'ID': str})
            df = df.replace({np.nan: None})
        except Exception as e:
            print(f"Error reading XML file: {str(e)}")
            return None

    def read_other(self, filename):
        print(f"Unsupported file type for: {filename}")
        return None