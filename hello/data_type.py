str1 = '''一 23414
滴42134
水421344'''
str2 = "wowowo"

print(str1, str2)

int1 = 1
int2 = 2
# actually int3 is a float

int3 = 1 / 2

print(int1, int2, int3)
print(type(int1), type(int2), type(int3))

#string

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("python")
print("\tpython")
print("python\n")

favorite_language = "golang "
favorite_language = favorite_language.rstrip()
#rstrip change "golang " into "golang"
#lstrip change " golang" into "golang"
#strip does both
print(favorite_language)


print(2 ** 3)
#a ** b = a^b

age = 10
message = "happy " + str(age) + "th birthday"
print(message)