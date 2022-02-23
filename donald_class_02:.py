class Duck:
    sound = 'Quaaack!'
    walking = 'Walks like a duck.'


    def quack(self): #self is a refrence to the object, not the class, when an object is created from the class, self will refrence that object.   
        print(self.sound) # anything that refnreces anything defined in the class, is de-refnreced off of self, to get the obstanciated object version of it.     
                          # the . (perion) operator is used to de-refrence the object
    def walk(self):
        print(self.walking)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if  __name__ == '__main__': main()

