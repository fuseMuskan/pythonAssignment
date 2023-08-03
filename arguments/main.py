def sum(*args: int or float) -> int or float:
    """Returns sum of all the numbers

    Returns:
        *args: a list of numbers (int or float)
    """
    sum = 0
    for arg in args:
        sum += arg
    return sum


def create_student_report(name: str, age: int, **kwargs) -> dict:
    """_summary_

    Args:
        name (str): name of the student
        age (int): age of the student

    Returns:
        student_report (dict): returns a dictionary with the student's
        information and a list of subjects along with their scores
    """
    student_report = dict()
    student_report["name"] = name
    student_report["age"] = age
    student_report["marks"] = list()
    for key, value in kwargs.items():
        student_report["marks"].append({key: value})
    return student_report
