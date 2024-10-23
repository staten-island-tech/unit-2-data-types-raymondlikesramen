num1= int(input('number'))
num2=int(input('number'))
gcf=1
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcf = i
print (f'{gcf} is the gcf')