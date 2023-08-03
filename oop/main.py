from exception_handling.main import user_age

class University(object):
    def __init__(self, name: str, location: str, departments: list) -> None:
        self._name = name
        self._location = location
        self._departments = departments
    
    def display_details(self):
        return f"Name: {self._name}, Location: {self._location}, Departments: {self._departments}"


class Department(University):
    def __init__(self, name: str, hod: str, courses: list) -> None:
        self.name = name
        self.hod = hod
        self.courses = courses
    
    def display_details(self):
        return f"Department Name: {self.name}, HOD: {self.hod}, Courses: {self.courses}"


class BankAccount(object):
    def __init__(self, account_number: str, balance: float, account_type: str) -> None:
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
    
    def __del__(self):
        print(f"{self.account_number} deleted.")

class Customer(object):
    def __init__(self, name: str, age: int, address: str, bank_details: BankAccount) -> None:
        if (user_age(age)):
            self.name = name
            self.age = age
            self.address = address
            self.bank_details = bank_details

    def __del__(self):
        print(f"{self.name} account's deleted")
        super().__del__()


        

            
        




        