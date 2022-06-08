def greet():
  print("Greetings")
  print("Welcome")
  print("Feel right at home")

def greet_with_name(name): #here name is a variable, but it's often refered to as the parameter
  print(f"Greetings {name}")
  print(f"Welcome {name}")
  print(f"Feel right at home {name}")

greet_with_name("Wisti") #here we are giving that same variable a value called "Wisti", but it's often referd to as the argument

