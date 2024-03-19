print("My do list \n")
The_List = []
while True:
    print("Do you want to add or delete something to your list? Add/remove")
    didChange = False
    number = 0
    myAnswer = input()
    if myAnswer.lower() == "add":
        print("What do you want to add?")
        myAnswer2 = input()
        The_List.append(myAnswer2)
        number += 1
        didChange = True
        for (index, todo) in enumerate(The_List):
            print(index+1, todo)
    elif myAnswer.lower() == "remove":
        number -= 1
        print("Which item do you want to remove? type in the number of the item")
        myAnswer3 = int(input())
        del The_List[myAnswer3-1]
        didChange = True
        for (index, todo) in enumerate(The_List):
            print(index+1, todo)
    else:
        print("Im sorry, I don't understand")

    if didChange == True:
        print("Do you want to exit? y/n")
        myAnswer4 = input()
        if myAnswer4.lower() == "y":
            print("Okey, Bye!")
            for (index, todo) in enumerate(The_List):
                print(index+1, todo)
            exit()
        else:
            continue