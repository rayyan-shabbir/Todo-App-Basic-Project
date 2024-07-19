from functions import get_todos, write_todos
import time
# import functions

# If different directory
# from modules import functions  

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is now:", now)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
 
    elif user_action.startswith("edit"):
        try:
            mumber = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue


    elif user_action.startswith("complete"):
        try:
            mumber = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)


            write_todos("todos.txt", todos)


            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue

        
    elif user_action.startswith("exit"):
        break
    
    else:
        print("Command not match.")

print("Bye!")
    