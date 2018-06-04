name = input("Please enter your name: ")
age = int(input("Please enter your age in years: "))
if (age >= 18) and (age < 31):
    print('{0} the company welcomes you to the holiday!'.format(name))
else:
    print("Sorry {0}, you have been denied entry because you do not fit the age requirements.".format(name))
    print("Have a good day!")
