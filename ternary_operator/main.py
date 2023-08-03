
def check_odd_even(num: int) -> str:
    """This function takes an integer as input and uses a ternary
    operator to return "Even" if the number is even, and "Odd" if
    the number is odd.

    Args:
        num (int): any integer

    Returns:
        res (str): "Even" if num is even else "Odd"
    """

    return "Even" if num % 2 == 0 else "Odd"


def find_bigger_number(num1: int, num2: int, num3: int) -> int or str:
    """ This function takes three integers as input and uses a
    ternary operator to return the larger number. If all numbers
    are equal, the it returns "Equal"

    Args:
        num1 (int): any integer
        num2 (int): any integer
        num3 (int): any integer

    Returns:
        result (int or str): larger number among num1, num2, and num3 or "Equal"
    """

    result =  "Equal" if (num1 == num2 & num1 == num3) else num1 if (num1 > num2 and num1 > num3) else num2 if (num2 > num1 and num2 > num3) else num3
    return result
