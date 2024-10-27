import streamlit as st
import pandas as pd
from PIL import Image

# Load dataset
df = pd.read_csv('pics/nvda (3).csv')

# Display title
st.title("Stock Market Prediction")

# Show the first few rows of the dataset
st.subheader("Dataset Preview")
st.write(df.head())  # Displays the first few rows of the dataset

# Stock selection options with multiple images per stock
stock_images = {
    'Tesla (TSLA)': [
        'pics/tsla1.png',
        'pics/tsla2.png',
        'pics/tsla3.png',
        'pics/tsla4.png',
        'pics/tsla5.png'
    ],
    'Microsoft (MSFT)': [
        'pics/msft1.png',
        'pics/msft2.png',
        'pics/msft3.png',
        'pics/msft4.png',
        'pics/msft5.png'
    ],
    'NVIDIA (NVDA)': [
        'pics/nvda1.png',
        'pics/nvda2.png',
        'pics/nvda3.png',
        'pics/nvda4.png',
        'pics/nvda5.png'
    ],
    'Google (GOOGL)': [
        'pics/goog1.png',
        'pics/goog2.png',
        'pics/goog3.png',
        'pics/goog4.png',
        'pics/goog5.png'
    ]
}

# Dropdown menu for stock selection
stock_choice = st.selectbox("Select a stock to view predictions:", list(stock_images.keys()))

# Dropdown for specific image selection
image_options = [f"{stock_choice} Prediction {i+1}" for i in range(5)]
image_choice = st.selectbox("Select prediction image:", image_options)

# Display the selected image
selected_image_path = stock_images[stock_choice][image_options.index(image_choice)]
selected_image = Image.open(selected_image_path)
st.subheader(f"{image_choice} for {stock_choice}")
st.image(selected_image, caption=image_choice, use_column_width=True)
