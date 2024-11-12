
def calculate_average (list_a):
    if list_a == []:
        print(0)
        return 0


    num = 0 # sum the numbers in array
    num2 = 0 # sum how many instance are in list
    for i in list_a:
        num += i
        num2 += 1
    return num / num2

numbers = []
calculate_average(numbers)


