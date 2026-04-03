def risk_score(input_text: str) -> float:
    high_risk = ["delete", "shutdown", "hack"]
    medium_risk = ["install", "run script"]

    text = input_text.lower()

    for word in high_risk:
        if word in text:
            return 0.9

    for word in medium_risk:
        if word in text:
            return 0.6

    return 0.1