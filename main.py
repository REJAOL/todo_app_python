while True:
    user_action = input("enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)

        case 'edit':
            number = int(input('number of the todo to edit: '))
            index_number = number-1
            new_todo = input('enter new todo: ')
            todos[index_number] = new_todo

        case 'complete':
            number = int(input('number of the todo to complete: '))
            todos.pop(number-1)

        case 'exit':
            break
print("BYE!!!!")
