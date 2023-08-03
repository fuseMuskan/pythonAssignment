
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
