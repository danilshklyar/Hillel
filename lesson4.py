# обработка исключений

# value = input('Введи целое число')
# if value.isdigit():
#     value = int(value)
#     result = value / 2
#     print(result)
# else:
#     print("не верный ввод")
#####################################################
# value = input('Введи целое число')
# if value.isdigit():
#     value = int(value)
#     result = value / 2
# else:
#     print("не верный ввод")
#     result = 0
#
# print(result)
######################################################

# value = input('Введи целое число')
# if value.isdigit():
#     value = int(value)
#     result = value / 2
# else:
#     print("не верный ввод")
#     result = ""
#
# print(result)
#################################################################


# try:
#     value = float(value)
#     result = 2 / value
# except (ValueError, TypeError):
#     print("Не верный ввод")
#     value = 0
#     result = 1
# except ZeroDivisionError:
#     print("Делеие на 0")
#     value = 0
#     result = 1
# except FileExistsError:
#     pass
# print(result)
###########################################
# my_str = "qwertyqwerty"
# symbol = "ty"
# res = my_str.rfind(symbol)
# print(res)
############################################

# my_str = "qwertyqwerty"
# symbol = "ty"
# res = my_str.replace(symbol, "TY", 1)
# print(res)

#################################################
# test_str = "qwerty is default String"
#
# res = test_str.capitalize()
# print(res)
#################################################

# test_str = "qwerty is default String"
#
# res = test_str[0].upper() + test_str[1:]
# print(res)
# res = test_str.replace(test_str[0], test_str.upper(), 1)
# print(res)

# методы строк
# цикл for

# my_string = "test string"
# # print(len(my_string))
#
# for symbol in my_string:
#     print(symbol * 3)


# my_string = "test string"
#
# for symbol in my_string:
#     if symbol in "eyuioa":
#         print(symbol)
########################################################

# my_string = "test strIng"
# my_string_2 = "test strIng".upper()


# for symbol in my_string:
#     if symbol.lower() in "eyuioa" and symbol.isupper():
#         print(symbol)

# for index in range(len(my_string)):
#     if not index %2:
#         print(index, my_string[index])

# for index, symbol in enumerate(my_string):
    # print(index, symbol)
    # if not index % 2:
    #     print(index, symbol)



# кортежи

# my_typle = (1, 2, 3, 4, "123", True) # не изменяемый тип
# print(type(my_typle), my_typle)
# print(my_typle[1:4])
#
# point = (2, 4, -7)
# x_0 = point[0]
# print([x_0])
# x_0 +=2
# point = (x_0, point[1], point[2])
# print(point)
###################################################################

# my_typle = list(my_typle)
# my_typle[-1] = -1
# my_typle = typle(my_typle)

##############################################################

# списки

# my_list = (1, 2, (3, 4), "123", True) # изменяемый тип
# print(type(my_list), my_list)
# print(my_list [0])
#
# point = [2, 4, -7]
# x_0 = point[0]
# print([x_0])
# point[0] = x_0
# print(point)
######################################################
# my_list = (1, 2, (3, 4), "123", True)
# for value in my_list:
#     if type(value) not in (str, int):
#         print(value)


new_list = []

for number in range(1,6):
    value = number ** 2
    new_list.append(value)

print(new_list)