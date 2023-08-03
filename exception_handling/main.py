# Arithmetic Exception
def arthimetic_exception(num1: int, num2: int) -> int or float:
    """This function takes two take integers and peforms division

    Args:
        num1 (int): first integer
        num2 (int): second integer

    Returns:
        result (int or float): num1 / num2
    """
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return ("Second number cannot be zero.")


# ValueError
def value_error_exception(user_input) -> int:
    """This function takes a user input and converts it into
    integer

    Args:
        user_input (any): user input

    Returns:
        result (int): int(user_input) 
    """
    try:
        result = int(user_input)
        return result
    except ValueError:
        return ("Failed to convert to integer.")


# Custom Exception "Invalid Age Error"
class InvalidAgeError(Exception):
    "Raised when the input value is between 0 and 120"
    pass

def user_age(age: int) -> str:
    """This function takes a user age and determines
    whether it is valid or not

    Args:
        age (int): integer

    Returns:
        result (str): Valid or not
    """
    try:
        if age <= 0 or age >=120:
            raise InvalidAgeError
        else:
            return "Valid Age"
    except InvalidAgeError:
        return "Age must be between 0 and 120"

# Custom Exception "Weak Password Error"
class WeakPasswordError(Exception):
    "Raised when password is less than 8 characters"

def check_password(password: str) -> str:
    """Check if the password is weak or strong

    Args:
        password (str): user's password

    Returns:
        result (str): Strong password or weak password
    """
    try:
        if len(password) <= 8:
            raise WeakPasswordError
        else:
            return "Strong Password"
    except WeakPasswordError:
        return "Password must be 8 characters long"


