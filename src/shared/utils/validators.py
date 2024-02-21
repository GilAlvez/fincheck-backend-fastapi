import re


def full_name_validation(name: str):
    if " " not in name:
        raise ValueError("Name must include at least a first name and a last name.")
    return name


def email_validation(email: str):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format.")
    return email
