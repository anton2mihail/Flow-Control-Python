number = "9,223,372,036,854,775,807"
cleanedNumbers = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumbers += number[i]

newNumber = int(cleanedNumbers)
print("The number is {}".format(newNumber))
# *=
# /=
# -=

x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x **= 3
print(x)

y =12
y /= 4
print(y)


greeting = "Good "
greeting += "Morning "
print(greeting)

greeting *= 5
print(greeting)
