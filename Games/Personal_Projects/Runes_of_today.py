import random

def select_runes ():
    rune_list = ["Fehu", "Uruz", "Thurisaz", "Ansur", "Raido", "Kauna", "Gebo", "Wunjo", ]
    rune_choice = random.choice(rune_list)
    return rune_choice
