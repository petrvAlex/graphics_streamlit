import streamlit as st


page_diagrams = st.Page("pages/diagrams.py", title="Диаграммыс", icon="📊")
home = st.Page("pages/homepage.py", title="Главная", icon="🏠")
pg = st.navigation([home, page_diagrams], position="sidebar")
pg.run()
st.sidebar.success("Select a demo above.")