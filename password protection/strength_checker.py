import re
from collections import Counter

# Common weak passwords / patterns
COMMON_PASSWORDS = [
    "password", "admin", "welcome", "qwerty", "letmein",
    "abc123", "password123", "admin123", "iloveyou"
]

SEQUENTIAL_PATTERNS = [
    "0123", "1234", "2345", "3456", "4567", "5678", "6789",
    "abcd", "bcde", "cdef", "defg",
    "qwerty", "asdf", "zxcv"
]


def check_length(password):
    length = len(password)
    if length < 8:
        return 5, "Password is too short (minimum 8 characters recommended)"
    elif length < 12:
        return 15, "Password length is acceptable but could be longer"
    elif length < 16:
        return 30, None
    else:
        return 40, None


def check_character_variety(password):
    score = 0
    warnings = []

    if re.search(r"[a-z]", password):
        score += 8
    else:
        warnings.append("Add lowercase letters")

    if re.search(r"[A-Z]", password):
        score += 8
    else:
        warnings.append("Add uppercase letters")

    if re.search(r"[0-9]", password):
        score += 7
    else:
        warnings.append("Add numbers")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 7
    else:
        warnings.append("Add special characters")

    return score, warnings


def check_repetition(password):
    counts = Counter(password)
    most_common = counts.most_common(1)[0][1]

    if most_common > len(password) / 2:
        return -15, "Too many repeated characters"
    return 0, None


def check_sequences(password):
    lowered = password.lower()
    for pattern in SEQUENTIAL_PATTERNS:
        if pattern in lowered:
            return -20, "Avoid sequential or keyboard patterns"
    return 0, None


def check_common_passwords(password):
    lowered = password.lower()
    for weak in COMMON_PASSWORDS:
        if weak in lowered:
            return -30, "Password contains common or leaked patterns"
    return 0, None


def classify_strength(score):
    if score <= 30:
        return "Very Weak"
    elif score <= 50:
        return "Weak"
    elif score <= 70:
        return "Medium"
    elif score <= 85:
        return "Strong"
    else:
        return "Very Strong"


def check_strength(password):
    score = 0
    warnings = []

    length_score, length_warning = check_length(password)
    score += length_score
    if length_warning:
        warnings.append(length_warning)

    variety_score, variety_warnings = check_character_variety(password)
    score += variety_score
    warnings.extend(variety_warnings)

    rep_score, rep_warning = check_repetition(password)
    score += rep_score
    if rep_warning:
        warnings.append(rep_warning)

    seq_score, seq_warning = check_sequences(password)
    score += seq_score
    if seq_warning:
        warnings.append(seq_warning)

    common_score, common_warning = check_common_passwords(password)
    score += common_score
    if common_warning:
        warnings.append(common_warning)

    score = max(0, min(score, 100))
    strength = classify_strength(score)

    return {
        "score": score,
        "strength": strength,
        "warnings": warnings
    }
