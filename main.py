import re

pattern = r"^[0-9]{2}+[a-zA-Z]{2}+[0-9]{6}$"

while True:
    user_input = input("Enter test: ")

    if re.search(pattern, user_input):
        print("Valid")
    else:
        print("Invalid")