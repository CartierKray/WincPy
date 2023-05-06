# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

#1
spain_most_spoken_language = "Castilian Spanish"
switserland_most_spoken_language = "Swiss German"
print(spain_most_spoken_language == switserland_most_spoken_language)


#2
spain_most_religion = "Roman Catholic"
switerland_most_religion = "Roman Catholic"
print(spain_most_religion == switerland_most_religion)


#3
spain_capital = "Madrid"
switserland_capital = "Bern"
result =  len(spain_capital) != len(switserland_capital)
print(result)

#4
spain_GDP = 1,393,351,000,000
switserland_GDP = 731,502,000,000
print(switserland_GDP < spain_GDP)


#5
spain_population_growth = 0.12
switzerland_population_growth = 0.64
result = (spain_population_growth < 1) and (switzerland_population_growth < 1)
print(result)


# Data for question 6 & 7
spain_population = 46222613
switserland_population = 8563760

#6
result = spain_population > 10000000 or switserland_population > 10000000
print(result)

#7
result = (spain_population > 10000000 and switserland_population <= 10000000) or (switserland_population > 10000000 and spain_population <= 10000000)
print(result)