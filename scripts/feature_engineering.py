def add_profit_margin(df):
    """Add a profit margin column"""
    df['Profit Margin'] = (df['Amount'] - df['Total Cost']) / df['Amount'] * 100
    return df

def add_discount_column(df):
    """Calculate discount percentage"""
    df['Discount %'] = (df['MRP Old'] - df['Final MRP Old']) / df['MRP Old'] * 100
    return df

def add_price_difference(df):
    """Calculate price differences across platforms"""
    df['Price Difference Amazon'] = df['Amazon MRP'] - df['Final MRP Old']
    df['Price Difference Flipkart'] = df['Flipkart MRP'] - df['Final MRP Old']
    return df

if __name__ == "__main__":
    # Load cleaned data
    cleaned_data = pd.read_csv('../data/cleaned_sales_data.csv')
    
    # Add new features
    data_with_features = add_profit_margin(cleaned_data)
    data_with_features = add_discount_column(data_with_features)
    data_with_features = add_price_difference(data_with_features)
    
    # Save data with features
    data_with_features.to_csv('../data/featured_sales_data.csv', index=False)
