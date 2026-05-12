def classify_job(title):

    title_lower = title.lower()

    category_scores = {
        "Tech": 0,
        "Finance": 0,
        "NGO / Development": 0,
        "General": 0
    }

    # Keywords
    tech_keywords = [
        "engineer",
        "developer",
        "software",
        "backend",
        "frontend"
    ]

    finance_keywords = [
        "finance",
        "bank",
        "accountant",
        "analyst"
    ]

    ngo_keywords = [
        "ngo",
        "foundation",
        "development",
        "grants",
        "humanitarian"
    ]

    # Score categories
    for word in tech_keywords:
        if word in title_lower:
            category_scores["Tech"] += 1

    for word in finance_keywords:
        if word in title_lower:
            category_scores["Finance"] += 1

    for word in ngo_keywords:
        if word in title_lower:
            category_scores["NGO / Development"] += 1

    # Pick best category
    category = max(category_scores, key=category_scores.get)

    highest_score = category_scores[category]

    # Confidence calculation
    if highest_score == 0:
        confidence = 0.30
        category = "General"
    else:
        confidence = min(
            0.50 + (highest_score * 0.20),
            0.95
        )

    # Level detection
    if any(word in title_lower for word in [
        "intern",
        "assistant",
        "junior"
    ]):
        level = "Entry Level"

    elif any(word in title_lower for word in [
        "senior",
        "lead",
        "manager"
    ]):
        level = "Senior Level"

    else:
        level = "Mid Level"

    # Remote detection
    remote = "remote" in title_lower

    return {
        "title": title,
        "category": category,
        "confidence": round(confidence, 2),
        "level": level,
        "remote": remote
    }