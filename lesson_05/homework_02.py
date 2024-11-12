num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# result = ("The larger number is: " +  str(num1)) if num1 > num2  else ("The larger number is: " +  str(num2))
# print (result)

max_value = num1 if num1 > num2 else num2
print("The larger number is:", max_value)