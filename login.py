def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match a predefined set of credentials
    if username == "admin" and password == "password":
        print("Login successful!")
    else:
        print("Incorrect username or password. Please try again.")

# Main function
def main():
    print("Welcome to the Login Page")
    login()

if __name__ == "__main__":
    main()
