import atexit

todo_list = []
filename = "store_list.txt"
t_list = "That task is not on the list"

with open(filename, 'r', encoding='utf-8') as txt_file:
    if txt_file != "":
        print("Welcome back. Here is your current to-do list:")
        
    for index, item in enumerate(txt_file):
        if item == "":
            pass
        else:
            todo_list.append(item.rstrip('\n'))
            print(f"{index+1}. {item}")


def add_to_list(list_item: str) -> list:
    """Function adds item to the to-do list

    Args:
        list_item (str): Takes string input from user

    Returns:
        list: Appends to-do list to add item to be completed
    """
    strip_item = list_item.lstrip(" ").capitalize()
    todo_list.append(strip_item)
    print()
    print(f"{strip_item} has been added to your to-do list")
    print("Here is your updated list:")
    for index, item in enumerate(todo_list):
            print(f"{index+1}. {item}")
    print()

            
def remove_from_list(item_to_remove: str) -> list:
    """Removes item from list

    Args:
        item_to_remove (str): String input from user of item to remove

    Returns:
        list: Updated to-do list with requested item removed
    """
    strip_item = item_to_remove.lstrip(" ").capitalize()
    if strip_item in todo_list:
        todo_list.remove(strip_item)
        print()
        print(f"{strip_item} has been removed from your to-do list")
        print("Here is your updated list:")
        for index, item in enumerate(todo_list):
            print(f"{index+1}. {item}")
        print()


def store_list(item_list: list) -> list:
    """Create/update a txt file where program is stored. Txt file will store the users
    current to-do list once the program exits using "close" or any other way to exit within Python. 
    """
    filename = "store_list.txt"
    with open(filename, "w", encoding="utf-8") as txt_file:
        for item in item_list:
            print(item, file=txt_file)
            

# def pull_stored_list(resume_list: list) -> list:
#     """Pulls the currently stored to-do list from a text file previously created/updated
#     when the original program was ended.
#     """
    # with open(filename, 'r', encoding='utf-8') as txt_file:
    #     for item in txt_file:


# For loop that requests a users input to add or remove task to list.
# "add:..." will add an item to the list "remove:..." will remove an
# item from the list. Capitalization does not matter. Intended action
# and item being added/removed must be separated by a colon(:)
# ex. add: coding
# ex. remove: coding
while True:
    user_input = input("What do you need to get done?\n")
    if user_input.casefold() == 'close':
        break
    
    command, task = user_input.casefold().split(':')
    if command == 'add':
        add_to_list(task.casefold())
    elif command == 'remove':
        remove_from_list(task.casefold())
    else:
        print()
        print(f"{t_list}_^10")
        print()
        
atexit.register(store_list,todo_list)