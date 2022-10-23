# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))

# 3. Define the type of each object from step 1.
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e))

# 4*. Check the type of the objects by using isinstance.
print("Is int-a an integer:", isinstance(int_a, int))
print("Is str_b a string:", isinstance(str_b, str))
print("Is set_c a set:", isinstance(set_c, set))
print("Is lst_d a list:", isinstance(lst_d, list))
print("Is dict_e a dict:", isinstance(dict_e, dict))

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(4, 7))

# 6. By passing index numbers into the curly braces.
print("Anna has {1} apples and {0} peaches.".format(8, 5))

# 7. By using keyword arguments into the curly braces.
print("Anna has {apples} apples and {peaches} peaches.".format(apples=6, peaches=9))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches.".format(7, 10))

# 9. With f-strings and variables
apples = 8
peaches = 11
print(f"Anna has {apples} apples and {peaches} peaches.")

# 10. With % operator
print("Anna has %s apples and %s peaches." % (9, 12))

# 11*. With variable substitutions by name (hint: by using dict)
data_dict = {"apples": 10, "peaches": 13}
print("Anna has %(apples)s apples and %(peaches)s peaches." % data_dict)

# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)

# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

# 12. Convert (1) to list comprehension
list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)

# 13. Convert (2) to regular for with if-else
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
