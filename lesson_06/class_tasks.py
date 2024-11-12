original_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


print(f"Using Regular function: {get_even_numbers(original_numbers)}")

#numbers = [1, 2, 3, 4, 5, 6]
#even_numbers =
#
# (filter(lambda x: x % 2 == 0, numbers))
#print(even_numbers)

#squared_numbers_list = list(map(lambda x : x ** 2, even_numbers))
#print(squared_numbers_list)
