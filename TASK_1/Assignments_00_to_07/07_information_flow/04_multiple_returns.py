def get_user_info():
    user_info = {
        "First Name": input("What is your first name?: "),
        "Last Name": input("What is your last name?: "),
        "Email": input("What is your email address?: ")
    }
    return user_info  

def main():
    user_data = get_user_info()
    print("Received the following user data:")
    
    for key, value in user_data.items():  # Pretty Print
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
