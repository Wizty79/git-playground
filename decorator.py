#Decorator
#A form of meta programming, a type of function that returns a wrapper function

def f1():
    def f2():
    print('this is f2')
    return f2

def f3():
    print('this is f3')



