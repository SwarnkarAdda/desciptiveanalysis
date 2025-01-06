import streamlit as st
import numpy as np



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


