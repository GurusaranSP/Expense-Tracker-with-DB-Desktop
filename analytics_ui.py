import streamlit as st
import requests
import pandas as pd

from datetime import date


API_URL = "http://127.0.0.1:8000"


def show():

    st.header("Analytics")

    start_date = st.date_input(
        "Start Date",
        date.today()
    )

    end_date = st.date_input(
        "End Date",
        date.today()
    )

    if st.button("Get Analytics"):

        payload = {
            "start_date": str(start_date),
            "end_date": str(end_date)
        }

        response = requests.post(
            f"{API_URL}/analytics/",
            json=payload
        )

        data = response.json()

        st.write(data)

        if not data:

            st.warning(
                "No expense data found"
            )

            return

        chart_data = []

        for category, values in data.items():

            chart_data.append({
                "Category": category,
                "Total": values["total"]
            })

        df = pd.DataFrame(
            chart_data
        )

        st.dataframe(df)

        st.bar_chart(
            df.set_index("Category")
        )