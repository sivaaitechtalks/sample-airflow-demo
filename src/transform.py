def clean_data(df):
    df = df.dropna()
    df['name'] = df['name'].str.title()
    return df
