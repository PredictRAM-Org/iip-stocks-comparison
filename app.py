import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load IIP data
def load_iip_data():
    iip_file_path = 'path/to/IIP_Data.xlsx'  # Replace with the actual path
    iip_data = pd.read_excel(iip_file_path)
    return iip_data

# Function to load stock data
def load_stock_data(stock_symbol):
    stock_file_path = f'path/to/Stock_Data/{stock_symbol}.xlsx'  # Replace with the actual path
    stock_data = pd.read_excel(stock_file_path)
    return stock_data

# Streamlit app
def main():
    st.title("Data Comparison App")

    # Load IIP data
    iip_data = load_iip_data()

    # Load stock symbols
    stock_symbols = ["AAPL", "GOOGL", "MSFT"]  # Add more stock symbols as needed

    # User selects IIP or Stock Data
    data_option = st.radio("Select Data Type:", ["IIP Data", "Stock Data"])

    if data_option == "IIP Data":
        # Show IIP Data
        st.subheader("IIP Data")
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

    elif data_option == "Stock Data":
        # User selects stock symbol
        selected_stock = st.selectbox("Select Stock Symbol:", stock_symbols)

        # Load stock data for the selected symbol
        stock_data = load_stock_data(selected_stock)

        # Show Stock Data
        st.subheader(f"Stock Data for {selected_stock}")
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
