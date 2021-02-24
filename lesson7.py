# Генератор словарей

# ascii_table = {numb: chr(numb) for numb in range(ord("a"), ord("Z")+ 1)}
# print(ascii_table)

# test_str = "qwerty"
# func_dict = {0: len,
#              1: type
#              2: max
#              3: min}
# number = 0
# value = func_dict[number](test_str)
# print(value)
#####################################################################

# ascii_table = {numb: chr(numb) for numb in range(ord("a"), ord("z") + 1)}
# for key in ascii_table:
#     print(key, ascii_table[key])
#
# print("A" in ascii_table) # проверяет ключи
#
# test_key = "A"
# if test_key in ascii_table:
#     print(ascii_table[test_key])

#####################################################
# ascii_table = {numb: chr(numb) for numb in range(ord("a"), ord("z") + 1)}
# for key in ascii_table:
#     print(key, ascii_table[key])
#
# print("A" in ascii_table) # проверяет ключи
#
# test_key = 61
# value = ascii_table.get(test_key, "")
# print(value, type(value))

##############################################################################

# ascii_table = {numb: chr(numb) for numb in range(ord("a"), ord("d") + 1)}
# new_dict = ascii_table.copy()
# new_dict["test"] = "test"
# print(new_dict)
# print(ascii_table)

################################################

# ascii_table = {numb: chr(numb) for numb in range(ord("a"), ord("d") + 1)}
# for key, value in ascii_table.items():
#     print(key, value)
#
# print(ascii_table.items())
# print(list(ascii_table.keys()))
# print(list(ascii_table.values()))
# ascii_table.pop(65) #удалвет по ключу
# ascii_table.popitem()
# print(ascii_table)
#######################################################

# dict_1 = {1:1, 2:2}
# dict_2 = {2: "22", 3: "33"}
#
# dict_3 = dict_1.copy()
# dict_3.update(dict_2)
# print(dict_3)
# print(dict_1, dict_2)

#######################################################

# dict_1 = {1:1, 2:2}
# dict_2 = {2: "22", 3: "33"}
#
# dict_3 = dict_1.update(dict_2) #ошибка
# print(dict_3)
# print(dict_1, dict_2)

########################################################3

# dict_1 = {1:1, 2:2}
# dict_2 = {2: "22", 3: "33"}
#
# dict_3 = {**dict_1, **dict_2}
#
# print(dict_3)
# print(dict_1, dict_2)
########################################################
#модули

# import random #Такой вариант самый правильный
# test_str = "qwerty"
# func_dict = {0: len,
#              1: type,
#              2: max,
#              3: min}
# number = random.randint(1, 3)
# value = func_dict[number](test_str)
# print(number, value)

############################################################
# import random
# test_str = "qwerty"
# rand_symbol = random.choice(test_str)
# print(rand_symbol)

############################################################
# import random
# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8]
# new_list = list(set(test_list)) #аналог, который лучше не использовать
# random.shuffle(test_list)
# print(new_list)
# print(test_list)

##########################################################

# from random import choice, shuffle
# test_str = "qwerty"
# rand_symbol_1 = choice(test_str)
# rand_symbol_2 = shuffle(test_str)

##########################################################

# import random as rnd
# test_str = "qwerty"
# rand_symbol = rnd.choice(test_str)
# print(rand_symbol)

########################################################
#Функции

# import random as rnd
# def test_function(param):
#     print(param)
#
# def test_function_2():
#     value = rnd.randint(1, 10)
#     return value
#
# test_function("Hello")
#
# result = test_function_2()
# print(result)

###########################################################





