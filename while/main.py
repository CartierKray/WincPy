from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())


# Part 1
# Function takes an integer as an argument
def unique_koala_facts(num):
    # Create an empty list to store the unique facts
    unique_facts = [] 
     # Set an iteration limit to avoid an infinite loop
    int_limit = 1000
    # Loop until we collect the desired number of unique facts or reach the iteration limit
    while len(unique_facts) < num and int_limit > 0:
        # Generate a random koala fact
        fact = random_koala_fact()
           # Check if the fact is already in the unique_facts list
        if fact not in unique_facts:
             # If it's not, add it to the list
            unique_facts.append(fact)
        int_limit -= 1
    # Return the list of unique facts
    return unique_facts
# Print unique_koala_facts with the ammount of int in it to print.
print(unique_koala_facts(1))




# Part 2
def num_joey_facts():
    # count the occurance of each joey
    joey_fact = {}
    # Set the occurrence limit
    occurance_limit = 10
    # Set an iteration limit to avoid an infinite loop
    int_limit = 1000
    # Loop until we reach the occurrence limit or the iteration limit
    while int_limit > 0:
        # Generate a random koala fact
        fact = random_koala_fact()
        # Check if the fact mentions "joey"
        if 'joey' in fact.lower():
            # Increment the count for this joey fact
            joey_fact[fact] = joey_fact.get(fact, 0) + 1
            # Check if we have reached the occurrence limit for a particular fact
            if joey_fact[fact] == occurance_limit:
                # Return the number of unique joey facts counted
                return len(joey_fact)
# Print num_joey_facts function
print(num_joey_facts())




# Part 3
def koala_weight():
    # Set an iteration limit to avoid an infinite loop
    int_limit = 100
    # Loop until we find the weight fact or we reach the iteration limit
    while int_limit > 0:
        # Generate a random koala fact
        fact = random_koala_fact()
        # Check if the fact mentions koala 'weight'
        if 'kg' in fact.lower():
            # Extract the weight from the fact  
             weight_str = int(fact.split("kg")[0].split(" ")[-1])
             # Convert the weight to an integer in kg
             try:
                 weight_kg = int(weight_str)
                 return weight_kg
             except ValueError:
                 pass
        int_limit -= 1
    # If the iteration limit is reached without finding the weight fact, return -1 as failure
    return -1
# Print koala_weight function 
print(koala_weight())
        

       
    
