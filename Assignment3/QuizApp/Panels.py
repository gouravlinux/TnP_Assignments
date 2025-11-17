import json
import quiz
import profile


def get_choice(prompt):
    while True:
        try:
            choice = int(input(prompt))
            return choice
        except ValueError:
            print("Invalid input! Please enter a number.")


def adminRegistration():
    print("Admin Registration Panel: ")
    file_name = "Admins.json"
    try:
        with open(file_name, "r") as f:
            adminData = json.load(f)
    except FileNotFoundError:
        with open(file_name, "w") as f:
            adminData = dict()

    while True:
        user = input("Enter username: ")
        if user in adminData:
            print("The username is already used. Please try different username! ")
        else:
            break

    adminData[user] = str()
    while True:
        passwd = input("Enter your password: ")
        re_pass = input("re-Enter your password: ")
        if passwd == re_pass:
            adminData[user] = passwd
            break
        else:
            print("Passwords didnot match. Please try again. ")

    with open(file_name, "w") as f:
        json.dump(adminData, f, indent=4)

    print("Admin Registration was successful!")
    return


def removeAdmin():
    admin = input("Enter the admin to be removed: ")
    file_name = "Admins.json"
    try:
        with open(file_name, "r") as f:
            adminData = json.load(f)
    except FileNotFoundError:
        print("No admins Found!")
        return

    if admin not in adminData:
        print(f"{admin} not found!")
        return
    adminData.pop(admin)
    with open(file_name, "w") as f:
        json.dump(adminData, f, indent=4)
    print("Removal Successful!")
    return


def removeUser():
    user = input("Enter the user to be removed: ")
    file_name = "Users.json"
    try:
        with open(file_name, "r") as f:
            userData = json.load(f)
    except FileNotFoundError:
        print("No user found!")
        return
    if user not in userData:
        print(f"{user} not found!")
        return
    x = input("Do you really want to remove the user? (Y/N)? ")
    if x == 'N':
        return
    if x == "Y":
        userData.pop(user)
        with open(file_name, "w") as f:
            json.dump(userData, f, indent=4)
        print("Removal Successful!")
    return


def adminPanel(user):
    print(f"Hey {user}, Welcome to Admin Panel!")
    x = get_choice(
        "1. Add a new admin\n2. Remove an admin\n3. Remove a user\n4. Add a category\n5. Add a Question in a category\n6. Remove a category\n7. Remove a Question\n8. Go to Previous Panel\n9. Exit\nEnter your choice: "
    )
    if x == 1:
        adminRegistration()
    elif x == 2:
        removeAdmin()
    elif x == 3:
        removeUser()
    elif x == 4:
        quiz.addCategory()
    elif x == 5:
        quiz.addQuestion()
    elif x == 6:
        quiz.removeCategory()
    elif x == 7:
        quiz.removeQuestion()
    elif x == 8:
        return
    elif x == 9:
        print("Thank you for using Quiz App! Goodbye.")
        exit(0)
    else:
        print("Please enter a valid choice!")


def userPanel(user):
    print(f"Hey {user}, Welcome to User Panel!")
    while True:
        x = get_choice(
            "1. Attempt Quiz\n2. Scores\n3. Show Profile\n4. Edit Profile\n5. Back to Previous Panel\n6. Exit\nEnter your choice: "
        )
        if x == 1:
            quiz.attemptQuiz(user)
        elif x == 2:
            profile.scores(user)
        elif x == 3:
            profile.showProfile(user)
        elif x == 4:
            profile.editProfile(user)
        elif x == 5:
            return
        elif x == 6:
            print("Thank you for using Quiz App! Goodbye.")
            exit(0)
        else:
            print("Invalid choice! Please try again.")
