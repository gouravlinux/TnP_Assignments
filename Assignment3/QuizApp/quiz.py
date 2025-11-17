import pytz
from datetime import datetime
from tabulate import tabulate

import random

file_name = "Quiz.txt"


# Categories = {'DSA': [{'question':question, 'options':options, 'answer':answer}]}
def addCategory():
    try:
        with open(file_name, "r") as f:
            Categories = eval(f.read())
    except FileNotFoundError:
        Categories = dict()
    while True:
        category = input("Enter the category to be added: ")
        Categories[category] = list()  # storing list of questions
        x = input("Do you want to add more categories? (Y/N): ")
        if x == "Y":
            pass
        elif x == "N":
            break
        else:
            print("Invalid Input! Please try again.")
    with open(file_name, "w") as f:
        f.write(str(Categories))
    return


def addQuestion():
    while True:
        category = input("Enter category of the question: ")
        with open(file_name, "r") as f:
            Categories = eval(f.read())
        if category not in Categories:
            print("category not found! Please first add category")
            return
        else:
            questDict = dict()
            question = input("Enter the question: ")
            options = list()
            for i in range(4):
                options.append(input("Enter the option: "))
            while True:
                answer = input("Enter the correct answer(from the above options): ")
                if answer not in options:
                    print("No such option!")
                else:
                    break
            questDict = {"question": question, "options": options, "answer": answer}
            Categories[category].append(questDict)
            with open("Quiz.txt", "w") as f:
                f.write(str(Categories))
            print("Question added Successfully!")
            return


def removeCategory():
    with open(file_name, "r") as f:
        Categories = eval(f.read())
    categoryItems = Categories.keys()
    while True:
        print(categoryItems)
        print("Delete any of the one category from above")
        category = input("Enter the category to be deleted: ")
        if category not in categoryItems:
            print("No such category found! Please try again")
        else:
            break
    x = input(f"Are you sure you want to remove this category: {category}?(Y/N): ")
    if x == "Y":
        Categories.pop(category)
    else:
        return
    with open(file_name, "w") as f:
        f.write(str(Categories))


def removeQuestion():
    with open(file_name, "r") as f:
        Categories = eval(f.read())
    categoryItems = Categories.keys()
    while True:
        print("Categories of Questions: ")
        print(categoryItems)
        category = input("Enter the category of which the question belongs to: ")
        if category not in Categories:
            print("No such category found! Please provide correct one")
        else:
            break
    while True:
        print("Questions: ")
        print(Categories[category])
        try:
            index = int(input("Enter the index of the question to be deleted: "))
        except ValueError:
            print("Invalid index! Please enter a number.")
            continue
        if index not in range(len(Categories[category])):
            print("Index out-of-bounds! Please enter correct index.")
        else:
            x = input("Are you sure you want to remove this question?(Y/N): ")
            if x == "Y":
                Categories[category].pop(index)
            else:
                return
            break
    with open(file_name, "w") as f:
        f.write(str(Categories))
    print("Question Deleted Successfully!")
    return


def attemptQuiz(user):
    print("Welcome to Attempt Quiz Panel: ")
    try:
        with open(file_name, "r") as f:
            Categories = eval(f.read())
    except FileNotFoundError:
        print("There are no question files till now. ")
        return
    while True:
        print(Categories.keys())
        categoriesKeys = Categories.keys()
        category = input("Select from any of the above categories: ")
        if category not in categoriesKeys:
            print("No such category found! Please enter the correct category again")
        else:
            break
    score = 0
    questions = 0
    n = 0
    if len(Categories[category]) >= 5:
        n = 5
    elif len(Categories[category]) > 0:
        n = len(Categories[category])
    else:
        return

    listOfQuestions = Categories[category].copy()
    random.shuffle(listOfQuestions)

    for i in range(n):
        questions += 1
        print(f"Question No. {i+1}")
        print("Q. ", listOfQuestions[i]["question"])
        print("Options: ")
        options = listOfQuestions[i]["options"].copy()
        random.shuffle(options)
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        while True:
            try:
                ans = int(input("Your answer is option No.: "))
                if 1 <= ans <= len(options):
                    break
                else:
                    print(f"Please select a number between 1 and {len(options)}.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        if options[ans - 1] == listOfQuestions[i]["answer"]:
            print("Correct answer!")
            score += 1
        else:
            answer = listOfQuestions[i]["answer"]
            print(f"Incorrect answer! Correct answer is {answer}")
    ist_timezone = pytz.timezone("Asia/Kolkata")
    now_ist = datetime.now(ist_timezone)
    formatted_time = now_ist.strftime("%H:%M %d/%m/%Y")
    timestamp = formatted_time
    print("Thank you for attempting this quiz!")

    with open("Users.txt", "r") as f:
        userData = eval(f.read())
    quizData = {
        "category": category,
        "marks": score,
        "total_marks": questions,
        "timestamp": timestamp,
    }
    if "Scores" not in userData[user]:
        userData[user]["Scores"] = []
    userData[user]["Scores"].append(quizData)

    print("Results: ")
    table_data = [quizData]

    print(tabulate(table_data, headers="keys", tablefmt="grid"))

    with open("Users.txt", "w") as f:
        f.write(str(userData))
