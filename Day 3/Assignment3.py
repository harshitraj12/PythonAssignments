def mod_divide(func):
    def inner(a,b):
        if a>b:
          print(a/b)
        else:
            print(b/a)

        return func(a,b)
    return inner

@mod_divide
def divide(a,b):
    pass

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
divide(num1,num2)
