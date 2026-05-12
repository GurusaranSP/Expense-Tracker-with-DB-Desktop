import streamlit as st
import requests

from datetime import date


API_URL = "http://127.0.0.1:8000"


def show():

    st.header("Add Expense")

    selected_date = st.date_input(
        "Expense Date",
        date.today()
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0,
        step=1.0
    )

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Entertainment"
        ]
    )

    notes = st.text_input(
        "Notes"
    )

    if st.button("Add Expense"):

        payload = [
            {
                "amount": amount,
                "category": category,
                "notes": notes
            }
        ]

        response = requests.post(
            f"{API_URL}/expenses/{selected_date}",
            json=payload
        )

        if response.status_code == 200:

            st.success(
                "Expense Added Successfully"
            )

        else:

            st.error(
                "Failed to Add Expense"
            )