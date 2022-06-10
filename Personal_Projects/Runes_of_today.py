import random

def select_runes (number_of_runes):
    rune_list = ["Fehu", "Uruz", "Thurisaz", "Ansur", "Raido", "Kauna", "Gebo", "Wunjo", "Hagalaz", "Naudir", "Isar", "Jara", "ihwar", "Pertho", "Algir", "Sowelu", "Tyr", "Berkana", "Ehwas", "Mannaz", "Laguz", "Ingwar", "Odila", "Dag"]
    rune_choice = random.choice(rune_list)
    return rune_choice 

print("Velkommen til dine runer for i dag")

first_choide = input("Skriv 'j' for at se dine runer og 'n' for at vaelge fra: ")
amount_of_runes = [1, 2, 3, 4, 5]
if first_choide == "j":
    second_choide = input("Hvor mange Runer wil du gerne se i dag? Vaelge '1', '2', '3', '4' eller '5'" )
    second_choice_result = amount_of_runes.append(select_runes)
    print(f"Dette er done runer for i dag:" + {second_choide_result})
        
        
        
#    rune.choice.append(draw_runes()) 
#elif:
#    is_divination_over = True

    



        