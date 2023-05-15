# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

# 1
import this
print(this)


# 2
import time
def wait(seconds):
    time.sleep(seconds)
print(time)


# 3
import math
def my_sin(number):
    return math.sin(number)
print(my_sin)


# 4
from datetime import datetime
def iso_now():
    current_time = datetime.now().strftime('%Y-%m-%dT%H:%M')
    return current_time
print(iso_now)


# 5 | Nog niet af
import sys
def platform():
    return sys.platform
print(platform)


# 6
from greet import supergreeting
def supergreeting_wrapper(name):
    return supergreeting(name) 
print(supergreeting_wrapper('Winc'))


