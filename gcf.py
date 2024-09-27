t=int(input('Input number 1'))
y=int(input('Input number 2'))

for x in range(2, t+1 and 2, y+1):
    if t % x == 0 and y % x == 0:
        print(x)

