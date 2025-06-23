import hashlib
import json
import os
import random
import getpass

DATA_FILE = "data.json"

# Helper to load users
def load_users():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Helper to save users
def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

#  Registration
import getpass  # Add this to your imports

#  Registration with getpass
def register_user():
    users = load_users()
    username = input("Choose a username: ")

    if username in users:
        print(" Username already exists. Try logging in.")
        return

    password = getpass.getpass("Set your password: ")  # Hidden input
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    sec_answer = input("Name of your first stuffed animal (for Level 3): ").strip().lower()

    users[username] = {
        "password": hashed_pw,
        "security": sec_answer
    }

    save_users(users)
    print(f" Welcome, {username}! You’re officially registered.")

# Level 1 - Username & Password with getpass
def level1_auth(users):
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")  # 👈 Hidden input

    if username in users:
        hashed_input = hashlib.sha256(password.encode()).hexdigest()
        if hashed_input == users[username]["password"]:
            print(f"Okay {username}, let’s see if you got the sauce to log in...")
            return username
        else:
            print("Password ain’t it.")
    else:
        print("User not found.")

    return None


#  Level 2 - OTP
def level2_otp():
    otp = str(random.randint(100000, 999999))
    print(f"\n OTP sent: {otp}")  # Simulated OTP display
    entered = input("Enter the OTP: ")
    if entered == otp:
        print("OTP dropped! You're in.")
        return True
    else:
        print("bro ig you should check your eyes.")
        return False

#  Level 3 - Security Question
def level3_security(user_data):
    answer = input("Final vibe check—your plushie’s name pls: ").strip().lower()
    if answer == user_data["security"]:
        print(" Nice! You’ve got memory, loyalty, and taste.")
        print(" Attitude approved by: Tony Stark, Lizzo, and your inner chaos gremlin.")
        return True
    else:
        print(" Sass revoked. Access denied.")
        return False

#  Main Menu
def main():
    print(" Welcome to the 3-Level Secure Login System ✨")
    choice = input("Do you want to [register] or [login]? ").strip().lower()

    if choice == "register":
        register_user()
    elif choice == "login":
        users = load_users()
        user = level1_auth(users)
        if user:
            if level2_otp():
                if level3_security(users[user]):
                    print(f" Access granted, {user}! You made it through all 3 levels.")
                else:
                    print(" Level 3 failed. Access denied.")
            else:
                print(" Level 2 failed. Access denied.")
        else:
            print(" Level 1 failed. Access denied.")
    else:
        print(" Invalid choice. Please enter 'register' or 'login'.")
    # Start the program
if __name__ == "__main__":
    main()
