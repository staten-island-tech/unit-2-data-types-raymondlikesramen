b=int(input('Please type a number.'))

factors = [1]

for x in range(2, b+1):
    if b % x == 0:
        print(x)
