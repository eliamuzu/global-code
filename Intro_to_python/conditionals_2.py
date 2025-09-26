yob = int(input("Enter your year of birth: "))
now = 2024
status = "young" if (now - yob) < 18 else "old"
print(status)
