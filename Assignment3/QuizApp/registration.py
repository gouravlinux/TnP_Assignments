import json  # JS Object Notation


def userRegistration():
    print("Welcome to Registration Panel")
    file_name = "Users.json"
    try:
        with open(file_name, "r") as f:
            userData = json.load(f)
    except FileNotFoundError:
        with open(file_name, "w") as f:  # creates an empty file
            userData = dict()

    print("New registration: ")
    while True:
        user = input("Enter username: ")
        if user in userData:
            print("The username is already used. Please try different username! ")
        else:
            break

    while True:
        passwd = input("Enter your password: ")
        re_pass = input("re-Enter your password: ")
        if passwd == re_pass:
            userData[user] = dict()
            userData[user]["password"] = passwd
            break
        else:
            print("Your passwords didn't match. Please try again!")

    userData[user]["name"] = input("Enter your name: ")
    userData[user]["course"] = input("Enter your course name: ")
    userData[user]["specialization"] = input("Enter your specialization: ")
    userData[user]["year"] = input("Enter your year: ")
    userData[user]["sem"] = input("Enter your semester: ")
    userData[user]["address"] = input("Enter your address: ")
    userData[user]["contact"] = input("Enter your contact No.: ")
    userData[user]["guardian"] = input("Enter your guardian's name: ")
    userData[user]["guardianContact"] = input("Enter your guardian's contact No.: ")
    userData[user]["Adhaar"] = input("Enter your Adhaar Number: ")
    userData[user]["Scores"] = list()
    print(f"\nThank you, {user}. Your account has been created.")
    with open(file_name, "w") as f:
        json.dump(userData, f, indent=4)
    return


if __name__ == "__main__":
    userRegistration()
