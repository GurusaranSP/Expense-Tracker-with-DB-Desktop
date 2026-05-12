import mysql.connector


def get_db_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )

    return connection


def insert_expense(
    expense_date,
    amount,
    category,
    notes
):

    connection = get_db_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO expenses
    (expense_date, amount, category, notes)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            expense_date,
            amount,
            category,
            notes
        )
    )

    connection.commit()

    cursor.close()
    connection.close()


def fetch_expenses_for_date(
    expense_date
):

    connection = get_db_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    query = """
    SELECT
        amount,
        category,
        notes
    FROM expenses
    WHERE expense_date = %s
    """

    cursor.execute(
        query,
        (expense_date,)
    )

    expenses = cursor.fetchall()

    cursor.close()
    connection.close()

    return expenses


def fetch_expense_summary(
    start_date,
    end_date
):

    connection = get_db_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    query = """
    SELECT
        category,
        SUM(amount) AS total
    FROM expenses
    WHERE expense_date
    BETWEEN %s AND %s
    GROUP BY category
    """

    cursor.execute(
        query,
        (
            start_date,
            end_date
        )
    )

    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return data