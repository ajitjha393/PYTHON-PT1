
def increaseResultBy4(myFunction):
    def wrapperFunction(*args, **kwargs):
        return myFunction(*args, **kwargs) + 4
    return wrapperFunction


def multiplyResultBy2(myFunction):
    def wrapperFunction(*args, **kwargs):
        return myFunction(*args, **kwargs) * 2
    return wrapperFunction


@increaseResultBy4
def findSquare(num):
    return num ** 2


@multiplyResultBy2
def findCube(num):
    return num ** 3


print(
    f'''Square of number increased by 4 => {findSquare(int(input("Enter a number to find square")))}''')

print(
    f'''Cube of a number multiply by 2 => {findCube(int(input("Enter a number to find Cube")))}''')
