cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

#sort the list permanently
#sort the list
cars.sort()
print(cars)

#sort by another order
cars.sort(reverse = True)
print(cars)

#sort the list temparory
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("the original list:")
print(cars)

print("\nsorted list:")
print(sorted(cars, reverse = True))
print(sorted(cars))

print("original list again:")
print(cars)

#reverse the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

#len of list
print(len(cars))