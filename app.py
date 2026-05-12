import streamlit as st

import add_update_ui
import analytics_ui


st.set_page_config(
    page_title="Expense Tracker",
    layout="wide"
)

st.title("Expense Tracking System")


tab1, tab2 = st.tabs([
    "Add / Update",
    "Analytics"
])


with tab1:

    add_update_ui.show()


with tab2:

    analytics_ui.show()