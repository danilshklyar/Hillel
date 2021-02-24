# Добавление [1, 10, 2, 20, 3, 30, 4, 40, 5, 50] из списка. Равное количество значений в списках
# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [10, 20, 30, 40, 50]
#
# my_result = []
# list_len = len(my_list_1)
# for index in range(list_len):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# print(my_result)
####################################################################################
# Не равное количество значений в списках
# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [10, 20, 30, 40, 50, 60, 70]
#
# my_result = []
# list_len = min(len(my_list_1), len(my_list_2)) # min выбирает список меньшей длинны из двух
# for index in range(list_len):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# tail = my_list_2[list_len:]
# my_result.extend(tail)
# print(my_result)
################################################################################################
# Не равное количество значений в списках второй вариант
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 20, 30, 40, 50, 60, 70]

# my_result = []
# list_len = min(len(my_list_1), len(my_list_2)) # min выбирает список меньшей длинны из двух
# if len(my_list_2) < len(my_list_1):
#     my_list_2, my_list_1 = my_list_1, my_list_2
# for index in range(list_len):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# tail = my_list_2[list_len:]
# my_result += tail
# print(my_result)
#########################################
# Смена значений местами
# a = 5
# b = 6
# a, b = b, a
# print(a, b)


