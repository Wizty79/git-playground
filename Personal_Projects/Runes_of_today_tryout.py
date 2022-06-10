import random
from rune_art import The_futhark_three as rune_logo

rune_list = ["Fehu", "Uruz", "Thurisaz", "Ansur", "Raido", "Kauna", "Gebo", "Wunjo", "Hagalaz", "Naudir", "Isar", "Jara", "ihwar", "Pertho", "Algir", "Sowelu", "Tyr", "Berkana", "Ehwas", "Mannaz", "Laguz", "Ingwar", "Odila", "Dag", "skaebne"]

print(rune_logo)

print("Velkommen til dine runer for i dag")

first_choide = input("Skriv 'j' for at se dine runer og 'n' for at vaelge fra: ")
if first_choide == "j":
    nr_runes = int(input(f"Hvor mange Runer wil du gerne se i dag? vaelge '1', '2', '3', '4', eller '5'\n"))
    if nr_runes == "1":
        todays_selection_one = random.sample(rune_list, 1)
        print(todays_selection_one)
    elif nr_runes == "2":
        todays_selection_two = random.sample(rune_list, 2)
        print(todays_selection_two)
    elif nr_runes == "3":
        todays_selection_three = random.sample(rune_list, 3)
        print(todays_selection_three)
    elif nr_runes == "4":
        todays_selection_four = random.sample(rune_list, 4)
        print(todays_selection_four)
    elif nr_runes == "5":
        todays_selection_five = random.sample(rune_list, 5)
        print(todays_selection_five)
elif first_choide == "n":
    exit()