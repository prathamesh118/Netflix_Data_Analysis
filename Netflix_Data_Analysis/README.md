# Netflix Data Analysis

A comprehensive data analysis project exploring Netflix's content catalog.

## Project Structure

```
Netflix_Data_Analysis/
├── data/
│   ├── raw/
│   │   └── netflix_titles.csv
│   └── processed/
│       └── netflix_titles_cleaned.csv
├── notebooks/
│   └── netflix_analysis.ipynb
├── scripts/
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   ├── visualization.py
│   └── utils.py
├── output/
│   ├── charts/
│   └── report.pdf
├── reports/
│   ├── project_report.docx
│   └── project_presentation.pptx
├── requirements.txt
├── main.py
└── .gitignore
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Place your raw data in `data/raw/netflix_titles.csv`

3. Run the pipeline:
   ```bash
   python main.py
   ```

## Features

- Data cleaning and preprocessing
- Exploratory data analysis
- Visualizations (bar charts, line plots, heatmaps)
- Content type distribution analysis
- Country, genre, and rating analysis
