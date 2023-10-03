def file_read(file_name= 'todo.txt'):
    file = open(file_name, 'r')
    todo3 = file.readlines()
    file.close()
    return todo3

def file_write(x, file_name='todo.txt'):
    file = open(file_name, 'w')
    file.writelines(x)
    file.close()
