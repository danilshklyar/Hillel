# values = (1, 2, 3, 4, 5)
# values = list(values)
# print(type(values))
#######################################
# values = [1, 2, 3, 4, 5]
# values = tuple(values)
# print(type(values))
#######################################
# values = [1, 2, 3, 4, 5]
# result = []
# for value in values[::-1]:
#     result.append(value)
# print(result)
###################################
# values = [1, 2, 3, 4, 5]
# print(len(values))
######################################
# values = [1, 2, 3, 4, 5]
# new_values = values + values[::-1]
# print(new_values)
####################################
# values = [1, 2, 3, 4, 5]
# new_values = values
# new_values.append(6)
# print(new_values)
###################################
# values = [1, 2, 3, 4, 5]
# new_values = values.copy()
# new_values.append(6)
# print(new_values)
####################################3
# values = [0] * 6
# values[0] = 1
# print(values)
#######################################
# value = 0
# values = [value] * 6
# value = 1
# print(values)
###################################
# my_list = [0]
# values = [my_list] * 3
# print(values)
#######################################
# my_list = [0]
# values = [my_list] * 3
# my_list.append(1)
# print(values)
##################################
# my_list = [0]
# values = [my_list.copy()] * 3
# my_list.append(1)
# print(values)
#########################################
# my_list = ["a", "b", "c", "d", "i", "f"]
# my_str = " ".join(my_list)
# print(my_str)
###########################################
# my_list = ["a", "b", "c", "d", "i", "f"]
# my_str = "_".join(my_list)
# print(my_str)
###############################################
# my_list = ["a", "b", "c", "d", "i", "f"]
# my_str = "_".join(my_list[::-1])
# print(my_str)
#################################################
my_list = ["a", "b", "c", "d", "i", "f"]
my_str = "".join(my_list[::2])
print(my_str)