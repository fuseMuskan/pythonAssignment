import string

# List Comprehension
def more_than_five_characters(strs: list) -> list:
    """The function takes a list of strings and returns
    a list that only contains more than 5 characters

    Args:
        strs (list): a list of strings

    Returns:
        result (list): a list of strings having more than 5 characters
    """

    result = [word for word in strs if len(word) > 5]
    return result


def zero_sum_triplets(list_one: list, list_two: list, list_three: list) -> list:
    """This function creates a unique triplets from list_one, list_two
    and list_three (x, y, z) where x is from list_one, y is from list_two,
    and z is from list_three, such that x + y + z = 0

    Args:
        list_one (list): a list of integers
        list_two (list): a list of integers
        list_three (list): a list of integers

    Returns:
        result (list): a list of integers
    """
    result = [(x, y, z) for x, y, z in zip(list_one, list_two, list_three) if x + y + z == 0]
    result = list(set(result))
    return result


# Dictionary Comprehension
def create_dictionary(keys_list: list, values_list: list) -> dict:
    """This functions takes two different list one containing keys and
    another values and returns a dictionary using those two lists.

    Args:
        keys_list (list): A list containing keys
        values_list (list): A list containing values

    Returns:
        result_dict (dict): A dictionary made from keys and values list
    """
    result_dict = {key: value for key, value in zip(keys_list, values_list)}
    return result_dict


def create_ascci_dict() -> dict:
    """This function returns a dictionary of keys having
    lowercase alphabets and ascii values of those alphabets

    Returns:
        ascci_dict (dict): a dictionary containing alphabet and ascci value
    """

    ascii_dict = {key:ord(value) for key, value in zip(string.ascii_lowercase, string.ascii_lowercase)}
    return ascii_dict



