class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self): #first argument for a method inside a class, not a ketword, can be renamed but most devs stick to self. used to refrence the object itself, see next code V
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if  __name__ == '__main__': main()

