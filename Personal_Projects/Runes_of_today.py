import random

def select_runes(number_of_runes):
    rune_list = ["Fehu", "Uruz", "Thurisaz", "Ansur", "Raido", "Kauna", "Gebo", "Wunjo", "Hagalaz", "Naudir", "Isar", "Jara", "ihwar", "Pertho", "Algir", "Sowelu", "Tyr", "Berkana", "Ehwas", "Mannaz", "Laguz", "Ingwar", "Odila", "Dag", "skaebne"]
    rune_choice = random.choice(rune_list)
    return rune_choice 

print("Velkommen til dine runer for i dag")

first_choide = input("Skriv 'j' for at se dine runer og 'n' for at vaelge fra: ")
if first_choide == "j":
    nr_runes = int(input(f"Hvor mange Runer wil du gerne se i dag?\n"))
    number_of_runes = nr_runes
    select_runes(number_of_runes)
    
    print(f"Dette er dine Runer for i dag:" + " {select_runes}")
    


#    rune.choice.append(draw_runes()) 
#elif:
#    is_divination_over = True

