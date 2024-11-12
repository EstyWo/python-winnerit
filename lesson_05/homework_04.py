total = 0
count = 5

for i in range(count):
    number = float(input(f"Enter number {i + 1}: "))
    total += number

average = total / count

print("The average is:", average)


# num_array = []
# num1 = int(input("Enter number 1: "))
# num_array.append(num1)
# num2 = int(input("Enter number 2: "))
# num_array.append(num2)
# num3 = int(input("Enter number 3: "))
# num_array.append(num3)
# num4 = int(input("Enter number 4: "))
# num_array.append(num4)
# num5 = int(input("Enter number 5: "))
# num_array.append(num5)
# print (num_array)
#
# tempAverage = 0
# for num in num_array:
#     tempAverage +=num
# tempAverage = tempAverage / len(num_array)
# print (tempAverage)
