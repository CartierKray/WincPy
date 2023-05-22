# Do not modify these lines
__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"

# Add your code after this line

class Homeowner:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.needs = []

    def add_need(self, need):
        self.needs.append(need)


class Specialist:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession


class Electrician(Specialist):
    pass


class Painter(Specialist):
    pass


class Plumber(Specialist):
    pass


# Create homeowners
alfred = Homeowner("Alfred Alfredson", "Alfredslane 123")
bert = Homeowner("Bert Bertson", "Bertslane 231")
candice = Homeowner("Candice Candicedottir", "Candicelane 312")

# Create specialists
alice = Electrician("Alice Aliceville", "electrician")
bob = Painter("Bob Bobsville", "painter")
craig = Plumber("Craig Craigsville", "plumber")

# Add needs for homeowners
alfred.add_need(bob.profession)
alfred.add_need(craig.profession)
bert.add_need(craig.profession)
candice.add_need(alice.profession)
candice.add_need(bob.profession)

# Match specialists with homeowners
alfred_contracts = [specialist.name for specialist in [alice, bob, craig] if specialist.profession in alfred.needs]
bert_contracts = [specialist.name for specialist in [alice, bob, craig] if specialist.profession in bert.needs]
candice_contracts = [specialist.name for specialist in [alice, bob, craig] if specialist.profession in candice.needs]

print("Alfred's contracts:", alfred_contracts)
print("Bert's contracts:", bert_contracts)
print("Candice's contracts:", candice_contracts)

