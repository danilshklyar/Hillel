# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

my_list = [100, 50, 200, 300, 20]
for number in my_list:
    if number > 100:
        print(number)


######################################################################################
# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = [100, 50, 200, 300, 20]
my_result =[]
for number in my_list:
     if number > 100:
         my_result.append(number)
print(my_result)


################################################################################

# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)


my_list = [100, 50, 200, 300, 20]
symbol = len(my_list)
if symbol < 2:
    my_list.append(0)
    print(my_list)
else:
    my_list.append(my_list[-2] + my_list[-1])
    print(my_list)

##################################################################

# 4) Пользователь вводит value - число с запятой (например 3.14) с клавиатуры.
# Вы приводите это value к типу float и выводите результат выражения value ** -1.
# Написать программу, которая вычисляет данное выражение и
# корректно обрабатывает возможные исключения.

value = input("Введи число: ")
try:
    value = float(value)
    values = value ** -1
    print(values)
except (ValueError, TypeError, ZeroDivisionError):
    print("Не верный ввод")

########################################################################

# 5) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения из my_list для которых сумма индекса и значения будет четной.
# Пример. [1,11,20,100]
# Ответ [11, 20], потому что индекс 1 + значение 11 это 12 - четное, индекс 2 + значение 20 это 22 - четное

my_list = [1,11,20,100]
my_results = []
for symbol in range(len(my_list)):
    if (symbol + my_list[symbol]) % 2 == 0:
        my_results.append(my_list[symbol])
print(my_results)

##############################################################################

# 6) У вас есть два списка my_list_1 и my_list_2 равной длинны.
# Распечатать пары значений из my_list_1 и my_list_2 через обращение по индексу (можно range, можно enumerate).
# Например для списков [1, 3] и [2, 4]:
# (1, 2)
# (3, 4)

my_list_1 = [1, 3]
my_list_2 = [2, 4]
my_tuple = []
for symbol in range(len(my_list_1)):
    print(my_list_1[symbol], my_list_2[symbol])

#############################################################################################

# 7) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов .
# Генерирование через range или другие "фишки" я засчитывать не буду ))

my_list = [1, 2, 3, 4, 5]
for symbol in range(1,99):
    my_list.append(symbol)
print(my_list)

#  Вложенные циклы не осилил(
















