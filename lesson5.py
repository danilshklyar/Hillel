# sort, sorted

# ages = [12, 34, 23, 55, 11, 4]
#
# ages.sort()
#
# print(ages)

##########################################

# ages = [12, 34, 23, 55, 11, 4]
# ages_sort = ages.copy()
# ages_sort.sort()
#
# print(ages, ages_sort)

#############################################

# ages = [12, 34, 23, 55, 11, 4]
# ages_sort = sorted(ages)
# print(ages, ages_sort)

############################################

# ages = [12, 34, 23, 55, 11, 4]
# ages_sort = sorted(ages)
# print(ages, ages_sort)
# value = ages.sort()
# print(">>>>", value)

###################################


# value = "34251"
#
# res = sorted(value)
# print(res)

###########################################

# value = "342abc51gfd+/"
# res = sorted(value)
# print(res)

############################################

# value = "342abc51gfd+/"
# print(ord("="), ord("a"))
# res = sorted(value)
# print(res)

########################################

# value = "342abc51gfd+/"
# print(chr(61), chr(98))

##########################################

# value = "342abc51gfd+/"
# res = sorted(value)
# print(res[::-1])

#############################################

# value = "342abc51gfd+/"
# res = sorted(value, reverse=True)
# print(res)
#
# value = "342abc51gfd+/"
# res = sorted(value, reverse=False)
# print(res)

################################################

# value = ["Name", 'Age', 'adress']
# res = sorted(value, reverse=False)
# print(res)

################################################

# value = ["Name", 'Age_q', 'Age_1', 'adress']
# res = sorted(value, reverse=False)
# print(res)

#############################################

# value = ["Name", 'Age_q', 'Age_1', 'adress']
# res = sorted(value, reverse=True, key=len)
# print(res)

###############################################


# Практическое

# my_str = "blablacar"
# my_symbol = "bla"
#
# count = my_str.count(my_symbol)
# print(count)

#############################################

# my_str = "blablacar"
# my_symbol = "bla"
# count = my_str.count(my_symbol)
# for qantity in range(count):
#     print(my_symbol)
#
# my_str = "blablacar"
# my_symbol = "bla"
# count = my_str.count(my_symbol)
# for _ in range(count):  # можно использовать _ в качестве переменной
#     print(my_symbol)

############################################
#
# my_str = "blablacar"
# my_symbol = "bla"
# response = f"{my_symbol}\n" * count
# print(response.strip())

################################################

# my_str = "bla BLA car"
# my_str = my_str.lower()
#
# result = []
# result_str = ""
#
# for symbol in my_str:
#     if symbol in result:
#         # result.append(symbol)
#         result_str += symbol
# print(result)


#######################################################

# my_str = "hgfdfghgfd    fghgfd     hgf"
# my_list = []
# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbol)
# print(my_list)

##################################################

# my_str = "hgfdfghgfd    fghgfd     hgf"
# my_list = []
# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbol)
# print(my_list, id(my_list))
#
# my_list= list(my_str) [::2]
# print(my_list, id(my_list))
############################################################
# my_str = "hgfdfghgfd    fghgfd     hgf"
# my_list = []
# my_list.extend(list(my_str) [::2])
# print(my_list, id(my_list))

##############################################################

# my_str = "hgfdfghgfd    fghgfd     hgf"
# print(len(my_str))
# str_index = [2, 23, 5, 27, 17, 0]
# my_list = []
# for index in str_index:
#     value = my_str[index]
#     my_list.append(value)
# print(my_list)

##############################################################

# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [10, 20, 30, 40, 50]
# result = my_list_1[::2] + my_list_2[1::2]
# print(result)
##############################################
# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [10, 20, 30, 40, 50]
# result = []
# print(id(result))
# result += my_list_1[::2]
# result += my_list_2[1::2]
# print(id(result), result)
##################################################

# nunber = 123467894341354154163541635416354163541653416534165342
# res = len(str(nunber))
# print(res)
#
#
# nunber = 123467894341354154163541635416354163541653416534165342
# res = max(str(nunber))
# print(res)
#
# my_str = "ghfjdklkfgjhfjdkfjhjdkfghfjdkjhgfjdk"
# res = max(str(my_str))
# print(res)
#
# nunber = 123467894341354154163541635416354163541653416534165342
# nunber = sorted(str(nunber))
# print(nunber)
#
# nunber = 123467894341354154163541635416354163541653416534165342
# nunber = int("".join(sorted(str(nunber))))
# print(nunber)


#####################################################################








