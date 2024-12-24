import re

def email_is_valid(email, role: str):
    email_pattern = ""

    if role.lower() == "student":
        email_pattern = r"^[a-z]+(-[a-z]+)*\.\d{7}@stu\.cu\.edu\.ng$"
    elif role.lower() == "lecturer":
        email_pattern = r"^[a-z]+(-[a-z]+)*\.[a-z-]+(-[a-z]+)*@covenantuniversity\.edu\.ng$"

    if re.search(email_pattern, email):
        return True
    return False