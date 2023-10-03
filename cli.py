user_prompt = "Type add, show, edit, complete or exit:  "
from functions import file_write,file_read
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    if 'add' in user_action:
        todo1 = user_action[4:] + "\n"
        todo=file_read('todo.txt')
        todo.append(todo1)
        file_write(todo, 'todo.txt')
    elif 'show' in user_action:
        todo=file_read('todo.txt')
        for index, item in enumerate(todo):
            item=item.strip('\n')
            print(f"{index + 1}-{item}")
    elif 'edit' in user_action:
        number = int(user_action[5:])

        todo=file_read('todo.txt')
        new_todo = input("Enter the new value")
        todo[number - 1] = new_todo + '\n'

        file_write(todo, 'todo.txt')

    elif 'complete' in user_action:
        number = int(user_action[8:])
        todo=file_read('todo.txt')
        todo_to_remove = todo[number - 1]
        print(todo_to_remove)
        todo.pop(number - 1)

        file_write(todo, 'todo.txt')

    elif 'exit' in user_action:
        break
    else:
        print("Wrong command")

print('bye')
