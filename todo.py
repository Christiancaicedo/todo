todo_list = []


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


t_list = "That task is not on the list"

# For loop that requests a users input to add or remove task to list.
# "add:..." will add an item to the list "remove:..." will remove an
# item from the list
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