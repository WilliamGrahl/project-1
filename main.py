import pickle

def load_data_with_pickle(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        print("Data loaded successfully from", filename)
        return data
    except Exception as e:
        print("An error occurred:", e)
        return None

The_List = load_data_with_pickle("saved_data.pkl")
if The_List is None:
    The_List = []

print("My to do list \n")

def add_to_list():
    print("What do you want to add? \n")
    while True:
        try:
            myAnswer2 = input()
            The_List.append(myAnswer2)
            for index, todo in enumerate(The_List):
                print(index+1,". ", todo)
            print()
            break
        except (IndexError, ValueError):
            print("Invalid input. Please enter a valid number.")
            continue

def delete_from_list():
    print("Which item do you want to delete? type in the number of the item \n")
    while True:
        try:
            myAnswer3 = int(input())
            del The_List[myAnswer3-1]
            for index, todo in enumerate(The_List):
                print(index+1,". ", todo)
            print()
            break
        except (IndexError, ValueError):
            print("Invalid input. Please enter a valid number.")
            continue

def move_from_list():
    while True:
        try:
            print("Which item do you want to move? type in the number of the item \n")
            myAnswer4 = int(input())
            print("Now type in the number you want to move it to \n")
            myAnswer5 = int(input())
            index_to_move = myAnswer4 - 1
            element = The_List.pop(index_to_move)
            new_position = myAnswer5 - 1
            The_List.insert(new_position, element)
            for index, todo in enumerate(The_List):
                print(index+1,". ", todo)
            print()
            break
        except (IndexError, ValueError):
            print("Invalid input. Please enter a valid number.")
            continue

def save_data_with_pickle(data, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        print("Data saved successfully to", filename)
    except Exception as e:
        print("An error occurred:", e)

def main():
    while True:
        print("Do you want to add, delete or move something in your list? \n")
        for index, todo in enumerate(The_List):
            print(index+1,". ", todo)
        print()
        myAnswer = input()

        if myAnswer.lower() == "add":
            add_to_list()
            didChange = True

        elif myAnswer.lower() == "delete":
            delete_from_list()
            didChange = True

        elif myAnswer.lower() == "move":
            move_from_list()
            didChange = True

        else:
            print("Im sorry, I don't understand \n")
            didChange = False

        if didChange == True:
            while True:
                print("Do you want to exit? y/n \n")
                myAnswer2 = input()
                if myAnswer2.lower() == "y":
                    while True:
                        print("Do you want to save? \n")
                        myAnswer3 = input()
                        if myAnswer3.lower() == "y":
                            save_data_with_pickle(The_List, "saved_data.pkl")
                            print("Okey, Bye! \n")
                            for index, todo in enumerate(The_List):
                                print(index+1,". ", todo)
                            print()
                            exit()
                        elif myAnswer3.lower() == "n":
                            print("Okey, Bye! \n")
                            for index, todo in enumerate(The_List):
                                print(index+1,". ", todo)
                            print()
                            exit()
                        else:
                            print("Invalid input. Please enter 'y' or 'n'. \n")
                            continue
                elif myAnswer2.lower() == "n":
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'. \n")

main()