# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

# librairies pour streamlit
import streamlit as st

### CONFIG STREAMLIT

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

### Titre de l'application
st.title('Application STREAMLIT pour HEROKU')

st.write('Hello World')