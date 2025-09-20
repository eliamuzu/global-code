#the map function
names = ["sam", "john", "james"]
map_of_names = map(len, names)
print(list(map_of_names))

#using a for loop to implement a map function
len_of_names = []
for name in names:
    len_of_names.append(len(name))

print("using loops: ", len_of_names)

list_of_ages = [12,13,41,13, 3, 45, 46]

def verify_age(age):
    if(age > 18):
        return True
    else:
        return False

age_check = []

for age in list_of_ages:
    age_check.append((age, verify_age(age)))

print(age_check)

map_ages = list(map(verify_age, list_of_ages))
print(map_ages)
filtered_ages = list(filter(verify_age, list_of_ages))
print(filtered_ages)