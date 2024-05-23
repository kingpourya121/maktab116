age_list = []

for i in range(3):
    age = int(input('please enter age: '))
    age_list.append(age)
    age_list.sort()
max_age = age_list[-1]
min_age = age_list[0]
a =123

print(f'maximum age is {max_age} and minimum age is {min_age}')
