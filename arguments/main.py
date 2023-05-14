# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1
def greet(name, greeting_template='Hello, <name>!'):
    return greeting_template.replace('<name>', name)

# print(greet('Olya'))
# print(greet('Anna', 'Whatsup, <name>!'))




# Part 2
def force(mass, body='earth'):
    gravity_factors = {
        'mercury': 3.7,
        'venus': 8.9,
        'earth': 9.8,
        'moon': 1.6,
        'mars': 3.7,
        'jupiter': 23.1,
        'saturn': 9.0,
        'uranus': 8.7,
        'neptune': 11.0,
        'pluto': 0.7,
    }
    gravity = gravity_factors.get(body.lower(), 9.8)
    return round(mass * gravity, 1)

print(force(0.1, 'sun'))