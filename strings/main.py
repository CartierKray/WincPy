# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_name_1 = "Ruud Gullit "
scorer_name_2 = "Marco van Basten "
goal_0 = 32
goal_1 = 54

scorers = scorer_name_1 + str(goal_0) + ", " + scorer_name_2 + str(goal_1)

report = scorer_name_1 + "scored in the " + str(goal_0) +"nd minute" '\n' + scorer_name_2 + "scored in the " + str(goal_1) + "th minute"

print(scorers)
print(report)

# --------------------------------------- Part 2 

player = "Frank Rijkaard"
first_name = player[:player.find(" ")]
last_name_len = len(player[player.find(" ") + 1 :])
name_short = f"{player[0]}.{player[player.find(' '):]}"

chant_with_space = f"{first_name}! " * len(first_name)
chant = chant_with_space[:-1]
good_chant = chant[-1] != " "

print(player)
print(first_name)
print(last_name_len)
print(name_short)

print(chant_with_space)
print(chant)
print(good_chant)

