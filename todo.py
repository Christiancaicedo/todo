todo_list = []

def add_to_list(list_item: str) -> list:
    """Function adds item to the to-do list

    Args:
        list_item (str): Takes string input from user

    Returns:
        list: Appends to-do list to add item to be completed
    """
    todo_list.append(list_item.capitalize())
    for index, item in enumerate(todo_list):
            print(f"{index+1}. {item}")
            

def remove_from_list(item_to_remove: str) -> list:
    """Removes item from list

    Args:
        item_to_remove (str): String input from user of item to remove

    Returns:
        list: Updated to-do list with requested item removed
    """
    if item_to_remove.casefold() in todo_list:
        todo_list.remove(item_to_remove)
        print(f"{item_to_remove} has been removed from your to-do list")
        print(enumerate(todo_list))
        print()


while True:
    user_input = input("What do you need to get done?\n")
    if user_input.casefold() == 'close':
        break
    elif 'remove' in user_input.casefold():
        remove_from_list(user_input[7:])
    else:
        add_to_list(user_input)
        # todo_list.append(user_input.capitalize())
        # for index, item in enumerate(todo_list):
        #     print(f"{index+1}. {item}")