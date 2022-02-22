#ex.
#def main():
#    for i in range(25):
#        print(i, end = ' ')
#    print()
#if using this function instead of inclusive_range finction it will print fromv 0 to 24, where as this will 0 to 25 instead

def main():
    for i in inclusive_range(25):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    #initialise parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args 
    elif numargs == 3:
        (start, stop, stop) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == '__main__': main()

     


    