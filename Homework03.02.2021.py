value = input("Введи число: ")
value =int(value)
if value < 100:
    new_value = value / 2
    print(new_value)
else:
    print(value * -1)
##################################################
value = input("Введи число: ")
value =int(value)
if value < 100:
    new_value = 1
    print(new_value)
else:
    new_value = 0
    print(new_value)
####################################################
value = input("Введи число: ")
value =int(value)
if value < 100:
    new_value = True
else:
    new_value = False
print(new_value)
######################################################
my_str = input("Введи текст: ")
my_str = str(my_str)
print(my_str.upper())
#####################################################
my_str = input("Введи текст: ")
my_str = str(my_str)
print(my_str.lower())
#####################################################
my_str = input("Введи текст: ")
my_str = str(my_str)
if len(my_str) < 5:
    print(my_str * 2)
else:
    print(my_str)
########################################################
my_str = input("Введи текст: ")
my_str = str(my_str)
if len(my_str) < 5:
    print(my_str + my_str[::-1])
else:
    print(my_str)
