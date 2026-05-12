# Job Intelligence API

A Flask-based backend automation project that processes job listings from CSV files, classifies them into categories, exports processed results, and automatically syncs the data to Google Sheets.

---

## Features

- Upload CSV files containing job titles
- Automatically classify job roles
- Detect:
  - Job category
  - Seniority level
  - Remote jobs
- Export processed results as CSV
- Sync classified data directly to Google Sheets
- REST API support using Flask

---

## Technologies Used

- Python
- Flask
- Pandas
- Google Sheets API
- gspread
- oauth2client

---

## Project Structure

```text
job-intelligence-api/
│
├── app.py
├── classifier.py
├── google_sync.py
├── jobs.csv
├── requirements.txt
├── credentials.json
├── result.csv
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Michael-oss138/Basic-Rule-Based.git
```

Move into the project folder:

```bash
cd Basic-Rule-Based
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

---

## Google Sheets Setup

1. Create a Google Cloud Project
2. Enable:
   - Google Sheets API
   - Google Drive API
3. Create a Service Account
4. Download the JSON credentials file
5. Rename it to:

```text
credentials.json
```

6. Place it inside the project folder
7. Share your Google Sheet with the service account email

---

## Running the Application

Start the Flask server:

```bash
python3 app.py
```

---

## CSV Format

Example input CSV:

```csv
title
Backend Engineer
Finance Analyst
NGO Grants Assistant
```

---

## API Endpoint

### Upload CSV

```http
POST /upload-csv
```

Example using curl:

```bash
curl -X POST http://127.0.0.1:5000/upload-csv \
-F "file=@jobs.csv" \
--output result.csv
```

---

## Example Output

```json
{
  "title": "Backend Engineer",
  "category": "Tech",
  "confidence": 0.9,
  "level": "Mid Level",
  "remote": false
}
```

---

## Workflow

```text
CSV Upload
   ↓
Job Classification
   ↓
CSV Export
   ↓
Google Sheets Synchronization
```

---
