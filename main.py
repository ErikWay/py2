new_list = [1, 3, 54, 5, 7.32, 6.3, 1.6, 7]
k = 0
count_int = 0
count_float = 0
while k < len(new_list):
    if new_list[k] == int(new_list[k]):
        count_int += 1
    elif new_list[k] == float(new_list[k]):
        count_float += 1
    k += 1
print("int: ", count_int, "float: ", count_float)




