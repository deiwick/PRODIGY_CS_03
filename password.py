import re

class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

def check_password_strength(password):
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Too short—use at least 8 characters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("🔸 Add uppercase letters (A-Z).")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔸 Add lowercase letters (a-z).")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔸 Include numbers (0-9).")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("🔸 Use special characters (!@#$...).")

    if score <= 2:
        strength = f"{Colors.RED}Weak 🔴{Colors.RESET}"
    elif score == 3 or score == 4:
        strength = f"{Colors.YELLOW}Moderate 🟡{Colors.RESET}"
    else:
        strength = f"{Colors.GREEN}Strong 🟢{Colors.RESET}"

    return strength, feedback

def main():
    print("🔐 Password Complexity Checker 🔐")
    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("\nSuggestions to improve:")
        for tip in feedback:
            print(tip)
    else:
        print("✅ Your password meets all criteria!")

if __name__ == "__main__":
    main()
