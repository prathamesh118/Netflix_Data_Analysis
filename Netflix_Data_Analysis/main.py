import os
from scripts.data_cleaning import clean_data
from scripts.exploratory_analysis import run_analysis
from scripts.visualization import generate_charts

def main():
    raw_path = "data/raw/netflix_titles.csv"
    cleaned_path = "data/processed/netflix_titles_cleaned.csv"

    print("Starting Netflix Data Analysis Pipeline...")

    print("Step 1: Cleaning data...")
    clean_data(raw_path, cleaned_path)

    print("Step 2: Running exploratory analysis...")
    run_analysis(cleaned_path)

    print("Step 3: Generating visualizations...")
    generate_charts(cleaned_path)

    print("Pipeline complete. Check output/ folder for results.")

if __name__ == "__main__":
    main()
