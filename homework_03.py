# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

positions = [pos for pos, char in enumerate(alice_in_wonderland) if char == "'"]
print("Positions of single quotes:", positions)

single_quote_count = alice_in_wonderland.count("'")
print("Number of single quotes:", single_quote_count)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
Black_sea_s = 436402
Azov_sea_s = 37800
total_s = Black_sea_s + Azov_sea_s
print("Tolat area :", total_s)

# якщо виводити повністю задачу
lack_sea_s = 436402
Azov_sea_s = 37800
total_s = Black_sea_s + Azov_sea_s
print("Black Sea area is 436402")
print("Azov Sea Area is 37800")
print("What is total area?")

print("Answer: Tolat area is", total_s)



# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

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

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_payment = 1179
number_of_payments = 18
Price = month_payment * number_of_payments

print("Computer prise is :", Price)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     
d) 7248 : 6
b) 9907 : 9    
e) 7128 : 5
c) 2789 : 5     
f) 19224 : 9
"""
# a) 8019 : 8
a = 8019
b = 8
result = a / b
print("result: ", result)
# d) 7248 : 6
print("Division1: ", 7248 / 6)
# b) 9907 : 9
number =  9907 / 9
print(f"Division with round: ,  {number: .2f}")
# e) 7128 : 5
print("Division2: ",  7128 / 5)
# c) 2789 : 5
print("Division3: ",  2789 / 5)
# f) 19224 : 9
print("Division4: ",  19224 / 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
Pizza_big_size = 274
Pizza_middle_size = 218
Juice = 35
Cake = 350
Water = 21
Total_Sum = 4 * Pizza_big_size + 2 * Pizza_middle_size + 4 * Juice + Cake + 3 * Water
print("Total_Sum is : ", Total_Sum)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
Total_pics = 232
Pic_on_page = 8
Total_number_of_pages = Total_pics / Pic_on_page
print("total number of pages is: ", Total_number_of_pages)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
Distance = 1600
Oil_usage = 9 / 100
receptacle = 48


Oil_volume = Distance * Oil_usage
print("Total needed oil volume is: ",Oil_volume)

charging_n = Oil_volume / receptacle
print("Number of charging is : ", charging_n)





