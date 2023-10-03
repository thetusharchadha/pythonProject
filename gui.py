
import functions
import PySimpleGUI as sg
import os

if not os.path.exists('todo.txt'):
    with open('todo.txt', 'w') as file:
        pass

label= sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button('Add')
list_box=sg.Listbox(values=functions.file_read(),key='todos',
                    enable_events=True, size=[45,10])
edit_button = sg.Button('Edit')
complete_buttom = sg.Button('Complete')
exit_button= sg.Button('Exit')
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button],
                           [list_box,edit_button,
                           complete_buttom],
                           [exit_button]],
                   font=('helvetica', 16))
while True:
    event, values= window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos= functions.file_read('todo.txt')
            new_todo=values['todo']+'\n'
            todos.append(new_todo)
            functions.file_write(todos,'todo.txt')
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit= values['todos'][0]
                new_todo=values['todo']
                todo=functions.file_read('todo.txt')
                index= todo.index(todo_to_edit)
                todo[index]=new_todo +'\n'
                functions.file_write(todo,'todo.txt')
                window['todos'].update(values=todo)
            except IndexError:
                sg.popup('Please select an item first', font=('Helvetica', 20))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todo=functions.file_read('todo.txt')
                todo.remove(todo_to_complete)
                functions.file_write(todo,'todo.txt')
                window['todos'].update(values=todo)
            except IndexError:
                sg.popup('Please select an item first', font=('Helvetica', 20))
        case 'Exit':
            exit()
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()
