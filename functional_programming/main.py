
def square_numbers(numbers: list) -> list:
    """This function takes a list of integers as input and uses the
    map function to return a new list containing the square of each
    element.

    Args:
        numbers (list): a list of integers

    Returns:
        squares (list): square of the integers in the list
    """
    squares = list(map(lambda x: x**2, numbers))
    return squares


def prime_number(num: int) -> bool:
    """This function takes a number a return whether the number
    is prime number or not

    Args:
        num (int): any integer

    Returns:
        result (bool): True (if prime) else False
    """
    flag = 1
    for i in range(2, num):
        if num % i == 0:
            flag = 0
    if flag == 1:
        return True
    else:
        return False


def filter_prime_numbers(numbers: list) -> list:
    """ This function takes a list of integers as input and uses the
    filter function to return a new list containing only the prime
    numbers.

    Args:
        numbers (list): a list of integers

    Returns:
        primes (list): prime numbers
    """
    primes = list(filter(prime_number, numbers))
    return primes
