prompt = "\nPlease enter add, remove, view, or quit to interact with To-Do List: "
todo_list =[]

def add_item(todo_list):
    todo_list = list(todo_list)
    try:
        name = str(input("Please enter to-do item: "))
        if name:
            print(todo_list)
            todo_list.append(name)
            print(todo_list)
        else:
            print("please enter a non empty value")
    except EOFError:
        print("please enter a valid input with no End of File characters")
    else:
        print("item added.")
    finally:
        return todo_list

def view_items(todo_list):
    if not todo_list:
        print("To-do list is empty")
    else:
        for val in todo_list:
            print(val)

def remove_movie(todo_list):
    todo_list = list(todo_list)
    try:
        name = input("Please enter item to remove: ")
        todo_list.remove(name)
    except EOFError:
        print("please enter a valid input with no End of File characters")
    except ValueError:
        print("please enter an item contained in the to-do list to remove")
    else:
        print("item removed.")
    finally:
        return todo_list

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    elif message == 'add':
        todo_list = add_item(todo_list)
    elif message == 'remove':
        todo_list = remove_movie(todo_list)
    elif message == 'view':
        view_items(todo_list)
    else:
        print("please enter a valid command")