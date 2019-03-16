myString = input('Enter a string : ')
if myString == myString[::-1]:
    print('Entered String is Palindrome')
else:
    print('Entered String is not a Palindrome')

print('Reverse of a string => ', myString[::-1])
