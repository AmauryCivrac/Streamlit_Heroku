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
st.title('STREAMLIT App deployed with HEROKU')

## Display Text

st.write('Hello Team !')

## Draw a line chart
st.markdown('## ** Draw a line chart **')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

## Plot a map
st.markdown('## ** Plot a map **')

map_data = pd.DataFrame(
    np.random.randn(200, 2) / [50, 50] + [48.86, 2.35],
    columns=['lat', 'lon'])

st.map(map_data)

## Space out the columns so each one has the same size
c1, c2 = st.beta_columns((1, 1))

## Plot text depending on button choice
c1.markdown('## ** Button choice ** ')
genre = c1.radio( "What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    c1.write('You selected comedy.')
else:
    c1.write("You didn't select comedy.")

## Option with selectbox
c2.markdown('## ** Selectbox ** ')
option = c2.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
stg = 'You selected:' + option 
c2.write(stg)