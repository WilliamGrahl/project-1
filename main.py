import pickle
from item import Item

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

def add_to_list():
    print("\nWhat do you want to add? \n")
    myAnswer8 = input()
    The_List.append(myAnswer8)
    print()
    for index, todo in enumerate(The_List):
        print(index+1,". ", todo)
    print()

def delete_from_list():
    print("\nWhich item do you want to delete? type in the number of the item \n")
    while True:
        try:
            myAnswer7 = int(input())
            del The_List[myAnswer7-1]
            print()
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
            print("\nWhich item do you want to move? type in the number of the item \n")
            myAnswer5 = int(input())
            print("\nNow type in the number you want to move it to \n")
            myAnswer6 = int(input())
            index_to_move = myAnswer5 - 1
            element = The_List.pop(index_to_move)
            new_position = myAnswer6 - 1
            The_List.insert(new_position, element)
            print()
            for index, todo in enumerate(The_List):
                print(index+1,". ", todo)
            print()
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
        for index, task in enumerate(results):
            print(index + 1, ". ", task)
    else:
        print("No matching tasks found.")

def search_in_list():
    print("\nEnter your search query with text or with 🔴, 🟡, 🟢: \n")
    search_query = input().strip()
    search_results = search_task(search_query)
    display_search_results(search_results)

def priority_in_list():
    while True:
        try:
            print("\nEnter the number of the item you want to set a priority level on: \n")
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
            for index, todo in enumerate(The_List):
                print(index+1, ". ", todo)
            print()
            break
        except (IndexError, ValueError):
            print("Invalid input. Please enter a valid number.")
            continue

def sort_list():
    priority_mapping = {'🔴': 4, '🟡': 3, '🟢': 2, '': 1}
    swapping = True
    end = len(The_List)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return The_List


def other():
    while True:
        try:
            print("\nWhat option do you want to choose? Type the number \n")
            print("1. Search")
            print("2. Set priority levels")
            print("3. Sort list in priorities")
            print()
            myAnswer4 = int(input())
            if myAnswer4 == 1:
                search_in_list()
            elif myAnswer4 == 2:
                priority_in_list()
            elif myAnswer4 == 3:
                sort_list()
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
        for index, todo in enumerate(The_List):
            print(index+1,". ", todo)
        print()
        print("Do you want to add, delete or move something in your list?")
        print("For other options type other \n")
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
                            for index, todo in enumerate(The_List):
                                print(index+1,". ", todo)
                            print()
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