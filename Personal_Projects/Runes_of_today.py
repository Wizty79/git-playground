import random

def select_runes (number_of_runes):
    rune_list = ["Fehu", "Uruz", "Thurisaz", "Ansur", "Raido", "Kauna", "Gebo", "Wunjo", "Hagalaz", "Naudir", "Isar", "Jara", "ihwar", "Pertho", "Algir", "Sowelu", "Tyr", "Berkana", "Ehwas", "Mannaz", "Laguz", "Ingwar", "Odila", "Dag"]
    rune_choice = random.choice(rune_list)
    return rune_choice 

print("Velkommen til dine runer for i dag")

first_choide = input("Skriv 'j' for at se dine runer og 'n' for at vaelge fra: ")
amount_of_runes = [1, 2, 3, 4, 5]
if first_choide == "j":
    nr_runes = int(input(f"Hvor mange Runer wil du gerne se i dag?\n"))
    runes_selected = []
    for int in nr_runes
    runes_selected.append(random.choice(rune_list))
    
    print(runes_selected)
    random.shuffle(runes_selected)
    print(f"Dette er done runer for i dag:" + {runes_selected})
    
    import random
    rune_list = ["Fehu", "Uruz", "Thurisaz", "Ansur", "Raido", "Kauna", "Gebo", "Wunjo", "Hagalaz", "Naudir", "Isar", "Jara", "ihwar", "Pertho", "Algir", "Sowelu", "Tyr", "Berkana", "Ehwas", "Mannaz", "Laguz", "Ingwar", "Odila", "Dag"]
    todays_selection = random.sample(rune_list, 3)
    print(todays_selection)
    
#    rune.choice.append(draw_runes()) 
#elif:
#    is_divination_over = True

