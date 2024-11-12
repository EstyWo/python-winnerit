
age = int(input("Enter your age: "))

has_ticket = input("Do you have a ticket? (yes/no) ").lower() == 'yes'

has_permission = input("Do you have special permission? (yes/no) ").lower() == 'yes'


if age >= 18 and has_ticket:
    print ("You can enter the club")

elif age >= 18 and not has_ticket:
    print("You can't enter the club without a ticket")

elif age < 18 and has_permission:
        print("You can enter the club with special permission")

else:
        print("You can't enter the club")

