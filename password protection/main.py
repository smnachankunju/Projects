from getpass import getpass

from strength_checker import check_strength
from breach_checker import check_password_breach
from password_hasher import hash_password


def main():
    print("🔐 Password Security Analyzer & Breach Checker")
    print("=" * 45)

    # 1. Secure password input
    password = getpass("Enter password to analyze: ")

    if not password:
        print("❌ Password cannot be empty")
        return

    # 2. Strength check (offline)
    strength_result = check_strength(password)

    print("\n📊 Strength Analysis")
    print("-" * 25)
    print(f"Score    : {strength_result['score']}/100")
    print(f"Strength : {strength_result['strength']}")

    if strength_result["warnings"]:
        print("\n⚠️ Warnings:")
        for warning in strength_result["warnings"]:
            print(f"- {warning}")
    else:
        print("\n✅ No weaknesses detected")

    # Reject very weak passwords early
    if strength_result["strength"] in ["Very Weak", "Weak"]:
        print("\n❌ Password rejected due to low strength")
        return

    # 3. Breach check (k-anonymity)
    print("\n🔍 Checking known data breaches...")
    breached, count = check_password_breach(password)

    if breached:
        print(f"❌ Password found in {count} known breaches")
        print("👉 Choose a different password")
        return
    else:
        print("✅ Password NOT found in known breaches")

    # 4. Secure hashing (bcrypt)
    hashed_password = hash_password(password)

    print("\n🔒 Password accepted and securely hashed")
    print("Stored hash (example):")
    print(hashed_password.decode())

    print("\n🎉 Password passed all security checks!")


if __name__ == "__main__":
    main()
