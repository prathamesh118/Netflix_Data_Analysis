import pandas as pd

def clean_data(raw_path, cleaned_path):
    df = pd.read_csv(raw_path)

    df.drop_duplicates(inplace=True)

    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    df['country'] = df['country'].fillna('Unknown')
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['rating'] = df['rating'].fillna('Unknown')

    df.to_csv(cleaned_path, index=False)
    print(f"Data cleaned and saved to {cleaned_path}")
    return df
