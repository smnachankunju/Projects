from crawler import crawl
from attacker import submit_form
from detectors import detect_sqli, detect_sqli_by_diff, detect_xss
from payloads import XSS_PAYLOADS
from reporter import generate_report

url = input("Enter target URL: ")
forms = crawl(url)

findings = []

normal_payload = "test"
sqli_payload = "' OR '1'='1"

for form in forms:
    action = form.get("action")

    # --- SQL Injection Test ---
    normal_res = submit_form(form, url, normal_payload)
    injected_res = submit_form(form, url, sqli_payload)

    if detect_sqli(injected_res) or detect_sqli_by_diff(normal_res, injected_res):
        findings.append({
            "type": "SQL Injection",
            "action": action,
            "severity": "High"
        })

    # --- XSS Test ---
    for xss_payload in XSS_PAYLOADS:
        res = submit_form(form, url, xss_payload)
        if detect_xss(res, xss_payload):
            findings.append({
                "type": "Cross-Site Scripting (XSS)",
                "action": action,
                "severity": "Medium"
            })
            break

generate_report(url, findings)
