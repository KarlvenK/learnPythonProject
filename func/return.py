def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#参数默认值应放在末尾
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


#return a dict
def build_persion(first_name, last_name):
    person = {'first': first_name,
              'last': last_name
              }
    return person

musician = build_persion('jimi', 'hendrix')
print(musician)

def build_persion(first_name, last_name, age=''):
    person = {
        'first': first_name,
        'last': last_name
    }
    if age:
        person['age'] = age
    return person

musician = build_persion('jimi', 'hendrix')
print(musician)

#list为列表类型的变量
#def func(list):
#def func(list[:]): 这里list为副本

def make_pizza(*toppings):
    print(toppings)

make_pizza('a', 'b', 'c')
