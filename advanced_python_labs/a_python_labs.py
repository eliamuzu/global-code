#Filter, Map, Lambda

#function to determine if a number is even

# def is_even(num):
#     return num % 2 == 0

# is_even = lambda x: x % 2 == 0

# #numbers = [1,56,234,87,4,76,24,69,90,135]
# even_nums = list(filter(is_even, numbers))

# print(even_nums)

# #rewriting code to print out odd numbers
# is_odd = lambda x: x % 2 == 1
# odd_nums = list(filter(is_odd, numbers))

# print(odd_nums)

# #Combinations
# is_even = lambda x: not x % 2 == 0

# #using the reduce function
# from functools import reduce
# strings = ["hello", "everyone", "my", "name", "is"]

# def join_strings(strings):
#     joined = reduce(lambda word, complete: word + " " + complete, strings)
#     return joined

# print(join_strings(strings))


# List Comprehensions
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_nums = [num for num in numbers if num > 0]
print(positive_nums)

even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)
#Classes 
class Person:
    def __init__(self, dob, name, gender, status):
        self.dob = dob
        self.name = name
        self.gender = gender
        self.status = status
    
    def speak(self):
        print(f"Hello, My name is {self.name}")

    def walk():
        print("walking away")

    def get_name(self):
        return self.name
    

    
