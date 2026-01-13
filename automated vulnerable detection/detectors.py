def detect_sqli(response):
    """
    Detects SQL Injection by checking for database error messages
    """

    errors = [
        "sql syntax",
        "mysql",
        "sqlite",
        "oracle",
        "psql",
        "warning: mysql",
        "unclosed quotation"
    ]

    for error in errors:
        if error in response.text.lower():
            return True

    return False
def detect_sqli_by_diff(normal_res, injected_res):
    """
    Detect SQL Injection by comparing response lengths
    """

    diff = abs(len(normal_res.text) - len(injected_res.text))

    if diff > 100:   # threshold
        return True

    return False
def detect_xss(response, payload):
    """
    Detect reflected XSS by checking payload in response
    """
    return payload.lower() in response.text.lower()
def detect_auth_bypass(response):
    indicators = [
        "welcome",
        "logout",
        "user information",
        "userinfo.php",
        "logout.php"
    ]

    text = response.text.lower()
    return any(i in text for i in indicators)
