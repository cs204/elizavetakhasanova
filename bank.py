def main() :
    a = input("Приветствие: ")
    a = a.lower()
    match a:
        case "Здравствуйте"| "здравствуй , человек":
            print( "$0" )
        case "здрасте":
            print (" $20 ")
        case _:
            print ( " $100 ")

main()