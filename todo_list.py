import json

user = input("Load or save your todo_list: "type "").strip().lower()

if user == "save":
    todolist = []

    new_task = input("Enter a task to add: ")

    todolist.append(new_task)
    
    with open("todo_data.json", "w") as file:
        json.dump(todolist, file)
        
    print("todo_list saved with your new task!") 
    
elif user == "load":
    try:
        with open("todo_data.json", "r") as file:
            todolist = json.load(file)
        print("todo_list loaded:", todolist)
    except FileNotFoundError:
        print("No saved file found yet. Save something first!")

else:
    print("Invalid choice type load/save.")

input("\nPress Enter to exit...")