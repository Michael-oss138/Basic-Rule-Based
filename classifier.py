def classify_job(title):
    title_lower = title.lower()

    # CATEGORY
    if any(word in title_lower for word in ["ngo", "foundation", "development", "grants"]):
        category = "NGO / Development"
    elif any(word in title_lower for word in ["engineer", "developer", "software"]):
        category = "Tech"
    elif any(word in title_lower for word in ["analyst", "finance", "bank"]):
        category = "Finance"
    else:
        category = "General"

    # LEVEL
    if any(word in title_lower for word in ["intern", "assistant", "junior"]):
        level = "Entry Level"
    elif any(word in title_lower for word in ["senior", "lead", "manager"]):
        level = "Senior Level"
    else:
        level = "Mid Level"

    # REMOTE
    remote = "remote" in title_lower

    return {
        "title": title,
        "category": category,
        "level": level,
        "remote": remote
    }