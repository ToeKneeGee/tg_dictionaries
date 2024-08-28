import random
import sys
# dictionary
fruits = {
  "cherry": "red",
  "blueberry": "blue",
  "lemon": "yellow",
  "lime": "green",
}

print(fruits)
print(fruits.items())

for fruit in fruits:
  print(f"15 - fruit - {fruit}")
  print(f"16 - fruit - {fruit} - fruits[{fruit}] - {fruits[fruit]}")

for key, value in fruits.items():
    print(f"19 - key = {key}")
    print(f"20 - value = {value}")

# nested dictionaries
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
print(f"48 - MENU['espresso'] - {MENU['espresso']}")
print(f"49 - MENU['espresso']['ingredients'] - {MENU['espresso']['ingredients']}")


#sys.exit()
# nexting
#country = input()                 # Add country name
#visits = int(input())             # Number of visits
#list_of_cities = eval(input())    # create list from formatted string
#list_of_cities = eval(input())    # create list from formatted string

# list with nested dictionaries and lists
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(name, times_visited, cities_visited):
  # this works but Angela's example shows dedicated commands for each element.
  #travel_log.append({'country': name, 'visits': times_visited, 'cities': cities_visited})
  # this is angela's code:
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    print(f"86 - new_country {new_country}")
    travel_log.append(new_country)

country = "Italy"                                 # country visited 
visits = 7                                        # Number of visits
list_of_cities = ["Venice", "Rome", "Florence"]   # create list from formatted string

add_new_country(country, visits, list_of_cities)

print(f"90 - travel_log {travel_log}")
print(f"91 - I've been to {travel_log[2]['country']} - {travel_log[2]['visits']} times.")
print(f"92 - My favourite city was {travel_log[2]['cities'][1]}.")

print(f"94 - travel_log[2] {travel_log[2]}")
print(f"95 - travel_log[2]['cities'] - {travel_log[2]['cities']}")

# print Italy data that is at index 2
for index in range (0, len(travel_log[2]['cities'])):
    city = travel_log[2]['cities'][index]
    # when printing a range, from 0 to 3, 3 is not included, only 0, 1, 2 are processed, a total of 3
    print(f"101 - index - {index} city - {city}")


# print country at each index
for index in range (0, len(travel_log)):
    print(f"106 - travel_log[{index}]['country'] - {travel_log[index]['country']}")

# print times visited the country at each index
for index in range (0, len(travel_log)):
    print(f"110 - index = {index} - travel_log[{index}]['country'] - {travel_log[index]['country']} - travel_log[{index}]['visits'] - {travel_log[index]['visits']}")