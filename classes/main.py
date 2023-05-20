# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line


# 1
class Player():
    # Instance Method
    def __init__(self, name, speed, endurance, accuracy):

        # If speed, endurance or accuracy is not between 0 and 1 (inclusive), a ValueError must be raised
        if not 0 <= speed <= 1:
            raise ValueError('Speed must be between 0 and 1')
        if not 0 <= endurance <= 1:
            raise ValueError('Speed must be between 0 and 1')
        if not 0 <= accuracy <= 1:
            raise ValueError('Speed must be between 0 and 1')
        
        # Assign instance atributes
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    # Define an instance method introduce that takes no arguments (except self!) and returns a string like the following, where 'Bob' is replaced by the player's actual name: 'Hello everyone, my name is Bob.' 
    def introduce(self):
        return "Hello everyone, my name is {}.".format(self.name)


    # Define an instance method strength that takes no arguments and returns a tuple like the following, where the string speed is replaced by the player's actual highest attribute and the value corresponds to that attribute
    def strength(self):
        attributes = [("speed", self.speed), ("endurance", self.endurance), ("accuracy", self.accuracy)]