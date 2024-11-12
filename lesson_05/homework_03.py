month = input("Enter a month: ")
match month:
    case "December" | "January" | "February":
        print("Season: Winter")
    case "March" | "April" | "May":
        print ("Season: Spring")
    case "June" | "July" | "August":
        print ("Season: Summer")
    case "September" | "October" | "November":
        print("Season: Autumn")
    case _:
        print ("Invalid month")