import pandas as pd
from src.transform import clean_data

def test_clean_data():
    df = pd.DataFrame({"name": ["siva", None, "babu"]})
    cleaned = clean_data(df)
    assert cleaned.shape[0] == 2
    assert cleaned["name"].iloc[0] == "Siva"
