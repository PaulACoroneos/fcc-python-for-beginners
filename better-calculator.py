num1 = float(input("Enter first nunber: "))
op = input("Enter an operator: ")
num2 = float(input("Enter a second number: "))


if op == "+":
  print( num1 + num2)
elif op == "-":
  print(num1-num2)
elif op == "*":
  print(num1*num2)
elif op == "/":
  print(num1/num2)
else:
  print("invalid operator")