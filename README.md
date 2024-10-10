## E-commerce Analytics Pipeline

This repository contains a complete ETL pipeline and Power BI dashboard for analyzing e-commerce profitability across platforms such as Shiprocket, INCREFF, and Amazon.

## Structure

- `data/`: Raw CSV files for analysis.
- `scripts/`: Python scripts for ETL, data cleaning, feature engineering, predictive modeling, and exporting for Power BI.
- `notebooks/`: Jupyter Notebooks for exploratory data analysis and profitability modeling.
- `powerbi/`: Power BI `.pbix` file with the dashboard.
- `requirements.txt`: Python dependencies.

## How to Run

1. Clone the repo:


        git clone https://github.com/username/ecommerce-analytics-pipeline.git


1. Install dependencies:


       pip install -r requirements.txt



2. Run the ETL Pipeline:


       python scripts/etl_pipeline.py



3. Run the feature engineering:


        python scripts/feature_engineering.py



4. Export the final dataset for Power BI:


         python scripts/power_bi_data_export.py
    
   

5. Open `powerbi/Ecommerce_Analytics_Dashboard.pbix` in Power BI to view the dashboard.
   
