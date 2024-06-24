import streamlit as st
import pandas as pd

with st.echo():
    st.title("Welcome to Streamlit")
    st.write("This is introduction to Streamlit")

st.markdown("## Code")
code = '''def hello():
        print("Hello, Streamlit!")'''

show_btn = st.button("Show code!")
if show_btn:
    st.code(code, language='python')

cols = st.columns(2)
with cols[0]:
    age_inp = st.number_input("Input your age")
    st.markdown(f"Your age is {age_inp}")

with cols[1]:
    text_inp = st.text_input("Input your text")
    word_tokenize = "|".join(text_inp.split())
    st.markdown(f"{word_tokenize}")

df = pd.DataFrame({
    'First column': [1, 2, 3, 4],
    'Second column': [10, 20, 60, 90]
})
st.dataframe(df)
show_chart_btn = st.button("Show Chart!!")
if show_chart_btn:
    st.line_chart(df, x='First column', y='Second column')
