def add_to_list(list_item):
    todo_list = []
    todo_list.append(list_item)
    for index, item in enumerate(todo_list):
        print(f"{index+1}. {item}")


while True:
    print("What do you need to get done?")
    add_to_list(input(""))
    if add_to_list() == "0":
        break