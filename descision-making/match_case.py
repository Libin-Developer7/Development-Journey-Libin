option = int(input("press 1 for tear press 2 for coffee press 3 for without sugar "))
match option:
    case 1:                                # case 'value for option'
        print("you chose tea")
    case 2:
        print("you chose coffee")
    case 3:
        print("you chose without sugar")
    case _:
        print("invalid")