import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_model(df):
    """Train a random forest model to predict sales"""
    X = df[['Size', 'Color', 'Amazon MRP', 'Flipkart MRP']]  # Features
    y = df['Amount']  # Target
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    
    # Return the trained model
    return model

if __name__ == "__main__":
    # Load data with features
    data_with_features = pd.read_csv('../data/featured_sales_data.csv')
    
    # Train predictive model
    model = train_model(data_with_features)
    
    # Save model (optional)
    import joblib
    joblib.dump(model, '../models/sales_forecasting_model.pkl')
