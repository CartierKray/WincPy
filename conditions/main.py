# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(
    weather, time_of_day, cows_milking_status, cows_location, season, slurry_tank, grass_status,):

    actions = ""
    moved_cows = False

    if time_of_day == "night" and weather == "rainy" and cows_location != "cowshed":
        actions += "take cows to cowshed\n"
    elif cows_milking_status:
        if cows_location != "cowshed":
            actions += "take cows to cowshed\n"
            moved_cows = True
        actions += "milk cows\n"
        if moved_cows:
            actions += "take cows back to pasture\n"
    elif slurry_tank and weather != "sunny" and weather != "windy":
        if cows_location != "cowshed":
            actions += "take cows to cowshed\n"
            moved_cows = True
        actions += "fertilize pasture\n"
        if moved_cows:
            actions += "take cows back to pasture\n"
    elif grass_status and season == "spring" and weather == "sunny":
        if cows_location == "pasture":
            actions += "take cows to cowshed\n"
            moved_cows = True
        actions += "mow grass\n"
        if moved_cows:
            actions += "take cows back to pasture\n"
    else:
        actions += "wait\n"

    return actions[:-1]


print(farm_action("rainy", "night", False, "pasture", "winter", False, False))


