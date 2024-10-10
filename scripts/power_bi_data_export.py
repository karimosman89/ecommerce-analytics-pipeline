def prepare_data_for_power_bi(df):
    """Prepare data for Power BI export"""
    columns_needed = ['SKU Code', 'Category', 'Amount', 'Profit Margin', 'Discount %', 
                      'Price Difference Amazon', 'Price Difference Flipkart', 'Size', 'Color', 'Date']
    df_power_bi = df[columns_needed]
    
    return df_power_bi

if __name__ == "__main__":
    # Load data with features
    data_with_features = pd.read_csv('../data/featured_sales_data.csv')
    
    # Prepare for Power BI
    data_for_power_bi = prepare_data_for_power_bi(data_with_features)
    
    # Export data to CSV
    data_for_power_bi.to_csv('../data/power_bi_export.csv', index=False)
