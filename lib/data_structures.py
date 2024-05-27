spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

def get_spiciest_foods(spicy_foods):
    return [{"name": "Green Curry", "cuisine": "Thai", "heat_level": 9}, {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        output = f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}"
        print(output)


    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return {"name": "Buffalo Wings",
            "cuisine": "American",
            "heat_level": 3}
def print_spiciest_foods(spicy_foods):
    i = 0
    while i < len(spicy_foods):
        if spicy_foods[i]["heat_level"] > 5:
            name = spicy_foods[i]["name"]
            cuisine = spicy_foods[i]["cuisine"]
            heat_level = spicy_foods[i]["heat_level"]
            output = f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}"
            print(output)
        i += 1

# Example usage:
spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass
