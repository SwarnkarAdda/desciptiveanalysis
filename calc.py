import streamlit as st
import numpy as np


# def calculate_mean(values):
#     try:
#         # Convert the list of strings to floats
#         numeric_values = [float(value) for value in values]
#         return np.mean(numeric_values)
#     except ValueError:
#         st.error("Please enter valid numeric values.")
#         return None
#
#
# # Streamlit app
# st.title("Mean Calculator")
# st.write("Enter a list of numeric values separated by commas, and we'll calculate the mean for you!")
#
# # User input
# user_input = st.text_input("Enter values (comma-separated):")
#
# if user_input:
#     # Split input into a list of values
#     value_list = user_input.split(',')
#
#     # Calculate the mean
#     mean_value = calculate_mean(value_list)
#
#     if mean_value is not None:
#         st.success(f"The mean of the given values is: {mean_value}")
#         st.success(f"value are: {value_list}")


from scipy import stats
st.title("Descriptive analytics")
st.write('Enter list of values separated by ","')
n = st.text_input("Enter values , use commas(,) as separator:")
try:
    l = n.split(",")
    f = []
    for i in l:
        f.append(float(i))
    st.write("---")
    st.write(f"Mean: {np.mean(f)}")
    st.write("---")
    st.write(f"Median: {np.median(f)}")
    st.write("---")
    st.write(f"Mode: {list(stats.mode(f))[0]}")
    st.write("---")
    st.write(f"Standard Deviation: {np.std(f)}")
    st.write("---")
    st.write(f"Variance: {np.var(f)}")






except ValueError:
    st.write("Enter valid numbers:")


