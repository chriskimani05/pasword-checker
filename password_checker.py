import string

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make your password at least 8 characters long.")

    # Digit check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Uppercase check
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Use at least one uppercase letter.")

    # Lowercase check
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Use at least one lowercase letter.")

    # Symbol check
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Include at least one symbol (e.g. @, #, $, !).")

    return score, suggestions

# Main
def main():
    password = input("Enter your password: ")
    score, suggestions = check_password_strength(password)

    print(f"\nPassword Strength Score: {score}/5")

    if score == 5:
        print("✅ Strong password!")
    else:
        print("⚠️ Weak password. Suggestions to improve:")
        for s in suggestions:
            print(f" - {s}")

if __name__ == "__main__":
    main()
