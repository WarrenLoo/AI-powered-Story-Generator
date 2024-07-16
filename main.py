import streamlit as st

st.markdown('**Bold**, *Italic*')

if st.button('Hi'):
  st.write('hello')
  st.balloons()
  st.snow()

option = st.selectbox(
    'What food would you like?',
    ('Pizza', 'Burger', 'Ice Cream', 'Plain water from Zus Coffee'))

st.write(option)
