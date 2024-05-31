my_list = [1,2,3,4,5,6,7,8,9]
n = int(input())
chunk = int(len(my_list) / n)


for i in range(0, len(my_list), chunk):
    print(my_list[i:i+chunk])