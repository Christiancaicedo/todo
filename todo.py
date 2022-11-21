import atexit
import os.path
import os

todo_list = []
filename = "store_list.txt"
t_list = "That task is not on the list"


if os.path.exists('store_list.txt'):
    # print("Welcome back. Here is your current to-do list:")
    with open(filename, 'r', encoding='utf-8') as txt_file:
        if os.stat('store_list.txt').st_size == 0:
            pass
        else:
            print("Welcome back. Here is your current to-do list:")
            for index, item in enumerate(txt_file):
                strip_item = item.rstrip('\n')
                todo_list.append(strip_item)
                print(f"{index+1}. {strip_item}")
        print()
else:
    pass


def add_to_list(item_to_add: str) -> list:
    """Function adds item to the to-do listd

    Args:
        list_item (str): Takes string input from user

    Returns:
        list: Appends to-do list to add item to be completed
    """
    strip_item = item_to_add.lstrip(" ").capitalize()
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


def clear_list(clear: list) -> list:
    """Clear all items in current to-do list"""
    while todo_list:
        todo_list.pop()
    print()
    print("Your to-do list has been cleared")
    print()


def store_list(item_list: list) -> list:
    """Create/update a txt file where program is stored. Txt file will store the users
    current to-do list once the program exits using "close" or any other way to exit within Python. 
    """
    filename = "store_list.txt"
    with open(filename, "w", encoding="utf-8") as txt_file:
        for item in item_list:
            print(item, file=txt_file)


# For loop that requests a users input to add or remove task to list.
# The loop will accept "clear" or "clear list" to remove everything from
# to-do list.

# "add:..." will add an item to the list "remove:..." will remove an
# item from the list. Capitalization does not matter. Intended action
# and item being added/removed must be separated by a colon(:)

# ex. add: coding
# ex. remove: coding
# ex. clear
# ex. clear list

while True:
    user_input = input("What do you need to get done?\n")
    if user_input.casefold() == 'close':
        break

    if ':' in user_input:
        command, task = user_input.casefold().split(':')
        if command == 'add':
            add_to_list(task.casefold())
        elif command == 'remove':
            remove_from_list(task.casefold())
        # elif command.casefold() == 'clear list' or 'clear':
        #     clear_list(command.casefold())
        else:
            print()
            print(f"{t_list}_^10")
            print()
    elif user_input.casefold() == "clear" or user_input.casefold() == "clear list":
        clear_list(user_input)
        store_list(todo_list)
    else:
        print()
        print("That input is not acceptable. Please specify if you are adding, removing or clearing the list.")
        print()

atexit.register(store_list, todo_list)
