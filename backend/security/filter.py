def is_safe(input_text: str) -> bool:
    blocked_keywords = [
        "delete all",
        "shutdown system",
        "format disk",
        "hack",
        "exploit"
    ]

    text = input_text.lower()

    for keyword in blocked_keywords:
        if keyword in text:
            return False

    return True