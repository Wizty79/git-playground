def greet():
  print("Greetings")
  print("Welcome")
  print("Feel right at home")

def greet_with_name(name): #here name is a variable, but it's often refered to as the parameter
  print(f"Greetings {name}")
  print(f"Welcome {name}")
  print(f"Feel right at home {name}")

greet_with_name("Wisti") #here we are giving that same variable a value called "Wisti", but it's often referd to as the argument

#functions with more than one input

def greet_with(name, location):#adding more then 1 parameter by using ,
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

greet_with("Wisti", "Bournemouth")

greet_with(location="Bournemouth", name="Wisti") #both function calls do the same job, but the latter simply specify position and the first make sure to provide the arguments in the right order

