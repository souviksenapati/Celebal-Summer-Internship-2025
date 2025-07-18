# House Price Predictor - Streamlit ML App

A simple Streamlit application that uses linear regression to predict house prices based on house size in square feet.

## Features

- **Simple Linear Regression**: Predicts house prices using only the house size
- **Interactive UI**: Adjust house size using a slider to see price predictions
- **Data Visualization**: View the dataset and regression line
- **Model Information**: See the model coefficients and performance metrics

## Setup Instructions

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model**:
   ```bash
   python train_model.py
   ```
   This will create a synthetic dataset and train a linear regression model.

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Access the app**:
   Open your browser and go to `http://localhost:8501`

## How to Use

1. Use the slider to select a house size in square feet
2. Click the "Predict Price" button to see the estimated house price
3. View the calculation breakdown showing base price and size factor
4. Explore the "Data Visualization" tab to see the regression line and data points

## Project Structure

- `app.py`: Main Streamlit application
- `train_model.py`: Script to generate data and train the model
- `house_data.csv`: Generated house price dataset
- `house_price_model.pkl`: Trained linear regression model
- `regression_plot.png`: Visualization of the data and regression line
- `requirements.txt`: Required Python packages