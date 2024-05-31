a, b = map(int, input().split())


turn = ''

if 1 <= b <= 10:
    turn = 'Right'
    c = 11 - b
else:
    turn = "Left"
    c = 21 - b

r = 11 - a

print(turn, r, c)