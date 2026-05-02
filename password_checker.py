import re

def check_password_strength(password):
    strength = "Weak"

    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[!@#$%^&*]", password)):
        strength = "Strong"
    elif len(password) >= 6:
        strength = "Medium"

    return strength

password = input("Enter a password: ")
print("Strength:", check_password_strength(password))