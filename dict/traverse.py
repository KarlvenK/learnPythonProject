user_0 = {
    'username': 'tester',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print('key: ' + key)
    print('value: ' + value)
    print()

for key in user_0.keys():
    print(key)

if 'username' in user_0.keys():
    print("'username' " + "is a part of user_0")


for name in sorted(user_0.keys()):
    print(name.title() + ': ' + user_0[name])

print()

for val in user_0.values():
    print(val)
