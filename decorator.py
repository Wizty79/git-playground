#Decorator
#A form of meta programming, a type of function that returns a wrapper function

def f1(f):
    def f2():
    print('this is before the function call')
    f()
    print('this is after the function call')
    return f2

@f1 #shortcut, this is the decorator, followed by the function definition that's just below
def f3():
    print('this is f3')

f3()

