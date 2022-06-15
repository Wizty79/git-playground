import random
from rune_art import The_futhark_three as rune_logo
from rune_letters import letter_fehu, letter_uruz, letter_thurisaz, letter_ansur, letter_raido, letter_kauna, letter_gebo, letter_wunjo, letter_hagalaz, letter_naudir, letter_isar, letter_jara, letter_ihwar, letter_pertho, letter_algir, letter_soweku, letter_tyr, letter_berkana, letter_ehwas, letter_mannaz, letter_laguz, letter_ingwar, letter_odila, letter_dag 

rune_list_two = letter_fehu, letter_uruz, letter_thurisaz, letter_ansur, letter_raido, letter_kauna, letter_gebo, letter_wunjo, letter_hagalaz, letter_naudir, letter_isar, letter_jara, letter_ihwar, letter_pertho, letter_algir, letter_soweku, letter_tyr, letter_berkana, letter_ehwas, letter_mannaz, letter_laguz, letter_ingwar, letter_odila, letter_dag

rune_list = ["Fehu", "Uruz", "Thurisaz", "Ansur", "Raido", "Kauna", "Gebo", "Wunjo", "Hagalaz", "Naudir", "Isar", "Jara", "ihwar", "Pertho", "Algir", "Sowelu", "Tyr", "Berkana", "Ehwas", "Mannaz", "Laguz", "Ingwar", "Odila", "Dag", "skaebne"]
print(rune_logo)    
print("Velkommen til dine runer for i dag")

first_choice = input("Skriv 'j' for at se dine runer og 'n' for at vaelge fra: ")
if first_choice == "j":
    second_choice = int(input(f"Hvor mange Runer wil du gerne se i dag?\n"))

    rune_selection = []
    
    for char in range(1, second_choice + 1):
        rune_selection.append(random.choice(rune_list)) 
    print(rune_selection)
    
#else print("Kan du have en god dag")

#go back and review the password_generator lesson as thos hold the key I was missing and did not understand. 
