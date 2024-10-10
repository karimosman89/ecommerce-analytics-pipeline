import pandas as pd

def load_data(file_path):
    """Load CSV data from file_path"""
    return pd.read_csv(file_path)

def merge_data(df1, df2, merge_col):
    """Merge two DataFrames on a specific column"""
    return pd.merge(df1, df2, on=merge_col, how='left')

if __name__ == "__main__":
    # Example of loading data
    cloud_data = load_data('../data/Cloud_Warehouse_Compersion_Chart.csv')
    sales_data = load_data('../data/Sale_Report.csv')
    
    # Merging data
    merged_data = merge_data(cloud_data, sales_data, 'SKU Code')
    
    # Save merged data
    merged_data.to_csv('../data/merged_sales_data.csv', index=False)
