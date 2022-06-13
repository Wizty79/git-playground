import random

def select_runes(number_of_runes):
    rune_list = ["Fehu", "Uruz", "Thurisaz", "Ansur", "Raido", "Kauna", "Gebo", "Wunjo", "Hagalaz", "Naudir", "Isar", "Jara", "ihwar", "Pertho", "Algir", "Sowelu", "Tyr", "Berkana", "Ehwas", "Mannaz", "Laguz", "Ingwar", "Odila", "Dag", "skaebne"]
    rune_choice = random.choice(rune_list)
    return rune_choice 

print("Velkommen til dine runer for i dag")

first_choice = input("Skriv 'j' for at se dine runer og 'n' for at vaelge fra: ")
if first_choice == "j":
    second_choice = int(input(f"Hvor mange Runer wil du gerne se i dag? vaelge '1', '2', '3', '4', eller '5'\n"))
    #rune_selection = for _ in range(nr_runes.select_runes()):
    #rune_selection = for nr_runes in range(select_runes)
    number_of_runes = second_choice
    rune_selection = select_runes(number_of_runes) 
    print(rune_selection)
    
#elif print("Kan du have en god dag")