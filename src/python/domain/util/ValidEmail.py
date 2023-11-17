import re


def ValidEmail(email):
    """
    Check if the provided string is a valid email address.
    :param email: The string to be checked.
    :return: True if the string is a valid email address, False otherwise.
    """
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None
