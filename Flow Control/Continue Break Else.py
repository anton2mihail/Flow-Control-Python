shoppingList = ("milk", "pasta","eggs","spam","bread","rice")
for item in shoppingList:
    if item == "spam":
        print("I am ignoring " + item)
        continue
    print("Buy " + item)

print('')
for item in shoppingList:
    if item == "spam":
        break

    print("Buy " + item)

print('')

meal = ("egg", "bacon", "spam", "sausages")
nastyFoodItem = ''
for item in meal:
    if item == 'spam':
        nastyFoodItem = item
        break
else:
    print("Ill have a plate of that then, please.")
if nastyFoodItem == 'spam':
    print("Can't i have anything without spam in it?")
