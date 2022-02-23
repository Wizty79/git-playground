class Animal:
    def __init__(self, type, name, sound): #__init__ = class function that works like an constructor or initialiser
        self._type = type                  # you pass it arguments, here 3(first is always self and don't count as part of the 3), and that's what makes it an object method
        self._name = name                  #again, it's an object method because self poiints to the object  
        self._sound = sound                # AND THOSE ARE USED TO INITIALISE OBJECT VARIABLES

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_anumal(): requires and animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

def main():
    a0 = Animal('kitten', 'fluffy', 'rawr')
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronica', 'hello'))

if __name__ == '__main__': main()
