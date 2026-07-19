import pandas as pd

def run_analysis(cleaned_path):
    df = pd.read_csv(cleaned_path)

    print("\n--- Dataset Overview ---")
    print(f"Total Titles: {len(df)}")
    print(f"Columns: {list(df.columns)}")

    print("\n--- Content Type Distribution ---")
    print(df['type'].value_counts())

    print("\n--- Top 10 Countries ---")
    countries = df['country'].str.split(',').explode().str.strip()
    print(countries.value_counts().head(10))

    print("\n--- Top 10 Genres ---")
    genres = df['listed_in'].str.split(',').explode().str.strip()
    print(genres.value_counts().head(10))

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    return df
