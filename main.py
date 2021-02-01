#хайноская башня

# def tower(height, from_column, to_column, tmp_column):
#     if height == 1:
#         print(f'From {from_column} to {to_column}')
#     else:
#         tower(height-1, from_column, tmp_column, to_column)
#         print(f'From {from_column} to {to_column}')
#         tower(height-1, tmp_column, to_column, from_column)
#
# tower(4, 'A', 'B', 'C')

#praktika


# data = input('Write some numbers: ')
# NUMBERS = '1234567890, '
#
# def is_valid(data):
#     for value in data:
#         # value.isdigit() and value != ',':
#         #     return False
#         if value not in NUMBERS:
#             return False
#     return True
#


# def to_list(data):
#     return data.split(',')
#
# if is_valid(data):
#     result = to_list(data)
#     print(result)
# else:
#     print('Value is not valid')
#
# print(is_valid(data))


# n = 1348329874628
#
# def some_numbers(n):
#     n = str(n)
#     result + 0
#     for item in n:
#         result = result + int(item)
#
#     return result


#
# string = 'asdlopksaopd123432423okspo'
#
# print(string.count('2'))


#
# lst1 = [1,2,3,5,2,5,2,4]
# print(lst1[::-1])


#
# MAX_SIZE = 5
# lst = []
#
# def queue(lst, value):
#     if len(value) > MAX_SIZE:
#         return
#
#     free_space = MAX_SIZE - len(lst)
#     need_remove = len(value) - free_space
#     for counter in range(need_remove):
#         lst.pop()
#
#     lst.extend(value)
#
# a = [1,2,3,4,5]
# b = [1,2,3,4,5]
# queue(a, b)
#
# queue([1,2,3,4,5], [1,2,3,4,5])
#
# print(a)
#


# def max_del(a):
#     b = a
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#


# def  cycle(lst, step):
#
#     if step < 0:
#         step = abs(step)
#         for _ in range(step):
#             tmp = lst.pop()
#             lst.insert(0, tmp)
#     else:
#         for _ in range(step):
#             tmp = lst.pop(0)
#             lst.append(tmp)


# def is_dupl(lst):
#     for index, value in enumerate(lst):
#         if value in lst[index+1:]:
#             return True
#     return False



# def replace_20(lst):
#     for item in lst:
#         if item == 20:
#             idx = lst.index(item)
#             lst[idx] = 200
#             return



# def remove_empty(lst):
#
#     for idx, item in enumerate(lst):
#         if item == '':
#             lst.pop(idx)
#

