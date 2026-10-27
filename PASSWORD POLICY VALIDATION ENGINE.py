
print("PASSWORD POLICY VALIDATION ENGINE")
print("----------------------------------")

passwords = [
    "abc12",
    "Password123!",
    "AAAA1234!",
    "Student123!",
    "Hello@2026"
]

prohibited_words = ["password", "student", "admin"]

for password in passwords:
    errors = []

    # Check minimum length
    if len(password) < 8:
        errors.append("Password must contain at least 8 characters")

    # Check character categories
    if not any(ch.isupper() for ch in password):
        errors.append("Missing uppercase letter")

    if not any(ch.islower() for ch in password):
        errors.append("Missing lowercase letter")

    if not any(ch.isdigit() for ch in password):
        errors.append("Missing digit")

    if not any(not ch.isalnum() for ch in password):
        errors.append("Missing special character")

    # Check repeated characters
    if any(password[i] == password[i + 1] for i in range(len(password) - 1)):
        errors.append("Contains consecutive repeated characters")

    # Check prohibited substrings (case-insensitive)
    for word in prohibited_words:
        if word in password.lower():
            errors.append("Contains prohibited word: " + word)

    # Display results
    print("\nPassword:", password)

    if len(errors) == 0:
        print("Status: Valid Password")
    else:
        print("Status: Invalid Password")
        print("Failed Conditions:")
        for error in errors:
            print("-", error)
