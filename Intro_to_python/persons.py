def get_age():
  age = int(input("What is your age?"))
  return age

def get_name():
  name = input("What is your name? ")
  return name

name = get_name()
age = str(get_age())

print("Your name is ", name, "and you are ",age)
