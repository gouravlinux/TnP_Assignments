"""
Name: Gourav Soni
Enrollment: 0157CY231043
Batch: 5
Batch Time: 10:30 am to 12:10 pm
"""

"""
# Basic if-else Problems
# Q1---Solution
num = int(input("Enter a number: "))
if num < 0:
    print("Number is negative!")
elif num == 0:
    print("Number is 0!")
else:
    print("Number is positive!")
"""
"""
# Q2---Solution
num=int(input("Enter a number: "))
if (num&1):
    print("Number is odd!")
else:
    print("Number is even!")
"""
"""
# Q3---Solution
yr=int(input("Enter a year: "))
if ((yr%4==0 and yr%100!=0) or yr%400==0):
    print("Year is leap year!")
else:
    print("Year is not a leap year!")
"""
"""   
# Q4---Solution
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
if (num1>num2):
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")
"""
"""  
# Q5---Solution
age=int(input("Enter your age: "))
if (age>=18):
    print("You are eligible for voting!")
else:
    print("You are not eligible for voting")
"""
""" 
# Q6---Solution
ch = input("Enter a single character: ")
if len(ch) == 1:
    if ch in "aeiou":
        print(f"{ch} is a vowel!")
    else:
        print(f"{ch} is a consonant!")
else:
    print("Please enter a valid single character!")
"""
""" 
# Q7---Solution
num = int(input("Enter a number: "))
if num % 5 == 0:
    print(f"{num} is divisible by 5!")
else:
    print(f"{num} is not divisible by 5!")
"""
""" 
# Q8---Solution
num=int(input("Enter a number: "))
num1=num
digits=0
while(num>0):
    num=int(num/10)
    digits+=1
print(f"{num1} has {digits} digits!")
"""
""" 
# Q9---Solution
marks=int(input("Enter marks: "))
if (marks>=40):
    print("You have passed the exam!")
else:
    print("You havenot passed exam!")
"""
""" 
# Q10---Solution
num=int(input("Enter a number: "))
if (num%21==0):
    print(f"{num} is divisible by both 3 and 7!")
else:
    print(f"{num} is not a multiple of both 3 and 7!")
"""
# Ladder if & Nested if
""" 
# Q1---Solution
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
num3=int(input("Enter a number: "))
if (num1>num2):
    if (num1>num3):
        print(f"{num1} is greatest!")
    else:
        print(f"{num3} is greatest!")
else:
    if (num2>num3):
        print(f"{num2} is greatest!")
    else:
        print(f"{num3} is greatest!")
"""
""" 
# Q2---Solution
age=int(input("Enter your age: "))
if (age<0 and age>100):
    print("You should not exist in this multiverse!")
elif (age<13):
    print("You are a child!")
elif (age>=13 and age <= 19):
    print("You are a Teenager!")
elif (age>=20 and age<=59):
    print("You are Adult")
else:
    print("You are Senior")
"""
""" 
# Q3---Solution
marks=int(input("Enter marks: "))
if (marks<0 or marks>100):
    print("Invalid marks!")
elif (marks>=90):
    print("Grade: A")
elif (marks>=75):
    print("Grade: B")
elif (marks>=50):
    print("Grade: C")
elif (marks>=35):
    print("Grade: D")
else:
    print("Fail!")
"""
""" 
#Q4---Solution
print("Enter sides of triangle:\n")
side1=int(input("Enter side1: "))
side2=int(input("Enter side2: "))
side3=int(input("Enter side3: "))
if (side1==side2 and side2==side3):
    print("An Equilateral Triangle!")
elif (side1==side2 or side2==side3 or side1==side3):
    print("An Isosceles Triangle!")
else:
    print("A Scalene Triangle!")
"""
""" 
# Q5---Solution
ch=input("Enter a single character: ")
if ord(ch) in range(65,91):
    print(f"{ch} is an Uppercase Character")
elif ord(ch) in range(97,123):
    print(f"{ch} is a Lowercase Character")
elif ord(ch) in range(48,58):
    print(f"{ch} is a digit")
else:
    print(f"{ch} is a special character")
"""
""" 
# Q6---Solution
units=int(input("Enter units: "))
bill=0
if (units<0):
    print("Invalid units!")
elif (units<=100):
    bill=units*5
elif (units<=200):
    bill=units*7
else:
    bill=units*10
print(f"Your bill: {bill}")
"""
""" 
# Q7---Solution
num1=int(input("num1: "))
num2=int(input("num2: "))
num3=int(input("num3: "))
num4=int(input("num4: "))
if (num1>num2):
    if (num1>num3):
        if (num1>num4):
            print(f"{num1} is greatest")
        else:
            print(f"{num4} is greatest")
    else:
        if (num3>num4):
            print(f"{num3} is greatest")
        else:
            print(f"{num4} is greatest")
else:
    if (num2>num3):
        if (num2>num4):
            print(f"{num2} is greatest")
        else:
            print(f"{num4} is greatest")
    else:
        if (num3>num4):
            print(f"{num3} is greatest")
        else:
            print(f"{num4} is greatest")
"""
""" 
# Q8---Solution
year=int(input("Enter any year: "))
if (year%400==0):
    print(f"{year} is both century and leap year")
else:
    print("Not a leap and century year")
"""
""" 
# Q9---Solution
bmi=float(input("Enter BMI: "))
if (bmi<18.5 and bmi>0):
    print("Underweight")
elif (bmi<=24.9 and bmi>=18.5):
    print("Normal")
elif (bmi>=25 and bmi<=29.9):
    print("Overweight")
elif (bmi>=30):
    print("Obese")
else:
    print("Invalid BMI!")
"""
""" 
# Q10---Solution
num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))
if num1 < num2:
    if num1 < num3:
        print(f"{num1} is smallest")
    else:
        print(f"{num3} is smallest")
else:
    if num2 < num3:
        print(f"{num2} is smallest")
    else:
        print(f"{num3} is smallest")
"""
# For Loop Problems
""" 
# Q1---Solution
ls = []
for i in range(100, 1000):
    sum = 0
    j = i
    while j > 0:
        digit = j % 10
        sum += digit**3
        j = j // 10
    if sum == i:
        ls.append(i)
print(ls)
"""
""" 
# Q2---Solution
n = int(input("Enter n: "))
ls = []
print("Printing n prime numbers in a list: \n")
i = 2
while n != len(ls):
    isPrime = True
    for j in range(len(ls)):
        if i % ls[j] == 0:
            isPrime = False
            break
    if isPrime == True:
        ls.append(i)
    i += 1
print(ls)
"""
""" 
# Q3---Solution
ls = []
for i in range(1, 501):
    if i % 3 == 0:
        j = i
        sum = 0
        while j > 0:
            digit = j % 10
            sum += digit
            j = j / 10
        if sum <= 10:
            ls.append(i)
print(ls)
"""
""" 
# Q4---Solution
n=int(input("n: "))
for i in range(n):
        print(" " * (n-i-1),end="")
        print("*" * (i+1),end="")
        print("*" * i,end="\n")
"""
""" 
# Q5---Solution
sentence=input("Enter a string: ").lower()
ls=[]
for i in sentence:
    if (ord(i)>=97 and ord(i)<=122):
        ls.append(i)
ls=set(ls)
if (len(ls)==26):
    print("It is a pangram")
else:
    print("It is not a pangram")
"""
""" 
# Q6---Solution
ls = []
fArr = []
for i in range(2, 101):
    isPrime = True
    for k in range(len(ls)):
        if i % ls[k] == 0:
            isPrime=False
            break
    if isPrime==True:
        ls.append(i)

for i in range(1,len(ls)):
    if (ls[i]-ls[i-1])==2:
        print(f"({ls[i-1]},{ls[i]})")
"""
""" 
# Q7---Solution
num = int(input("Enter a number: "))
strNum = str(num)
sum = 0
for i in strNum:
    digit = int(i)
    sum += digit
if num % sum == 0:
    print("It is a Harshad Number!")
else:
    print("It is not a Harshad Number!")
"""
""" 
# Q8---Solution
rows = int(input("Enter number of rows: "))
for row in range(1,rows+1):
    ans = 1
    print(" "*(rows-row),end="")
    for col in range(1,row+1):
        print(ans,end=" ")
        ans = ans * (row - col)
        ans = int(ans / (col))
    print("\n")
"""
""" 
# Q9---Solution
n = int(input("n: "))
ans = 0
for i in range(1, n + 1):
    ans = ans + i**2
print("Sum of the series: ", ans)
"""
""" 
# Q10---Solution
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


n = int(input("Enter a number: "))
stern = str(n)
ans = 0
j=n
for i in range(len(stern)):
    digit = j % 10
    ans = ans + fact(digit)
    j = int(j / 10)
if n == ans:
    print("It is a Strong number!")
else:
    print("It is not a Strong number")
"""
# While Loop Problems
""" 
# Q11---Solution
def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True 

n = int(input("Enter n: "))

num = n
reverseNum = 0
while num > 0:
    digit = num % 10
    reverseNum = reverseNum * 10 + digit
    num = int(num / 10)
if isPrime(reverseNum):
    print(f"{reverseNum} is prime!")
else:
    print(f"{reverseNum} is not prime!")
"""
""" 
# Q12---Solution
sum = 0
while sum <= 100:
    n = int(input("Enter a number: "))
    while n > 0:
        digit = n % 10
        sum=sum+digit
        n=int(n/10)
"""
""" 
# Q13---Solution
def hasZero(num):
    while(num>0):
        digit=num%10
        if (digit==0):
            return True
        num=int(num/10)
    return False
num_str = input("Enter a number: ")

if not num_str.isdigit():
    print("Please enter a valid positive integer!")
    exit(1)
num=int(num_str)
if hasZero(num) and num_str[0]!='0':
    print("It is a Duck number")
else:
    print("It is not a Duck number")
"""
""" 
# Q14---Solution
def numSquareSum(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit**2
        n = n // 10
    return sum

num = int(input("Enter a number: "))
n=num
st = set()
while True:
    n = numSquareSum(n)
    if n == 1:
        print("It is a happy number!")
        break
    elif n in st:
        print("It is not a happy number!")
        break
    st.add(n)
"""
""" 
# Q15---Solution
num=int(input("Enter a number: "))
n=num
ans=-1
while n%2==0:
    ans=2
    n=n//2
for i in range(3,int(n**0.5)+1,2):
    while n%i==0:
        ans=i
        n=n//i

if n>2:
    ans=n
print(f"{ans} is the largest prime factor of {num}")
"""
""" 
# Q16---Solution
while(True):
    InputStr=input("Enter a palindrome: ")
    if (InputStr==InputStr[::-1]):
        break
"""
""" 
# Q17---Solution
num = int(input("Enter a number: "))
n = num
while True:
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    if sum >= 0 and sum <= 9:
        print("Single digit number: ", sum)
        break
    n = sum
"""
""" 
# Q18---Solution
num=int(input("Enter a number: "))
print("Collatz sequence: ")
ls=[]
while(num!=1):
    if (num%2!=0):
        num=3*num+1
    else:
        num=num//2
    ls.append(num)
print(ls)
"""
""" 
# Q19---Solution
num=int(input("num: "))
n=num**2
i=0
RNum=0
while(n>0):
    anNum=0
    digit=n%10
    RNum=RNum+digit*(10**i)
    i=i+1
    n=n//10
    if (n+RNum==num):
        print(f"{n}+{RNum}={num}")
        break
    else:
        print("Not a Kaprekar's Number!")
"""
""" 
# Q20---Solution
bal=0
while(True):
    print("Welcome to ATM!\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit\n")
    n=int(input("Enter your choice: "))
    if (n<=0 or n>4):
        print("Invalid choice! Enter valid one")
    elif (n==1):
        print("Balance: ",bal)
    elif (n==2):
        inp=int(input("Enter money to be deposited: "))
        bal=bal+inp
    elif (n==3):
        inp=int(input("Enter money to be withdrawn: "))
        if (bal-inp) < 0:
            print("Insufficient Balance!")
        else:
            print("Balance Deducted!")
    elif (n==4):
        print("Thank you for using ATM!")
        break
"""