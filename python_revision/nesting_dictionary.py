#Nesting in Dictionary - France is here the key and Paris the value
capitals = {
    "France": "Paris",
    "Germany": "Berlin",    
}

#Nesting a list in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"], #A dictionary can only have one value in the normal format, so we are using a list as the entire value instead. 
    "Denmark": ["Viborg", "Kobenhavn", "Herning"]
}

#Nesting a Dictionary in a Dictionary
travel_log_b = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12}, 
    "Denmark": {"cities_visited":["Viborg", "Kobenhavn", "Herning"], "total_visits": 5},
}

#Nesting a Dictionary inside a list

travel_log_c = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], #if calling on cities visited be aware this is a list
        "total_visits": 12, #if calling in total visits be aware this is a interger
    },    
    {    
        "country": "Denmark", 
        "cities_visited": ["Viborg", "Kobenhavn", "Herning"], 
        "total_visits": 5,
    }
]

