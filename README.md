# Superstore Excel Automation — Real World Data Cleaning & Reporting

## 📊 Project Overview
A real world data analytics project using the Superstore Sales dataset from Kaggle.
The project covers the full pipeline — from exploring and cleaning raw data using Python
to building a professional automated Excel report with color coding and summary analytics.

## 🛠️ Tools & Technologies
- **Python** — Pandas, NumPy, OpenPyXL
- **Excel** — Automated report generation
- **Dataset** — Superstore Sales (Kaggle)

## 📁 Project Structure
Superstore-Excel-Automation/
├── explore.py
├── report.py
├── superstore_cleaned.csv
└── README.md

## 🔍 Data Cleaning Steps
- Loaded real world Kaggle dataset with 9800 rows and 18 columns
- Converted Order Date and Ship Date from string to datetime
- Fixed Postal Code from float to string format
- Filled 11 missing Postal Code values intelligently using city data
- Dropped useless columns (Country, Row ID)
- Added 4 calculated columns:
  - Shipping Days — days between order and delivery
  - Sales Category — High, Medium, Low classification
  - Order Year — extracted from Order Date
  - Order Month — extracted from Order Date

## 📈 Excel Report Features

### Sales Report Sheet
- 9800 rows of cleaned and enriched data
- Professional dark header formatting
- Color coded Sales Category column:
  - 🟢 High Sales — above $500
  - 🟠 Medium Sales — between $100 and $500
  - 🔴 Low Sales — below $100
- Frozen header row for easy navigation

### Summary Sheet
- Sales by Region breakdown
- Sales by Category breakdown
- Sales by Year breakdown

## 🚀 How to Run This Project
1. Download the any dataset from Kaggle
2. Need to define just the columns and what columns you want
3. Run explore.py to clean the data
4. Run report.py to generate the Excel report
5. Open your file.xlsx to view the results

