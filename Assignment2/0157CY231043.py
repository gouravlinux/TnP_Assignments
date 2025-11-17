"""
Name: Gourav Soni
Enrollment: 0157CY231043
Batch: 5
Batch Time: 10:30 am to 12:10 pm
"""

logged_user = ""
user_data = dict()  # structure: {'username':{'name': "fullname",...}}


def inputFields(user):
    # inputing atleast 10 fields
    print("Please provide the required data for the below fields: ")
    name = input("Enter your full name: ")
    course = input("Enter your course name: ")
    specialization = input("Enter your specialization: ")
    year = input("Enter your year: ")
    sem = input("Enter your sem: ")
    address = input("Enter your current address: ")
    contact = input("Enter your contact No: ")
    guardian = input("Enter your guardian name: ")
    guardian_contact = input("Enter your guardian's Contact No: ")
    adhaar = input("Enter your adhaar No: ")
    return [
        name,
        course,
        specialization,
        year,
        sem,
        address,
        contact,
        guardian,
        guardian_contact,
        adhaar,
    ]


def register():
    if logged_user != "":
        print("You can't register if you are already logged in")
        return
    print("\n---Registration---")
    while True:
        user = input("Enter username: ")
        if user in user_data:
            print("user already exist!")
        else:
            break
    while True:
        password = input("Enter password: ")
        re_pass = input("Reenter your new password: ")
        if password == re_pass:
            break
        else:
            print("Passwords didn't match! Please try again.")

    print("Registration Successful! Please provide your full details.")
    info = inputFields(user)
    # Store data in new username
    user_data[user] = {"password": password, "info": info}
    print(f"\nThank you, {user}. Your account has been created.")


def login():
    global logged_user
    if logged_user != "":
        print(f"You are already logged in as {logged_user}.")
        return
    print("\n--- Login Panel ---")
    user = input("Enter username: ")
    if user in user_data:
        for attempt in range(3):
            passwd = input("Enter your password: ")
            if passwd == user_data[user]["password"]:
                print(f"\nSuccessfully Logged in! Welcome, {user}.")
                logged_user = user
                return
            else:
                print(f"Wrong password! You have {2 - attempt} tries left.")
        print("You have failed to log in too many times.")
    else:
        print("No user found with that username!")


def show_user_menu():
    while logged_user != "":
        print(f"\n--- Welcome {logged_user} ---")
        response = input(
            """
            What do you want to do?
            1. Show Profile 
            2. Update Profile
            3. Logout
            Enter your choice(1/2/3)
            """
        )
        if response == "1":
            show_profile()
        elif response == "2":
            update_profile()
        elif response == "3":
            logout()
        else:
            print("Invalid choice, please try again.")


def show_profile():
    if logged_user == "":
        print("You must be logged in to see a profile.")
        return
    print(f"\n---Profile for {logged_user} ---")
    user_details = user_data[logged_user]["info"]
    fields = [
        "Name",
        "Course",
        "Specialization",
        "Year",
        "Semester",
        "Address",
        "Contact",
        "Guardian Name",
        "Guardian's Contact",
        "Aadhaar No.",
    ]

    for i, field in enumerate(fields):
        print(f"{field}: {user_details[i]}")


def update_profile():
    if logged_user == "":
        print("You must be logged in to update a profile.")
        return
    print(f"\n--- Update Profile for {logged_user} ---")
    fields = [
        "Name",
        "Course",
        "Specialization",
        "Year",
        "Semester",
        "Address",
        "Contact",
        "Guardian Name",
        "Guardian's Contact",
        "Aadhaar No.",
    ]
    for i, field in enumerate(fields):
        print(f"{i + 1}. {field}")

    try:
        choice = int(input("\nWhich field do you want to edit? (Enter a number): "))

        if 1 <= choice <= 10:
            new_value = input(f"Enter the new value for {fields[choice - 1]}: ")

            user_data[logged_user]["info"][choice - 1] = new_value
            print("Profile updated successfully!")
        else:
            print("Invalid number. Please choose a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def logout():
    """Logs the current user out."""
    global logged_user
    print(f"\nLogging out {logged_user}...")
    logged_user = ""
    print("You have been successfully logged out.")


def main():
    """The main function and entry point of the program."""
    print("Welcome to LNCT Student Portal")

    # IMPROVEMENT: The main menu should be a loop that runs until the user quits.
    while True:
        # If no one is logged in, show the main menu.
        if logged_user == "":
            response = input(
                """
--- Main Menu ---
Choose an option:
1. Register
2. Login
3. Exit

Select option (1/2/3): """
            )
            if response == "1":
                register()
            elif response == "2":
                login()
            elif response == "3":
                print("Thank you for using the portal. Goodbye!")
                break  # This exits the while loop and ends the program.
            else:
                print("Invalid choice, please select a valid option.")
        else:
            # If someone is logged in, show them their user menu.
            show_user_menu()


# This line starts the program by calling the main function.
if __name__ == "__main__":
    main()
