# def my_function(*args: int):
#     for arg in args:
#         print(arg, end=" ")
#     print("\n===========")
# #
# # my_function(1, 2, 3)
# # my_function(1, 2, 3, 4, 5)
# my_function()


def find_max(*args):
    if not args:
        return "No numbers were given"
    i = 0
    for arg in args:
        if arg > i:
            i = arg
    return i

max_number = find_max()
print (max_number)


