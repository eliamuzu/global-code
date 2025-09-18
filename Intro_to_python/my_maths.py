operation = input("What basic operation do you want to do?")
print("Enter two numbers")
x = int(input())
y = int(input())

def calculate(operation,x,y):
  if (operation == "add"):
    return x + y
  elif (operation == "subtract"):
    return x - y
  elif (operation == "multiply"):
    return x * y
  elif (operation == "divide"):
    return x/y
  else:
    return "Enter a valid operation"

print(calculate(operation,x,y))

