string = input('please enter your string: ')
n = int(input('please enter "n" :'))
if n > len(string):
    n = int(input('please enter lower "n" :'))
else:
    print(string[n : -1])