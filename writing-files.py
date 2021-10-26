# try:
#   employee_file = open("employees.txt","a")

#   employee_file.write("\nJeremy")
    
# except FileNotFoundError as err:
#   print(err)

# employee_file.close()

try:
  employee_file = open("employees1.txt","w")

  employee_file.write("\nJeremy")
    
except FileNotFoundError as err:
  print(err)

employee_file.close()
