class Animal:
    x = [1, 2, 3] #this is a class variable, not OV like below, because it's defined in the calss, not in any method
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'
        #The 3 above are object variables, they only exist when the object is created from the class 
        # they do not exist in the class itself 

        # The point is that the 3 object variables are incapsulated and thus immutable unlike the CV at the top (incapsulation are a major benifit of object oriented programming) 

    def type(self, t = None):
        if t: self._type = t # you don't want to access the variables directly, that's why they have the underscore which means do not touch directly,    
        return self._type    # so you don't set these variable from outside the classs methods, 

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s 
        return self._sound 

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1)

if __name__ == '__main__': main()



