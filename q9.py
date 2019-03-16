# All occurence of character
myString = input('Enter a string : ')
myCountDictionary = dict((letter, myString.count(letter))
                         for letter in set(myString))
print(myCountDictionary)

# panagram

# -------------Is Pangram--------------


def isPangram(myString):
    myString = myString.upper()
    myAlpha = ord('A')
    while(myAlpha <= ord('Z')):
        if chr(myAlpha) not in myString:
            return False
        else:
            myAlpha += 1
    return True


if isPangram(input("Enter a string : \n")):
    print("The entered String is a Pangram")
else:
    print("The entered String is not a Pangram")
