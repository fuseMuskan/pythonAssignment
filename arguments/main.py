def sum(*args: int or float) -> int or float:
    """Returns sum of all the numbers

    Returns:
        *args: a list of numbers (int or float)
    """
    sum = 0
    for arg in args:
        sum += arg
    return sum
