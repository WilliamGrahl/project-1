print("My to do list \n")
The_List = []
didChange = False

while True:
    print("Do you want to add, delete or move something in your list?")
    for index, todo in enumerate(The_List):
        print(index+1,". ", todo)
    myAnswer = input()

    if myAnswer.lower() == "add":
        print("What do you want to add? \n")
        myAnswer2 = input()
        The_List.append(myAnswer2)
        didChange = True
        for index, todo in enumerate(The_List):
            print(index+1,". ", todo)

    elif myAnswer.lower() == "delete":
        print("Which item do you want to delete? type in the number of the item \n")
        myAnswer3 = int(input())
        del The_List[myAnswer3-1]
        didChange = True
        for index, todo in enumerate(The_List):
            print(index+1,". ", todo)

    elif myAnswer.lower() == "move":
        print("Which item do you want to move? type in the number of the item \n")
        myAnswer4 = int(input())
        print("Now type in the number you want to move it to \n")
        myAnswer5 = int(input())
        index_to_move = myAnswer4 - 1
        element = The_List.pop(index_to_move)
        new_position = myAnswer5 - 1
        The_List.insert(new_position, element)
        didChange = True
        for index, todo in enumerate(The_List):
            print(index+1,". ", todo)

    else:
        print("Im sorry, I don't understand \n")

    if didChange == True:
        print("Do you want to exit? y/n \n")
        myAnswer6 = input()
        if myAnswer6.lower() == "y":
            print("Okey, Bye! \n")
            for index, todo in enumerate(The_List):
                print(index+1,". ", todo)
            break
        else:
            didChange = False