
# Creating a Dictionary
myDictionary1 = input(
    "Enter the key:value pair separated by comma(,): ").split(',')
myDictionary1 = {k: v for k, v in (x.split(':') for x in myDictionary1)}

# Displaying The Dictionary
print(myDictionary1)


# Sorting by Key

for key in sorted(myDictionary1.keys()):
    print(f"{key} => {myDictionary1[key]} ")


# Sorting by Value

print(sorted(myDictionary1.items(), key=lambda x: x[1]))

# Concatenate
myDictionary2 = input(
    "\nEnter the key:value pair separated by comma(,) for Second Dictionary: ").split(',')
myDictionary2 = {k: v for k, v in (x.split(':') for x in myDictionary2)}

myNewDictionary = myDictionary1
myNewDictionary.update(myDictionary2)

print(f"Concatenated Dictionary =>{myNewDictionary}")
