"""This module consist of a simple University Management System and Bank Account System"""
class University:
    """This is a University class with name, location and departments as attributes
    """
    def __init__(self, name: str, location: str, departments: list) -> None:
        self._name = name
        self._location = location
        self._departments = departments

    def display_details(self):
        """This function displays details of a university

        Returns:
            _type_: Name, Location and Departments of a university
        """
        return f"Name: {self._name}, Location: {self._location}, Departments: {self._departments}"


class Department:
    """This is a Department class which is inherited from 
    University class with name, location and courses and hod as attributes
    """
    def __init__(self, name: str, hod: str, courses: list, university: University) -> None:
        self.university = university
        self.name = name
        self.hod = hod
        self.courses = courses

    def display_details(self):
        """This function displays the details of a department

        Returns:
            _type_: Name, HOD and Courses of the department
        """
        return f"Department Name: {self.name}, HOD: {self.hod}, Courses: {self.courses}"

# Example
nepal_university = University("TU", "KTM", ["IOST"])
department = Department("IOST", "MR", ["CSIT", "BCA"], nepal_university)
department.display_details()


class BankAccount:
    """Bank Account with account number, balance, and account type
    """
    def __init__(self, account_number: str, balance: float, account_type: str) -> None:
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print(f"{self.account_number} deleted.")

class Customer:
    """Customer class with name, age, address and bank details
    """
    def __init__(self, name: str, age: int, address: str, bank_details: BankAccount) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.bank_details = bank_details

    def display_details(self):
        """This functions displays details of a customer.
        """
        print(f"Name: {self.name} Age: {self.age}")

    def __del__(self):
        print(f"{self.name} account's deleted")

# Example
bank_account = BankAccount(account_number="12345890",
                           balance=12345.09,
                           account_type="saving account")
john = Customer(name="John Doe", age=37, address="Baneshowr", bank_details=bank_account)
  