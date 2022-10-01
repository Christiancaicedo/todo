todo_list = []
while True:
    print("What do you need to do?")
    add_todo = input("")
    todo_list.append(add_todo)
    for item in todo_list:
        if item == f"{add_todo} completed":
            del item
        else:
            convert_to_string = ""
            for i in todo_list:
                convert_to_string += i

    print(convert_to_string)
