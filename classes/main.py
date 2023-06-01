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
        return f"Hello everyone, my name is {self.name}."

    # Define an instance method strength that takes no arguments and returns a tuple like the following, where the string speed is replaced by the player's actual highest attribute and the value corresponds to that attribute
    def strength(self):
        attributes = [("speed", self.speed), ("endurance", self.endurance), ("accuracy", self.accuracy)]
        attributes.sort(key=lambda x: (-x[1], x[1]))
        best_value = attributes[0][1]
        best_attributes = [attr[0] for attr in attributes if attr[1] == best_value]
        return (best_attributes[0], best_value)

# player = Player("Bob", 0.8, 0.8, 0.7)
# best_attribute = player.strength()
# print(best_attribute)


# 2
class Commentator():
     # Instance Method
    def __init__(self, name):
        self.name = name

    # Instance Method
    def sum_player(self, player):
        speed = getattr(player, "speed", 0)
        endurance = getattr(player, "endurance", 0)
        accuracy = getattr(player, "accuracy", 0)
        return speed + endurance + accuracy

# ray = Commentator('Ray Hudson')
# print(ray.name)

    # Instance Method
    def compare_players(self, player1, player2, attribute):
        value1 = getattr(player1, attribute, 0)
        value2 = getattr(player2, attribute, 0)

        if value1 > value2:
            return player1.name
        elif value1 < value2:
            return player2.name
        else:
            strength1 = self.sum_player(player1)
            strength2 = self.sum_player(player2)

            if strength1 > strength2:
                return player1.name
            elif strength1 < strength2:
                return player2.name
            else:
                total1 = strength1 + value1
                total2 = strength2 + value2

                if total1 > total2:
                    return player1.name
                elif total1 < total2:
                    return player2.name
                else:
                    return "These two players might as well be twins!"

# alice = Player('Alice', 0.8, 0.2, 0.6)
# bob = Player('Bob', 0.9, 0.2, 0.6)

# ray = Commentator('Ray Hudson')
# result = ray.compare_players(alice, bob, 'speed')
# print(result)