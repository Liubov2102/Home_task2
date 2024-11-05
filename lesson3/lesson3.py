print ("Division: ", 10 / 3)
print ("Division with round: ", 10 / 3)
number =  10 / 3
print ("Division with round: ", number)
print (f"Division with round 1: , {number: .4f}")
from operator import truediv

# print (f"Division with round 2: , {number: .1f}")

# rounded_number = round(10/3,2)

# print ("Division with round 3: ", rounded_number)

# S_Azov_sea = 37800
# S_Black_sea = 436402
# Total_s = S_Azov_sea + S_Black_sea
# print("Total Sea S :", Total_s)

# int_number = int(10/3)
# int_number = int(34.223)
# print(type(int_number))

# a = 10
# b = 10
# print("a==b :", a-b)
# print("ids a and b", id(a), id(b))

# int_number = int(10 / 3)
# print(type(int_number))

#####################################################

# a = 10
# b = 10
# print("a -- b: ", a -- b)
# print("ids", id(a), id(b))

# c = 12
# d = 12
# print("c -- d :", c--d)
# ("ids", id(a), id(b))

#  print(10 -- '10')

# c = 19
#  = 19
# print('c != d -', c != d)

# q = 12
# w = 16
# print('q != w', q != w)

# some = None
# print(some == None)
# some = 10
# print('some is not 10:', some != 10  )

# a = 2
# a = a + 2
# a += 2
# print("a: ", (a))
#
# a = True
# b = True
# if a and b:
#  print('something')

# name = "John1"
# surname = "Smith"
# if name == "John" and surname == "Smith" :
#     print("AMD: name is ok")
#
# if name == "John" or surname == "Smith" :
#     print("OR: name is ok")


# name = "John"
# is_john = name =="John"
#
# if is_john :
#     print("")
#
#
# print(10 == 10.0)
# print(10 == [10])
#
# price = 20.0
# if price == 20 :
#     print("ok")
#
#     import re
#
#     # Given text
#     alice_in_wonderland = (
#         '"Would you tell me, please, which way I ought to go from here?"\n'
#         '"That depends a good deal on where you want to get to," said the Cat.\n'
#         '"I don\'t much care where ——" said Alice.\n'
#         '"Then it doesn\'t matter which way you go," said the Cat.\n'
#         '"—— so long as I get somewhere," Alice added as an explanation.\n'
#         '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
#     )
#
#     # Find all single quote characters in the text
#     single_quotes = re.findall(r"'", alice_in_wonderland)
#     print(len(single_quotes), single_quotes)




# # Find and display all single quote characters
# positions = [pos for pos, char in enumerate(alice_in_wonderland) if char == "'"]
# print("Positions of single quotes:", positions)
# single_quote_count = alice_in_wonderland.count("'")
# print("Number of single quotes:", single_quote_count)

# Мережа супермаркетів має 3 склади, де всього розміщено
# 375 291 товар. На першому та другому складах перебуває
# 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі.



Total_items = 375291
W1  = 375291 - 222950
W3 = 375291 - 250449
W2 = Total_items - (W1 + W3)
print("There are 3 Warehouse related to the Supermarket chain")
print("Total number of items at all warehouses  = 375291")
print("The sum of Items at W1 and W2 is 250 449" )
print("The sum of Items at W2 and W3 is 222 950" )
print("How many items are there at the each warehouse?")


print("Total number of items at W1 = ", W1)
print("Total number of items at W2 = ", W2)
print("Total number of items at W3 = ", W3)




