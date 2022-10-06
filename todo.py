from audioop import add


todo_list = []
while True:
    print("What do you need to do?")
    add_todo = input("")
    todo_list.append(add_todo)
    for item in todo_list:
        print(item)
    print()

    if add_todo == f"{add_todo} completed":
        del add_todo
        print(todo_list)
