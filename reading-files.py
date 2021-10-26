
try:
  employee_file = open("employees.txt","r")
  
  for employee in employee_file.readlines():
    print(employee)
    
except FileNotFoundError as err:
  print(err)

employee_file.close()