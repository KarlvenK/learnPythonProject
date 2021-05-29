cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print()

# number part
answer = 17
if answer != 42:
    print('wrong answer')

if (answer < 100) and (answer > 20) and (answer < 50 or answer > 20):
    print('fuck')
else:
    print('shit')

# check if A in list B
objs = [1, 2, 3, 4, 5]

if 5 in objs:
    print('5 is in list')
else:
    print('5 is not in list')

if 6 not in objs:
    print('yeah')
else:
    print('nope')

# if-else-else structure
age = 12

if age < 4:
    print('cost = 0')
elif age < 18:
    print('cost = 10')
else:
    print('cost = 15')

if objs:
    print("objs is not empty")
else:
    print("objs is empty")

print()
#
odd_nums = [1, 3, 5, 7, 9]
three_times_nums = [3, 6, 9, 12]

for three_num in three_times_nums:
    if three_num in odd_nums:
        print(three_num)
