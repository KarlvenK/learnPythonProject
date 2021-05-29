cur = 1
while cur <= 5:
    print(cur)
    cur += 1

prompt = 'tell me a number'
message = ''

while message != '1':
    message = input(prompt)
    if message == '1':
        print('quit')
    else:
        print('go on')

# we can also use break to stop while
while True:
    message = input(prompt)
    if message == '1':
        break
    else:
        print('go on')

# we use continue to skip to next loop
# no code
