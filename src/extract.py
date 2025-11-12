import pandas as pd
from io import StringIO

def extract_from_s3():
    data = {"names": ["Alice", "Bob", "Charlie"], "ages": [25, 30, 35]}
    return pd.DataFrame(data)