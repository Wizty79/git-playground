import random
from rune_art import The_futhark_three as rune_logo
from rune_letters_dictionary_two import rune_letter_One, rune_letter_two, rune_letter_three, rune_letter_four, rune_letter_five, rune_letter_six, rune_letter_seven, rune_letter_eight, rune_letter_nine, rune_letter_ten, rune_letter_eleven, rune_letter_twelve, rune_letter_thirteen, rune_letter_fourteen, rune_letter_fiveteen, rune_letter_sixteen, rune_letter_seventeen, rune_letter_eighteen, rune_letter_nineteen, rune_letter_twenty, rune_letter_twentyone, rune_letter_twentytwo, rune_letter_twentythree, rune_letter_twentyfour
from rune_letters_dictionary import rune_row 

rune_list = ["Fehu", "Uruz", "Thurisaz", "Ansur", "Raido", "Kauna", "Gebo", "Wunjo", "Hagalaz", "Naudir", "Isar", "Jara", "ihwar", "Pertho", "Algir", "Sowelu", "Tyr", "Berkana", "Ehwas", "Mannaz", "Laguz", "Ingwar", "Odila", "Dag", "skaebne"]
rune_list_two = [rune_letter_One, rune_letter_two, rune_letter_three, rune_letter_four, rune_letter_five, rune_letter_six, rune_letter_seven, rune_letter_eight, rune_letter_nine, rune_letter_ten, rune_letter_eleven, rune_letter_twelve, rune_letter_thirteen, rune_letter_fourteen, rune_letter_fiveteen, rune_letter_sixteen, rune_letter_seventeen, rune_letter_eighteen, rune_letter_nineteen, rune_letter_twenty, rune_letter_twentyone, rune_letter_twentytwo, rune_letter_twentythree, rune_letter_twentyfour]

print(rune_logo)    
print("Velkommen til dine runer for i dag")

first_choice = input("Skriv 'j' for at se dine runer og 'n' for at vaelge fra: ")
if first_choice == "j":
    second_choice = int(input(f"Hvor mange Runer vil du gerne se i dag?\n"))

    rune_selection = []
    
    for char in range(1, second_choice + 1):
        rune_selection.append(random.choice(rune_list)) 
    print(rune_selection)
    
else: 
    print("Kan du have en god dag")

#go back and review the password_generator lesson as thos hold the key I was missing and did not understand. 
