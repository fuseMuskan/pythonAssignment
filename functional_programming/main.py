
def square_numbers(numbers: list) -> list:
    """_summary_

    Args:
        numbers (list): a list of integers

    Returns:
        squares (list): square of the integers in the list
    """
    squares = list(map(lambda x: x**2, numbers))
    return squares
