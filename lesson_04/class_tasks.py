# my_string = input("Enter your string: ")
# print(my_string[-1]+my_string[:-1])
from operator import contains

#my_string = input("Enter your string: ")
#print(my_string[1::2])
#word = input("enter a string ")
#print(word.upper())
string  = input("enter a string ")
print(string[:3].upper() + string[3:-3].lower() + string[-3].upper())

