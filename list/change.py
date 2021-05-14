motorcycles = ['honda', 'yamaha', 'suzuki']
#               #0          #1        #2
print(motorcycles)

motorcycles[0] = 'ducati' #change the #0 element
print(motorcycles)

#append list
motorcycles[0] = 'honda'
motorcycles.append('ducati')
print(motorcycles)

#pop the last element
poped_element = motorcycles.pop()
print(motorcycles, 'poped element:', poped_element)

#pop #i element
bad_luck_boy = motorcycles.pop(2)
print(motorcycles)
print(bad_luck_boy)

#list.insert(i, ele) inserts ele at the #i, and all elements after #i (include i) move one step to the right
motorcycles.insert(0, 'ducati')
print(motorcycles)

#delete element of list
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

#remove element according to its value
motorcycles.remove('honda')
print(motorcycles)