# Django CSV Data Analysis Web Application

## Project Overview

This project is a Django-based web application that allows users to upload CSV files, perform data analysis using Pandas and NumPy, and display the results and visualizations on the web interface. The application supports basic data analysis tasks such as displaying the first few rows of data, calculating summary statistics, and generating basic plots.

## Features

+ **CSV File Upload:** Users can upload CSV files through the web interface.
+ **Data Processing:** The application reads the uploaded CSV files and performs basic data analysis. Display the first few rows of the data. Calculate summary statistics (mean, median, standard deviation) for numerical columns. Identify and handle missing values.
+ **Data Visualization:** Generate and display basic plots such as histograms for numerical columns.
+ **User Interface:** A simple and user-friendly interface to display the results and visualizations.

## Requirements

- Python 3.x
* Django
+ Pandas
- NumPy
+ Matplotlib / Seaborn

## Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/yourusername/django-csv-analysis.git
cd django-csv-analysis
```
3. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
5. Install Dependencies
6. Create a Django Project
```bash
django-admin startproject myproject .
```
8. Create a Django App
```bash
python manage.py startapp myapp
```
10. Update `settings.py`
Add `'myapp'` to the `INSTALLED_APPS` list in `myproject/settings.py`.
12. Run the Server
```bash
python manage.py runserver
```
14. Access the Application
Open your web browser and navigate to `http://127.0.0.1:8000/`.
