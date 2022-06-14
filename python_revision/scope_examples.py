################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

############### Local Scope ############

def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()
print(potion_strength) #can't access potion_strength as it's 
                        #defined outside of the function

############## global scope #################

player_health = 10

def drink_potion():
  potion_strength  = 2
  print(player_health)

#here we can use the variable player_healt due to its potision
#it's in the global scope, and not locked inside the function. 
  
enemies = 1

def increase_enemies():
  global enemies
  enemies += 2 # however we can't modify the variable enemies until we've declared it in the function as a global vartiable, without that, it would fail
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


def increase_enemies_two():
  print(f"enemies inside function: {enemies}")
  return enemies + 1 #however we should avoid modifying a global scope, instead we can add the return statement with a + 1 to get the same result  

