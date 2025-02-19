import pandas as pd
import streamlit as st
import os
from io import BytesIO
import numpy as np

# set the page configuration
st.set_page_config(
    layout="wide",
    page_icon="📊",
    page_title="Data Visualization"
)

# set the title and paragraph
st.title("Data Visualization")
st.markdown("This is a simple data visualization app. You can upload a CSV, Excel and JSON file and visualize the data.")

uploade_file=st.file_uploader("Upload a file (CSV, Excel or JSON)", type=["csv", "xlsx", "json"], accept_multiple_files=True)

if uploade_file:
    for file in uploade_file:
        file_extension = os.path.splitext(file.name)[-1].lower()
        if file_extension == ".csv":
            df = pd.read_csv(file)
            st.success("File uploaded successfully!")
        elif file_extension == ".xlsx":
            df = pd.read_excel(file)
            st.success("File uploaded successfully!")
        elif file_extension == ".json":
            df = pd.read_json(file) 
            st.success("File uploaded successfully!")
        else:
            st.error(f"Unsupported file format {file_extension}. Please upload a CSV, Excel or JSON file.")
            continue

        # display the file info
        st.markdown(f"### **File Name** {file.name}")
        st.markdown(f"### **File Size** {file.size/1024}")

        st.markdown("Preview of the data")
        # to show only four rows of the data head() method
        st.dataframe(df.head(),use_container_width=True)

        st.subheader("Data Cleaning")
        if st.checkbox(f'Clean for data {file.name}'):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates {file.name}"):
                    df = df.drop_duplicates()
                    st.success("Duplicates removed successfully!")
                    st.dataframe(df, use_container_width=True)
            
            with col2:
                if st.button(f"Remove missing values {file.name}"):
                    numeric_vals=df.select_dtypes(include=['int64', 'float64','number']).columns
                    df.replace({"None":np.nan}, inplace=True)
                    st.write(df.isnull().sum())
                    df[numeric_vals].fillna(df[numeric_vals].mean())
                    st.success("Missing values removed successfully!")
                    st.dataframe(df, use_container_width=True)
                    st.write(df.isnull().sum())
                    #         with col2:
                    # if st.button(f"Remove missing values {file.name}"):
                    #     numeric_vals = df.select_dtypes(include=['int64', 'float64', 'number']).columns
                    #     df[numeric_vals].fillna(df[numeric_vals].mean(), inplace=True)  # Inplace directly modify karega
                    #     st.success("Missing values removed successfully!")
                    #     st.dataframe(df, use_container_width=True)

            

        st.subheader("Select Columns to Convert")
        columns=st.multiselect(f"Select columns to convert {file.name}", df.columns , default=df.columns)
        if columns:
            df=df[columns]
            st.success("Columns converted successfully!")
            st.dataframe(df, use_container_width=True)
        
        st.subheader("Data Visualization")
        if st.checkbox(f"Visualize data {file.name}"):
            # drop down the numeric columns
            numeric_columns = df.select_dtypes(include=['int64', 'float64', 'number']).columns
            selected_column = st.selectbox("Select a column", numeric_columns)
            if selected_column:
                st.bar_chart(df[selected_column])


        st.subheader("Convert the File") 
        if st.checkbox(f"Convert the file {file.name}"):
            # drop down the numeric columns
            file_extension = st.selectbox("Select a file extension", ["CSV", "Excel", "JSON"])
            if file_extension == "CSV":
                csv_buffer = BytesIO()
                df.to_csv(csv_buffer, index=False)
                csv_buffer.seek(0)
                st.download_button("Download CSV", csv_buffer, file_name=f"{file.name.split('.')[0]}.csv", mime="text/csv")
            elif file_extension == "Excel":
                excel_buffer = BytesIO()
                df.to_excel(excel_buffer, index=False)
                excel_buffer.seek(0)
                st.download_button("Download Excel", excel_buffer, file_name=f"{file.name.split('.')[0]}.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            elif file_extension == "JSON":
                json_buffer = BytesIO()
                st.write(json_buffer)
                json_str = df.to_json(orient="records")
                json_buffer.write(json_str.encode('utf-8'))
                json_buffer.seek(0)
                st.download_button("Download JSON", json_buffer, file_name=f"{file.name.split('.')[0]}.json", mime="application/json")       