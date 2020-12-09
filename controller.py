import view
from todo import ToDo
import time

todo_list = []

def time_to_formatted_string(time_format):
    year = time_format[0]
    month = time_format[1]
    day = time_format[2]
    hour = time_format[3]
    my_min = time_format[4]

    return f'{year}-{month}-{day} {hour}:{my_min}'


def see_all_todos():
    view.see_all_todos()
    for index in range(len(todo_list)):
        todo = todo_list[index]
        time_created = time_to_formatted_string(todo.time_created)

        print(todo.description, time_created)


def create_todo():
    view.create_new_todo()
    new_description = input('> ')
    new_todo = ToDo(new_description, time.localtime())
    todo_list.append(new_todo)

def update_todos():
    view.update_todos()


def delete_todos():
    view.delete_todos()


def sub_menus(user_input):
    if user_input in '1':
        see_all_todos()
    elif user_input in '2':
        create_todo()
    elif user_input in '3':
        update_todos()
    elif user_input in '4':
        delete_todos()
    else:
        view.wrong_message()


def menu_choice():
    user_input = input('> ')
    if user_input in '1234':
        sub_menus(user_input)
        return True
    elif user_input in '5':
        view.bye_message()
        return False
    else:
        view.invalid_input()

    return True


todo_list.append(ToDo('To Do 1', time.localtime()))
todo_list.append(ToDo('To Do 2', time.localtime()))
todo_list.append(ToDo('To Do 3', time.localtime()))
run_program = True

while run_program:
    view.welcome_message()
    view.main_menu()
    run_program = menu_choice()


