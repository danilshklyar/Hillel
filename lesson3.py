# if условие
#     блок действий если условие да

#elif условие 2
#     блок действий если условие 2 да

#else
#     блок действий если условие нет
#############################################

# if 4 > 20:
#     print("4>2")
#
# value = int(input("Какая теипература"))
# if value < 0:
#     print("Одень шапку")
# else:
#     print("шапку можно не надевать")
##################################################

# value = int(input("Какая теипература"))
# if value >= 0:
#     result = 1
# else:
#     result = -1
#
# result = 1 if value >=0 else -1
# print(result)


##############################################

# цикл while
# value = input("ВВеди что-то")

# break выход из текущего цикла

# while not value:
#     value = input("Введи что-то")
#
#     print("ок")

# from random import randint
# goal = randint(1, 100)
# print(goal)


# from random import randint
# goal = randint(1, 10)
# value = int(input("Угадай число"))
# done = False
#
# while not done:
#     if value > goal
#         value = int(input("Попробуй снова"))
#     elif value < goal
#
#########################################3

# Форматирование строк

# my_str = "qwerty"
# print("my_str=" , my_str)
#
# path = "/home/v2/test"
# filename = "python_test.py"
# full_path = f"{path}/{filename}"
# print(full_path)

##################################################################

# path = "/home/v2/test"
# filename = "python_test.py"
# full_path = f"{path}/{filename}"
# print(full_path[-2])
# print(len(full_path))

###########################################################

path = "/home/v2/test"
filename = "python_test.py"
full_path = f"{path}/{filename}"
print(len(full_path))
print(full_path[2:6])              #правый край не берется

path = "/home/v2/test"