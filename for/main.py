from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


# Add your code after this line

""" Write your functions here. """

# Part 1
def shortest_names(countries):
    shortest_len = float("inf")
    shortest_names = []

    for country in countries:
        country_length = len(country)
        if country_length < shortest_len:
            shortest_len = country_length
            shortest_names = [country]
        elif country_length == shortest_len:
            shortest_names.append(country)
    return shortest_names


# Part 2
def most_vowels(countries):
    vowels = ['a', 'e', 'i', 'o', 'u']
    leaderboard = [("", 0)]

    for country_name in countries:
        count = 0
        for char in country_name:
            if char.lower() in vowels:
                count += 1

        for position in range(len(leaderboard)):
            if count >= leaderboard[position][1]:
                leaderboard.insert(position, (country_name, count))
                break
            if position > 2:
                break

    return [x[0] for x in leaderboard[:3]]



# Part 3
def alphabet_set(countries):
    countries = [country.lower() for country in countries]
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    countries_used = []
    for country in countries:
        for char in country:
            if char in alphabet:
                alphabet.remove(char)
                if country not in countries_used:
                    countries_used.append(country)
        if len(alphabet) == 0:
            return countries_used


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

# Part 1
print(shortest_names(countries))

# Part 2
print(most_vowels(countries))

# Part 3
print(alphabet_set(countries))
print(len(alphabet_set(countries)))





