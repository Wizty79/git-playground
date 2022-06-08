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

#Nesting a Dictionary in a DIctionary
travel_log_b = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12}, 
    "Denmark": {"cities_visited":["Viborg", "Kobenhavn", "Herning"], "total_visits": 5},
}

