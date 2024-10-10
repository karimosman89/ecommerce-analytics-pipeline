import pandas as pd

def clean_data(df):
    """Basic data cleaning steps"""
    # Remove rows with missing SKU Code
    df = df.dropna(subset=['SKU Code'])
    
    # Convert dates to datetime
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    
    # Fill missing numeric values with 0
    df.fillna(0, inplace=True)
    
    return df

if __name__ == "__main__":
    # Load merged data
    merged_data = pd.read_csv('../data/merged_sales_data.csv')
    
    # Clean data
    cleaned_data = clean_data(merged_data)
    
    # Save cleaned data
    cleaned_data.to_csv('../data/cleaned_sales_data.csv', index=False)
