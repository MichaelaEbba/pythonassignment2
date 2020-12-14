def welcome_message():
    print()
    print('To Do List')


def main_menu():
    print('''1.\t See all To Do's''')
    print('''2.\t Create new''')
    print('''3.\t Update''')
    print('''4.\t Delete ''')
    print('''5.\t Quit''')
    print('''Menu choice: ''')


def bye_message():
    print('Arrividerci')


def invalid_input():
    print('WRONG! Please enter a number 1-5')


def see_all_todos():
    print('All: ')


def create_new_todo():
    print('Create new')
    print('Enter new description')


def update_todos():
    print('Update')


def choose_todo():
    print('Choose todo to edit (0 to go back)')


def update_description_or_set_done():
    print('Update')
    print('1. Description')
    print('2. Set done')
    print('3. Set undone')
    print('0. Go back')


def new_description():
    print('Enter new description')


def set_done():
    print('Marked as done')


def set_undone():
    print('Marked as undone')


def delete_todos():
    print('Delete')


def choose_todo_delete():
    print('Choose todo number to delete (0 to go back)')


def deleted_todo_object(todo_object):
    print(f'{todo_object}, deleted')


def wrong_message():
    print('This went wrong!')
