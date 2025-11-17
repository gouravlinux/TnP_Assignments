"""
Quiz App with FILE HANDLING
    1. registration
    2. login (user and admin)
    3. quiz
        3.1 login
        3.2 attempt quiz
            3.2.a category (DSA, DBMS, PYTHON)
                display at least 5-10 question randomly(shuffle)
                at a time 1 question with options
        3.3 score
            enrollment    category    marks/total marks   datetime
        3.4 logout
        3.5 update profile, email, branch, year
            contact, name,
        3.6 profile
    4. exit
"""

import login
import registration
import json


def adminAdd():
    try:
        with open("Admins.json", "r") as f:
            adminData = json.load(f)
        if adminData == None:
            adminData = dict()
            adminData["admin"] = "admin123"
        with open("Admins.json", "w") as f:
            json.dump(adminData, f, indent=4)
    except FileNotFoundError:
        adminData = dict()
        adminData["admin"] = "admin123"
        with open("Admins.json", "w") as f:
            json.dump(adminData, f, indent=4)


def main():
    print("Welcome to Quiz App")
    adminAdd()
    while True:
        x = int(input("1. User Registration\n2. Login\n3. Exit\nEnter Choice: "))
        if x == 1:
            registration.userRegistration()
        elif x == 2:
            login.mainLogin()
        elif x == 3:
            print("Thank you for using Quiz app! Bye:)")
            exit(0)
        else:
            print("Invalid input! Please try again!")


if __name__ == "__main__":
    main()
