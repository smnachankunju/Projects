import hashlib
import requests


HIBP_API_URL = "https://api.pwnedpasswords.com/range/"


def sha1_hash(password: str) -> str:
    """
    Returns SHA-1 hash of the password in uppercase
    """
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()


def check_password_breach(password: str):
    """
    Checks if the password has appeared in known data breaches
    using k-anonymity.
    
    Returns:
        breached (bool)
        breach_count (int)
    """
    sha1 = sha1_hash(password)
    prefix = sha1[:5]
    suffix = sha1[5:]

    response = requests.get(HIBP_API_URL + prefix)

    if response.status_code != 200:
        raise RuntimeError("Error fetching breach data")

    hashes = response.text.splitlines()

    for line in hashes:
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return True, int(count)

    return False, 0
