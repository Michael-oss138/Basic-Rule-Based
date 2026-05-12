import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define access scope
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",
    scope
)

# Authorize client
client = gspread.authorize(credentials)

# Open Google Sheet
sheet = client.open("Job Intelligence Results").sheet1


def upload_results(results):

    # Clear old sheet data
    sheet.clear()

    # Add headers
    headers = [
        "title",
        "category",
        "confidence",
        "level",
        "remote"
    ]

    sheet.append_row(headers)

    # Add data rows
    for result in results:

        row = [
            result.get("title", "N/A"),
            result.get("category", "N/A"),
            result.get("confidence", "N/A"),
            result.get("level", "N/A"),
            result.get("remote", "N/A")
        ]

        sheet.append_row(row)

    print("Results uploaded successfully!")