def greet_user():
    print('hello, this is greet function\n')


greet_user()


# transmit info in the func
def greet_user(user_name):
    print('hello, ' + user_name)


greet_user('idiot')


def describe_pet(animal_type, pet_name):
    print('\n i have a ' + animal_type + ".")
    print('my ' + animal_type + "'s name is " + pet_name + '.')


describe_pet('cat', 'tom')


def describe_pet(pet_name, animal_type='dog'):
    print('\n i have a ' + animal_type + ".")
    print('my ' + animal_type + "'s name is " + pet_name + '.')


describe_pet(pet_name='www', animal_type='ggg')
describe_pet('www', 'ooo')
