# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather, time_of_day, cow_milking_status, cow_location, season, slurry_tank, grass_status):
    actions = []

    if (cow_location == 'pasture' and time_of_day == 'night') or (weather == 'rainy' and cow_location != 'cowshed'):
        actions.append('take cows to cowshed')

    if cow_milking_status and cow_location == 'cowshed':
        actions.append('milk cows')

    if slurry_tank and cow_location == 'cowshed' and weather != 'sunny' and weather != 'windy':
        actions.append('fertilize pasture')


    if grass_status and season == 'spring' and weather == 'sunny' and cow_location != 'pasture':
        if cow_location == 'cowshed':
            actions.append('take cows back to pasture')
        actions.append('mow grass')
        if cow_location != 'cowshed':
            actions.append('take cows to cowshed')

    if not actions:
        actions.append('wait')

    return '\n'.join(actions)

print('sunny', 'day', True, 'pasture', 'spring', False, True)       


