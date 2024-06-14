def check_password_strength(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "_@$" for c in password)
    length = len(password)

    if has_lower and has_upper and has_digit and has_special and length >= 8:
        return "Strong"
    elif (has_lower or has_upper) and has_special and length >= 6:
        return "Moderate"
    else:
        return "Weak"


user_password = input("Enter a password: ")
strength = check_password_strength(user_password)
print(f"Password strength: {strength}")