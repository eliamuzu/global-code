yob = int(input("Enter the year you were born: "))
now = 2024
if (now - yob) < 18:
  print("you are still a child")
elif (now - yob) < 25:
  print("whoa! long way to go")
else:
  print("Hi! Grampss") 
