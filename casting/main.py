# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# Part 1
leek_price = 2
print ("Leek is " + str(leek_price ) + " euro per kilo." )

# Part 2
four_leeks = "Leek 4"
find_int = four_leeks.find("4")
get_int = int(four_leeks[find_int])
# print(get_int)

sum_total = str(leek_price * get_int)
print(sum_total)

# Part 3
broccoli_price = 2.34
brocolli_order = "broccoli 1.6"

find_order = brocolli_order.find(" ")
get_integer = float(brocolli_order[find_order+1:])
# print(get_integer)

total_cost = get_integer * broccoli_price
print(f'{get_integer}kg broccoli costs {total_cost:.2f}e')