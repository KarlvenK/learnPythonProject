#input() stop the program and wait you to input some text
#input(s) s is the string that input will output first before you input text
message = input('tell me sth, and i will repeat it back to you: ')
print(message)

name = input('please enter you name:')
print('hello, ' + name + '!')

prompt = 'if you tell us who you are, we can personalized the message you see'
prompt += '\nwhat is your first name? '

name = input(prompt)
print('\nhello, ' + name + '!')

print()

#int()
age = input("how old are you?")
age = int(age)
if age >= 18:
    print('you are an adult')
else:
    print('you are not an adult yet')
#python use % to operate 'mod'
