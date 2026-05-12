# Expense Tracker

A full-stack expense tracking and analytics application developed using Python.  
This project enables users to record daily expenses, manage financial data efficiently, and visualize spending patterns through interactive analytics.

The application follows a layered architecture with a Streamlit frontend, FastAPI backend, and MySQL database integration.



# Project Overview

The Expense Tracker application was built to understand and implement the complete workflow of a modern data-driven application, including:

- Frontend development
- Backend API creation
- Database integration
- Data analytics and visualization
- API communication
- Exception handling and logging

The system allows users to:
- Add daily expenses
- Store expense records in a relational database
- Retrieve expenses based on date
- Analyze category-wise spending
- Visualize expense distribution interactively



# Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI
- Uvicorn

## Database
- MySQL

## Python Libraries
- Pandas
- Requests
- Pydantic
- mysql-connector-python



# System Architecture


Streamlit Frontend
        ↓
FastAPI Backend
        ↓
Database Helper Layer
        ↓
MySQL Database



# Features

## Expense Management
- Add expense records
- Categorize expenses
- Store notes for transactions
- Retrieve expenses by date

## Analytics Dashboard
- Category-wise expense summary
- Percentage-based spending analysis
- Interactive bar chart visualization

## Backend Functionality
- REST API development using FastAPI
- Structured request handling
- Logging and exception management
- Database operations abstraction



# Project Structure

expense-tracker/
│
├── backend/
│   ├── server.py
│   ├── db_helper.py
│   ├── logger_setup.py
│   └── server.log
│
├── frontend/
│   ├── app.py
│   ├── add_update_ui.py
│   └── analytics_ui.py
│
├── tests/
│
├── requirements.txt
└── README.md






# Key Learnings

This project helped in gaining practical understanding of:

- Full-stack application development
- REST API architecture
- Frontend-backend integration
- Relational database handling
- Analytics visualization
- Debugging and dependency management
- Layered software design



# Future Enhancements

Planned improvements include:

- Expense editing and deletion
- Authentication system
- Monthly and yearly reports
- Pie chart visualizations
- Export to CSV/PDF
- Cloud deployment
- Advanced analytics dashboard



# Author

Guru Saran Satsangi  
BS in Data Science and Applications  
Indian Institute of Technology Madras