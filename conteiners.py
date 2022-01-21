# 1
# x = [i*i*i for i in range(0, 100, 5)]
# print(x)
# print(max(x))

# 2
# x = [i*i*i for i in range(0, 100, 5)]
# my_iter = iter(x)
# while True:
#     try:
#         print(next(my_iter))
#     except StopIteration:
#         break

# 3
# my_set = {i*i*i for i in range(0, 100, 5)}
# print(sum(my_set)/len(my_set))

# 4
# my_set = {i*i*i for i in range(0, 100, 5)}
# my_iter = iter(my_set)
# while True:
#     try:
#         print(next(my_iter))
#     except StopIteration:
#         break

# 5
# x = tuple(i*i*i for i in range(0, 100, 5))
# print(len(x))

# 6
# x = tuple(i*i*i for i in range(0, 100, 5))
# my_iter = iter(x)
# while True:
#     try:
#         print(next(my_iter))
#     except StopIteration:
#         break

# 7
# def my_gen():
#     n = 1
#     yield n
#
#     n += 1
#     yield n
#
#     n += 1
#     yield n
#
#     n += 1
#     yield n
#
#     n += 1
#     yield n
#
#
# x = my_gen()
# for i in range(5):
#     print(next(x))
