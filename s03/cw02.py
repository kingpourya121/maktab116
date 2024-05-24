# my_list = []

# nums = input('')
# my_list = ((nums.split(',')))
# new_list = []

# for items in my_list:
#     new_list.append(int(items))

# print(new_list)


list2 = []
number = True
while number:
    number = input('please enter number or "n" for break: ')
    if number == 'n':
        number = False
    else:
        list2.append(int(number))
print(list2)