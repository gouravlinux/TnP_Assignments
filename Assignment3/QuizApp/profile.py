import json
from tabulate import tabulate

file_name = "Users.json"


def scores(user):
    with open(file_name, "r") as f:
        userData = json.load(f)
    if user not in userData:
        print("You are not a user!")
        return
    scores = userData[user]["Scores"]
    if "Scores" not in userData[user] or not userData[user]["Scores"]:
        print("No quiz history found.")
        return
    print("Your entire quiz history goes here: ")
    print(tabulate(scores, headers="keys", tablefmt="grid"))


def showProfile(user):
    with open(file_name, "r") as f:
        userData = json.load(f)
    if user not in userData:
        print("You are not a user!")
        return
    if userData == dict():
        print("You don't have any details in your profile")
        return
    print("Showing you your profile: ")
    details = userData[user]
    print(tabulate([details], headers="keys", tablefmt="grid"))


def editProfile(user):
    with open(file_name, "r") as f:
        userData = json.load(f)
    if userData[user] == dict():
        print("You don't have any data in your profile!")
        return
    if user not in userData:
        print("you are not a user!")
        return
    while True:
        showProfile(user)
        print("What do you want to edit? ")
        detail = input("Enter the column you want to edit: ")
        if detail == "Scores" or detail == "user":
            print("That can't be edited!")
        elif detail in userData[user]:
            break
        else:
            print("Invalid choice! Please try again.")
    userData[user][detail] = input("Enter new value of that entry: ")
    x = input("Do you really want to make changes? (Y/N): ")
    if x == "N":
        return
    elif x == "Y":
        with open(file_name, "w") as f:
            json.dump(userData, f, indent=4)
    return
