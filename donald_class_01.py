class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self): #first argument for a method inside a class, not a ketword, can be renamed but most devs stick to self. used to refrence the object itself, see next code V
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if  __name__ == '__main__': main() #with an if statement you can have the code on the same line as long as it's just oen line, normally this is bad practice, but this is the exception
#__name__ will return the name of the current modul and '__main__' tells the code this is not an imported modul but running as the main fail.    

#below the function main calls the function kitten before it's defined, this is called forward declaration which Python don't support:
#the if statement if __name__ =='__main__': main() is a common workaround for this.    

#ex.def main():
#    kitten()

#def kitten():
#    print ('Meow.')
    
#if __name__ =='__main__': main()
