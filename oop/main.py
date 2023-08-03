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

university = University("TU", "Kiritipur", ["IOST", "IOE", "IOM"])
department = Department("IOST", "Muskan Bhandari", ["CSIT", "BCA", "BIT"])
print(university.display_details())
print(department.display_details())


        