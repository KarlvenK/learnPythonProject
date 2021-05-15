magicians = ['alice', 'david', 'caolina']
for magician in magicians:
    print(magician)
    print('fuck!\n')
print('loop ends')

# range(a, b)  =>  [a, b)
for value in range(1, 5):
    print(value)

# use range to create list
numbers = list(range(1, 6))
print(numbers)
numbers = list(range(1, 6, 2))
print(numbers)
print()

square = []
for value in range(1, 6):
    t = value ** 2
    square.append(t)

print(square)

for value in range(6, 11):
    square.append(value ** 2)
print(square)

print(min(square))
print(max(square))
print(sum(square))

square = [value ** 3 for value in range(1, 11)]
print(square)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])
print(players[:4])
print(players[2:])

for player in players[:4]:
    print(player.title())
beta_players = players[:]
print(beta_players)
