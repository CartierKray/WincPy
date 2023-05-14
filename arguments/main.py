# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1
def greet(name, greeting_template='Hello, <name>!'):
    return greeting_template.replace('<name>', name)

# print(greet('Olya'))
# print(greet('Anna', 'Whatsup, <name>!'))