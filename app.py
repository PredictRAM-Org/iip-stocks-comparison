import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to load IIP data
def load_iip_data():
    iip_file_path = 'IIP_Data.xlsx'  # Replace with the actual path
    iip_data = pd.read_excel(iip_file_path)
    return iip_data

# Function to load stock data
def load_stock_data(stock_symbol):
    stock_file_path = f'Stock_Data/{stock_symbol}.xlsx'  # Replace with the actual path
    stock_data = pd.read_excel(stock_file_path)
    return stock_data

# Streamlit app
def main():
    st.title("Data Comparison App")

    # Move selection options to the left side
    col1, col2 = st.columns(2)

    # Load IIP data
    with col1:
        st.subheader("IIP Data")
        iip_data = load_iip_data()
        st.dataframe(iip_data)

        # User selects industry for comparison
        industry_options = iip_data.columns[2:]
        selected_industry = st.selectbox("Select Industry for Comparison:", industry_options)

        # Plot time series comparison graph
        st.subheader(f"Time Series Comparison for {selected_industry}")
        plt.figure(figsize=(10, 6))
        plt.plot(iip_data["Date"], iip_data[selected_industry], label=f"{selected_industry} (IIP)")
        plt.xlabel("Date")
        plt.ylabel("Index Value")
        plt.title(f"{selected_industry} - IIP Data")
        plt.legend()
        st.pyplot(plt)

    # Load stock symbols from the Stock_Data folder
    stock_folder_path = 'Stock_Data'  # Replace with the actual path
    stock_symbols = [file.split('.')[0] for file in os.listdir(stock_folder_path) if file.endswith('.xlsx')]

    # User selects Stock Data
    with col2:
        st.subheader("Stock Data")

        # User selects stock symbol
        selected_stock = st.selectbox("Select Stock Symbol:", stock_symbols)

        # Load stock data for the selected symbol
        stock_data = load_stock_data(selected_stock)

        # Show Stock Data
        st.dataframe(stock_data)

        # Plot time series comparison graph
        st.subheader(f"Time Series Comparison for {selected_stock}")
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data["Date"], stock_data["Adj Close"], label=f"{selected_stock} (Stock)")
        plt.xlabel("Date")
        plt.ylabel("Adjusted Close Price")
        plt.title(f"{selected_stock} - Stock Data")
        plt.legend()
        st.pyplot(plt)

if __name__ == "__main__":
    main()
