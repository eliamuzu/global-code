i = 0
while(i < 10):
    i = i + 1
    print (i)

#explaination

#printing the numbers 7 to 19
i = 7
while(i < 20):
    print (i)
    i = i+1

#printing all even numbers between 12 and 20
i = 12
while(i < 21):
  if i % 2 == 0:
    print (i)
  i = i + 1

#printing all even numbers between x and y
def evens(x, y):
  while(x<y):
    if x % 2 == 0:
      print (x)
    x = x + 1 

#function for printing reverse even numbers between x and y
def reverse_evens(x, y):
   while y > x:
      y -= 1
      if y % 2 == 0:
         print(y)

        
