# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line

broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

sum_one_each = broccoli + leek + potato + brussel_sprout
total_items = 4
avg_price = sum_one_each / total_items

num_broccolis = 5
num_leeks =  2
num_potatoes = 7
num_brussel_sprouts = 10

total_broccolis = broccoli * num_broccolis
total_leeks = leek * num_leeks
total_potato = potato * num_potatoes
total_brussel_sprouts = brussel_sprout * num_brussel_sprouts

sum_total = total_broccolis + total_leeks + total_potato + total_brussel_sprouts

discount_percentage = 30
discount = (discount_percentage / 100) * sum_total
discounted_sum_total = round(sum_total - discount, 2)


print(discounted_sum_total)

