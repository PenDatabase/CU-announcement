import re

pattern = r"^[a-z]+(-[a-z]+)*\.\d{7}@stu\.cu\.edu\.ng$"

while True:
    user_input = input("Enter test: ")

    if re.search(pattern, user_input):
        print("Valid")
    else:
        print("Invalid")