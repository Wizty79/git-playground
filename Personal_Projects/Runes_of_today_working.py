import random

rune_list = ["Fehu", "Uruz", "Thurisaz", "Ansur", "Raido", "Kauna", "Gebo", "Wunjo", "Hagalaz", "Naudir", "Isar", "Jara", "ihwar", "Pertho", "Algir", "Sowelu", "Tyr", "Berkana", "Ehwas", "Mannaz", "Laguz", "Ingwar", "Odila", "Dag", "skaebne"]
    
print("Velkommen til dine runer for i dag")

first_choice = input("Skriv 'j' for at se dine runer og 'n' for at vaelge fra: ")
if first_choice == "j":
    second_choice = int(input(f"Hvor mange Runer wil du gerne se i dag?\n"))

    rune_selection = []
    
    for char in range(1, second_choice + 1):
        rune_selection.append(random.choice(rune_list)) 
    print(rune_selection)
    
#elif print("Kan du have en god dag")

