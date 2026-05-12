from google_sync import upload_results

sample_results = [
    {
        "title": "Backend Engineer",
        "category": "Tech",
        "confidence": 0.9,
        "level": "Mid Level",
        "remote": True
    },
    {
        "title": "Finance Analyst",
        "category": "Finance",
        "confidence": 0.8,
        "level": "Entry Level",
        "remote": False
    }
]

upload_results(sample_results)