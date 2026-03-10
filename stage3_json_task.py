#Name: Dulanmi Sasandula
#Date: 13/04/2025

#Software Development [Programming] coursework (Stage 3 & Stage 4)
#Using Dictionaries and JSON File Handling

#STAGE 03

import json

#List to store tasks

tasks =[]
file_name = "tasks.json"

#Validate priority input
def get_priority():
    while True:
        priority = input("Enter priority (High, Medium, Low): ").capitalize()
        if priority in ["High", "Medium", "Low"]:
            return priority
        print("Invalid priority!")

#Validate date input
def get_date():
    while True:
        date = input("Enter due date (YYYY-MM-DD): ")
        if len(date) == 10 and date[4] == "-" and date[7] == "-" :
            return date
        print("Invalid date format!")


#Load tasks from file
def load_tasks_from_json():
    global tasks
    try:
        with open(file_name, "r") as file:
            tasks = json.load(file)
            print("Tasks loaded successfully!")
    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        tasks = []
  
#Save tasks to file
def save_tasks_to_json():
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)
       

#CRUD operations for the functions
        
#Create task
def create_tasks():
    task = {
        "Name": input("Enter task name: "),
        "Description": input("Enter description: "),
        "Priority": get_priority(),
        "Due Date": get_date()
    }
    tasks.append(task)
    save_tasks_to_json()
    print("Task added successfully!")

# Read task
def read_tasks():
    if not tasks:
        print("No tasks available.")
        return
    
    for i, task in enumerate(tasks, 1):  # Added starting index (1) in enumerate
        print(f"Name: {task['Name']}")
        print(f"Description: {task['Description']}")
        print(f"Priority: {task['Priority']}")
        print(f"Due Date: {task['Due Date']}")


#Update task
def update_tasks():
    read_tasks()
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["Name"] = input("New name (leave empty to keep current name): ") or tasks[index]["Name"]
            tasks[index]["Description"] = input("New description: ") or tasks[index]["Description"]
            tasks[index]["Priority"] = get_priority()
            tasks[index]["Due Date"] = get_date()
            print("Task updated!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

save_tasks_to_json()
print("Task updated successfully!")


#Delete task
def delete_tasks():
    read_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Deleted task: {tasks.pop(index)['Name']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
save_tasks_to_json()


#Main menu
def main():
    load_tasks_from_json()
    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        if choice == "1":
            create_tasks()
        elif choice == "2":
            read_tasks()
        elif choice == "3":
            update_tasks()
        elif choice == "4":
            delete_tasks()
        elif choice == "5":
            print("Thank you for using!")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()
        
       
        



