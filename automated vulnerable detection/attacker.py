import requests
from urllib.parse import urljoin

session = requests.Session()   # 🔥 THIS IS THE FIX


def submit_form(form, base_url, payload):
    action = form.get("action")
    method = form.get("method", "get").lower()

    target_url = urljoin(base_url, action)

    inputs = form.find_all("input")
    data = {}

    for inp in inputs:
        name = inp.get("name")
        if name:
            data[name] = payload

    print(f"[+] Submitting payload to {target_url}")

    if method == "post":
        return session.post(target_url, data=data)
    else:
        return session.get(target_url, params=data)
