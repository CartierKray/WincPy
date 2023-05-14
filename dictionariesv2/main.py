# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

countries = get_countries()

# Part 1
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    # Create a passport with the key value pairs. returing the arguments
    passport = {
            "name": name,
            "date_of_birth": date_of_birth,
            "place_of_birth": place_of_birth,
            "height": height,
            "nationality": nationality
        }
    
    return passport




# Part 2
def add_stamp(passport, country):
    if 'stamps' not in passport:
        passport['stamps'] = []

    if country != passport['nationality'] and country not in passport['stamps']:
        passport['stamps'].append(country)

    return passport




# Part 3
def add_biometric_data(passport, biometric_type, value, date):
    if 'biometric' not in passport:
        passport['biometric'] = {}

    passport['biometric'][biometric_type] = {
        'date': date,
        'value': value
    }

    return passport



