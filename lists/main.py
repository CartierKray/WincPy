# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line


# Part 1 
def alphabetical_order(film_names):
    return sorted(film_names)

films = ["Jurassic Park", "Star Wars", "E.T.", "Jaws"]
sorted_films = alphabetical_order(films)
print(sorted_films)


# Part 2
def won_golden_globe(film_name):
  golden_globe_winners = [
        "jaws",
        "star wars",
        "e.t. the extra-terrestrial",
        "schindler's list",
        "memoirs of a geisha"
    ]
  return film_name.lower() in [movie.lower() for movie in golden_globe_winners]
film = "Star Wars"
is_won_golden_globe = won_golden_globe(film)
print(is_won_golden_globe)


# Part 3 
def remove_toto_albums(album_list):
       joseph_toto_albums = [
        "Fahrenheit",
        "The Seventh One",
        "Kingdom of Desire",
        "Tambu",
        "Mindfields",
        "Toto XX",
        "Falling in Between",
        "35th Anniversary – Live in Poland",
        "Toto XIV",
        "Old Is New"
    ]
       return [album for album in album_list if album not in joseph_toto_albums]
albums = [
    "Jurassic Park",
    "Falling in Between",
    "E.T.",
    "The Seventh One",
    "Jaws"
]
tidy_albums = remove_toto_albums(albums)
print(tidy_albums)