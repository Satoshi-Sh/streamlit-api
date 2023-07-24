import streamlit as st

# Title of the app
st.title('My Streamlit App')

# A simple text display
st.write('Welcome to my first Streamlit app!')

# An example of interactive widgets
name = st.text_input('Enter your name:', 'John Doe')
st.write(f'Hello, {name}!')

# A plot using Matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
st.pyplot(plt)
