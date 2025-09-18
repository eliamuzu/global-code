def sayHello():
  print("Hello")

def tellMeASecret():
  return "secreet"

def getHostPort():
  return ("nyde13", 3003)

def getHostPort(host = "nydv12", port=8080):
  return (host, port)


def listjoiner(list):
  string = " "
  for word in list:
    string = string + " "+ word
  return string

list = ["Hi", "Jeanelle"]
print(listjoiner(list))

