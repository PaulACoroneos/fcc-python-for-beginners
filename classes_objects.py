class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    def honors_roll(self):
      return self.gpa >= 3.5


# student = Student("Paul", "Computer Engineering", 3.5, False)

