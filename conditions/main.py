# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather, time_of_day, cow_milk_status, location_of_the_cows, season, slurry_tank, grass_status):
    if 'the cows are on the pasture at night' or 'the cows are standing in the rain':
        return True
    if "The cows are in the cowshed":
        return "Milk the cows"
   
