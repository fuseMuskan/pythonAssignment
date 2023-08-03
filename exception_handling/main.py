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
