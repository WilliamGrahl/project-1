import pickle

def load_data_with_pickle(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data
    except Exception as e:
        print("An error occurred:", e)
        return None

The_List = load_data_with_pickle("saved_data.pkl")
if The_List is None:
    The_List = []

print("My to do list \n")

def print_list():
    for index, todo in enumerate(The_List):
        print(index+1,". ", todo)
    print()

def add_to_list():
    print("\nWhat do you want to add? \n")
    myAnswer8 = input()
    The_List.append(myAnswer8)
    print()
    for index, todo in enumerate(The_List):
        print(index+1,". ", todo)
    print()

def delete_from_list():
    print("\nWhich item do you want to delete? type in the number of the item: \n")
    while True:
        try:
            myAnswer7 = int(input())
            del The_List[myAnswer7-1]
            print()
            print_list()
            break
        except (IndexError, ValueError):
            print("Invalid input. Please enter a valid number.")
            continue

def move_from_list():
    while True:
        try:
            print("\nWhich item do you want to move? type in the number of the item: \n")
            myAnswer5 = int(input())
            print("\nNow type in the number you want to move it to: \n")
            myAnswer6 = int(input())
            index_to_move = myAnswer5 - 1
            element = The_List.pop(index_to_move)
            new_position = myAnswer6 - 1
            The_List.insert(new_position, element)
            print()
            print_list()
            break
        except (IndexError, ValueError):
            print("Invalid input. Please enter a valid number.")
            continue

def search_task(query):
    matching_tasks = [task for task in The_List if query.lower() in task.lower()]
    return matching_tasks

def display_search_results(results):
    if results:
        print("Search Results: \n")
        for index, todo in enumerate(results):
            print(index+1,". ", todo)
        print()
    else:
        print("\nNo matching tasks found. \n")

def search_in_list():
    print("\nEnter your search query with text or with 🔴, 🟡, 🟢: \n")
    search_query = input().strip()
    search_results = search_task(search_query)
    display_search_results(search_results)

def priority_in_list():
    while True:
        try:
            print("\nWhich item you want to set a priority level on? type in the number of the item: \n")
            for index, todo in enumerate(The_List):
                print(index+1, ". ", todo)
            print()
            myAnswer8 = int(input())
            index_to_mark = myAnswer8 - 1
            print("\nEnter priority level (high, medium, low or none): \n")
            myAnswer9 = input()
            if myAnswer9.lower() == "high":
                The_List[index_to_mark] = f"{The_List[index_to_mark].replace('🔴', '').replace('🟡', '').replace('🟢', '')} 🔴"
            elif myAnswer9.lower() == "medium":
                The_List[index_to_mark] = f"{The_List[index_to_mark].replace('🔴', '').replace('🟡', '').replace('🟢', '')} 🟡"
            elif myAnswer9.lower() == "low":
                The_List[index_to_mark] = f"{The_List[index_to_mark].replace('🔴', '').replace('🟡', '').replace('🟢', '')} 🟢"
            elif myAnswer9.lower() == "none":
                The_List[index_to_mark] = The_List[index_to_mark].replace('🔴', '').replace('🟡', '').replace('🟢', '')
            else:
                print("Invalid input. Please enter 'high', 'medium', 'low' or 'none'.")
                continue
            print("\n Priority level updated successfully.")
            print_list()
            break
        except (IndexError, ValueError):
            print("Invalid input. Please enter a valid number.")
            continue

def sort_by_priority():
    global The_List

    The_new_List = sorted(The_List, key=lambda x: 3 if '🔴' in x else (2 if '🟡' in x else (1 if '🟢' in x else 0)), reverse=True)
    print("\nSorted list based on priority:")
    for index, task in enumerate(The_new_List):
        print(index + 1, ". ", task)
    print()
    The_List = The_new_List

def edit_list():
    while True:
        try:
            print("\nWhat item do you want to edit? Type the number of the item: \n")
            print_list()
            myAnswer10 = int(input())
            index_to_edit = myAnswer10 - 1
            if 0 <= index_to_edit < len(The_List):
                print("\nCurrent text:", The_List[index_to_edit])
                print("\nEnter the new text for the task: \n")
                new_text = input()
                The_List[index_to_edit] = new_text
                print("\nEnter priority level (high, medium, low or none): \n")
                myAnswer9 = input()
                if myAnswer9.lower() == "high":
                    The_List[index_to_edit] = f"{The_List[index_to_edit].replace('🔴', '').replace('🟡', '').replace('🟢', '')} 🔴"
                elif myAnswer9.lower() == "medium":
                    The_List[index_to_edit] = f"{The_List[index_to_edit].replace('🔴', '').replace('🟡', '').replace('🟢', '')} 🟡"
                elif myAnswer9.lower() == "low":
                    The_List[index_to_edit] = f"{The_List[index_to_edit].replace('🔴', '').replace('🟡', '').replace('🟢', '')} 🟢"
                elif myAnswer9.lower() == "none":
                    The_List[index_to_edit] = The_List[index_to_edit].replace('🔴', '').replace('🟡', '').replace('🟢', '')
                else:
                    print("Invalid input. Please enter 'high', 'medium', 'low' or 'none'.")
                    continue
                print("\nTask updated successfully.")
                print_list()
                break
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

def other():
    while True:
        try:
            print("\nWhat option do you want to choose? Type the number: \n")
            print("1. Search")
            print("2. Set priority levels")
            print("3. Sort list by priorities")
            print("4. Edit")
            print()
            myAnswer4 = int(input())
            if myAnswer4 == 1:
                search_in_list()
            elif myAnswer4 == 2:
                priority_in_list()
            elif myAnswer4 == 3:
                sort_by_priority()
            elif myAnswer4 == 4:
                edit_list()
            else:
                print("Invalid input. Please choose from the available options.")
                continue
            break
        except (ValueError):
            print("Invalid input. Please enter a valid number.")
            continue

def save_data_with_pickle(data, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        print("\nData saved successfully to", filename)
    except Exception as e:
        print("An error occurred:", e)

def main():
    didChange = False
    while True:
        print_list()
        print("Do you want to add, delete or move something in your list?")
        print("For other options type 'other': \n")
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

        elif myAnswer.lower() == "other":
            other()
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
                        print("\nDo you want to save? y/n \n")
                        myAnswer3 = input()
                        if myAnswer3.lower() == "y":
                            save_data_with_pickle(The_List, "saved_data.pkl")
                            print()
                            print_list()
                            exit()
                        elif myAnswer3.lower() == "n":
                            print("Okey, Bye! \n")
                            exit()
                        else:
                            print("Invalid input. Please enter 'y' or 'n'. \n")
                            continue
                elif myAnswer2.lower() == "n":
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'. \n")

main()