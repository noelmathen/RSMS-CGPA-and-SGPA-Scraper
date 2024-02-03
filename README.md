# RSMS CGPA Scraper

## Overview

The RSMS CGPA Scraper is a Python script that automates the process of extracting CGPA data from the Rajagiri School of Engineering and Technology's RSMS (Result and Student Management System) website. This tool is designed to make it easier for students to access their CGPA without manually navigating the website.

## Workflow

1. **Data Preparation**: The first step is to prepare a data file in Excel format. This file should include the following columns:

   - `Name`: Student name
   - `UID`: User ID (e.g., U21090xx)
   - `Password`: RSMS password associated with the User ID

   Save this file as `CSBS_UID_Password_List.xlsx`.
2. **Script Execution**: The script `cgpa.py` is run from the command line. It performs the following tasks for each student in the data file:

   a. Simulates a login to the RSMS website using the provided User ID and Password.

   b. Navigates to the student's profile page to scrape the CGPA.

   c. Extracts the CGPA data from the web page.

   d. Stores the CGPA data in a list.

   e. Handles any errors that may occur during the process.
3. **Data Storage**: The extracted CGPA data is stored in an Excel file named `CGPA_File.xlsx` in the project directory.
4. **Completion**: The script continues this process for all students in the data file, and once completed, it displays a completion message.

## Features

- **Automated Web Scraping**: The script automates the web scraping of CGPA data from RSMS, eliminating the need for manual retrieval.
- **Multi-Account Support**: It can handle multiple student accounts with login credentials in a single run.
- **Error Handling**: The script includes error handling to manage failed requests or login attempts.
- **Data Storage**: Extracted CGPA data is saved to an Excel file for easy access and analysis.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed.
- Required Python packages: `requests`, `BeautifulSoup`, `regex`, `pandas`.

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/RSMS-CGPA-Scraper.git
   ```
2. Navigate to the project directory:

   ```bash
   cd RSMS-CGPA-Scraper
   ```
3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
4. Prepare your student data in an Excel file with columns: `Name`, `UID`, and `Password`. Save it as `CSBS_UID_Password_List.xlsx`.
5. Run the script:

   ```bash
   python cgpa.py
   ```
6. The script will extract the CGPA data and save it in an Excel file named `CGPA_File.xlsx`.
