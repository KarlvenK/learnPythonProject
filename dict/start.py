alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print(alien_0)
del alien_0['points']
print(alien_0)

print()

#

favorite_language = {
    'a': 'python',
    'b': 'c',
    'c': 'go',
    'd': 'rust',
}

print('a\'s favorite language is ' +
      favorite_language['a'].title() +
      '.')
