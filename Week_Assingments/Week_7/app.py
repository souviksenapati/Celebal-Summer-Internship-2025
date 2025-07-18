import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import os

# Set page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Load the model
@st.cache_resource
def load_model():
    try:
        model_path = 'house_price_model.pkl'
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Load the dataset
@st.cache_data
def load_data():
    try:
        data_path = 'house_data.csv'
        return pd.read_csv(data_path)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Main function
def main():
    # Header
    st.title("🏠 House Price Predictor")
    st.write("Predict house prices based on size (square feet) using linear regression.")
    
    # Load model and data
    model = load_model()
    data = load_data()
    
    if model is None or data is None:
        return
    
    # Display model information
    st.subheader("Model Information")
    st.write(f"Base Price (Intercept): ₹{model.intercept_:.2f}")
    st.write(f"Price per Square Foot: ₹{model.coef_[0]:.2f}")
    
    # Create tabs
    tab1, tab2 = st.tabs(["Prediction", "Data Visualization"])
    
    with tab1:
        st.subheader("Predict House Price")
        
        # Input for house size
        house_size = st.slider(
            "House Size (square feet)",
            min_value=1000,
            max_value=5000,
            value=2500,
            step=100
        )
        
        # Predict button
        if st.button("Predict Price"):
            # Make prediction
            input_data = pd.DataFrame({'Size_sqft': [house_size]})
            prediction = model.predict(input_data)[0]
            
            # Display prediction
            st.success(f"Predicted House Price: ₹{prediction:,.2f}")
            
            # Show calculation
            st.write("#### Price Calculation:")
            st.write(f"Base Price: ₹{model.intercept_:,.2f}")
            st.write(f"Size Factor: {house_size} sq ft × ₹{model.coef_[0]:.2f}/sq ft = ₹{house_size * model.coef_[0]:,.2f}")
            st.write(f"Total: ₹{model.intercept_ + house_size * model.coef_[0]:,.2f}")
    
    with tab2:
        st.subheader("Data Visualization")
        
        # Show sample data
        st.write("Sample Data (first 5 rows):")
        st.dataframe(data.head())
        
        # Plot regression line
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(data['Size_sqft'], data['Price'], alpha=0.7)
        
        # Generate points for regression line
        line_x = np.array([data['Size_sqft'].min(), data['Size_sqft'].max()])
        line_x = line_x.reshape(-1, 1)
        line_y = model.predict(line_x)
        
        ax.plot(line_x, line_y, color='red', linewidth=2)
        ax.set_xlabel('House Size (square feet)')
        ax.set_ylabel('House Price (₹)')
        ax.set_title('House Price vs Size with Regression Line')
        
        # Display the plot
        st.pyplot(fig)
        
        # Show correlation
        correlation = data.corr().iloc[0, 1]
        st.write(f"Correlation between House Size and Price: {correlation:.4f}")
        
        # Show R-squared
        r_squared = model.score(data[['Size_sqft']], data['Price'])
        st.write(f"R² (coefficient of determination): {r_squared:.4f}")
        st.write("R² indicates how well the model fits the data (1.0 = perfect fit)")

if __name__ == "__main__":
    main()