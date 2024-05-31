my_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]



n = int(input())
chunk = int(len(my_list) / n)


for i in range(0, len(my_list), chunk):
    new_list = my_list[i:i+chunk]
    new_list.reverse()
    print(new_list)