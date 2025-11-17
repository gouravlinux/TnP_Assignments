import main
import Panels


def userExists(userName, loaded_data):
    if userName in loaded_data:
        return True
    else:
        return False


def verify_password(expected_password, passwd):
    while True:
        if passwd == expected_password:
            return True
        else:
            print("Invalid password. Please enter again!")


def load_file(filename):
    try:
        with open(filename, "r") as f:
            # return json.load(f)
            data = f.read()
            return eval(data)
    except FileNotFoundError:
        return None


def adminLogin():
    print("Welcome to Admin Login Panel: ")
    user = input("Enter username: ")
    file_name = "Admins.txt"
    adminData = load_file(file_name)
    if adminData == None:
        print(f"No {file_name} exists! Redirecting to main panel. ")
        main.main()
        return
    if not userExists(user, adminData):
        print("user not found!")
        return
    else:
        while True:
            passwd = input(f"Hey {user}, Enter your password: ")
            if verify_password(adminData[user], passwd):
                break
            else:
                print("Invalid password. Please enter again!")
        print("Successful Login!")
        Panels.adminPanel(user)
    return


def userLogin():
    print("Welcome to User Login Panel: ")
    user = input("Enter username: ")
    file_name = "Users.txt"
    userData = load_file(file_name)
    if userData == None:
        print("No user found! Returning to main panel!")
        main.main()
        return
    if not userExists(user, userData):
        print("user not found!")
        return
    else:
        while True:
            passwd = input(f"Hey {user}, Please enter your password: ")
            if verify_password(userData[user]["password"], passwd):
                break
            else:
                print("Incorrect password. Please enter again!")
        print("Successful Login!")
        Panels.userPanel(user)
    return


def menuInput():
    while True:
        try:
            x = int(
                input(
                    "1. Login as User\n2. Login as Admin\n3. Back to Main Panel\n4. Exit\nEnter: "
                )
            )
            return x
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 4.")


def mainLogin():
    print("Welcome to Login Panel")
    x = menuInput()
    if x == 1:
        userLogin()
    elif x == 2:
        adminLogin()
    elif x == 3:
        main.main()
        return
    elif x == 4:
        print("Thank you for using Quiz app! Bye:)")
        exit(0)
    else:
        print("Invalid input! Please try again!")


if __name__ == "__main__":
    mainLogin()
