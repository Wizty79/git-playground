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
  
