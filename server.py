from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date

import db_helper

from logger_setup import setup_logger


app = FastAPI()

logger = setup_logger()


class Expense(BaseModel):
    amount: float
    category: str
    notes: str


class DateRange(BaseModel):
    start_date: date
    end_date: date


@app.get("/")
def home():

    logger.info("Home API called")

    return {
        "message": "Expense Tracker Backend Running"
    }


@app.get("/expenses/{expense_date}")
def get_expenses(expense_date: date):

    logger.info(
        f"Fetching expenses for {expense_date}"
    )

    expenses = db_helper.fetch_expenses_for_date(
        expense_date
    )

    if expenses is None:

        raise HTTPException(
            status_code=500,
            detail="Database Error"
        )

    return expenses


@app.post("/expenses/{expense_date}")
def add_expenses(
    expense_date: date,
    expenses: List[Expense]
):

    logger.info(
        f"Adding expenses for {expense_date}"
    )

    try:

        for expense in expenses:

            db_helper.insert_expense(
                expense_date,
                expense.amount,
                expense.category,
                expense.notes
            )

        return {
            "message": "Expenses Added Successfully"
        }

    except Exception as e:

        logger.error(str(e))

        raise HTTPException(
            status_code=500,
            detail="Failed to Add Expenses"
        )


@app.post("/analytics/")
def get_analytics(
    date_range: DateRange
):

    logger.info("Fetching analytics")

    try:

        data = db_helper.fetch_expense_summary(
            date_range.start_date,
            date_range.end_date
        )

        if not data:

            return {}

        total = sum([
            row["total"] for row in data
        ])

        breakdown = {}

        for row in data:

            percentage = (
                (row["total"] / total) * 100
                if total != 0
                else 0
            )

            breakdown[row["category"]] = {
                "total": row["total"],
                "percentage": percentage
            }

        return breakdown

    except Exception as e:

        logger.error(str(e))

        raise HTTPException(
            status_code=500,
            detail="Failed to Fetch Analytics"
        )