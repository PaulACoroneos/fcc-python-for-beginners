from classes_objects import Student

student = Student("Paul", "Computer Engineering", 3.5, False)

class GraduateStudent(Student):
  def __init__(self,is_dissertation_done):
    self.is_dissertation_done = is_dissertation_done

  def finishDissertation(self):
    self.is_dissertation_done = True;


grad_student = GraduateStudent(False)

grad_student.finishDissertation()
print(grad_student.is_dissertation_done)