current_num = 0
previous_num = 0
for i in range(10):
    current_num = i
    sum = current_num + previous_num
    print(f'current number is: {current_num} and previous number is: {previous_num} and sum is: {sum}')
    previous_num = i