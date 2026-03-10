#Name: Dulanmi Sasandula
#Date: 15/04/2025

##Software Development [Programming] coursework (Stage 3 & Stage 4)
#Tkinter GUI for Viewing, Searching and Sorting tasks

#STAGE 04

import json
import tkinter as tk
from tkinter import ttk

# Task class
class Task:
    def __init__(self, Name, Description, Priority, Due_Date):
        self.Name = Name
        self.Description = Description
        self.Priority = Priority
        self.Due_Date = Due_Date

    def to_dict(self):
        return {
            "Name": self.Name,
            "Description": self.Description,
            "Priority": self.Priority,
            "Due Date": self.Due_Date
        }

# Task manager class
class TaskManager:
    def __init__(self, json_file='tasks.json'):
        self.json_file = json_file
        self.tasks = []
        self.load_tasks_from_json()

    def load_tasks_from_json(self):
        try:
            with open(self.json_file, "r") as file:
                data = json.load(file)
                self.tasks = [
                    Task(
                    Name=task.get("Name", ""),
                    Description=task.get("Description", ""),
                    Priority=task.get("Priority", ""),
                    Due_Date=task.get("Due Date", "")  
                )
                for task in data
            ]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []
            
    def save(self):
        with open(self.json_file, 'w') as file:
            json.dump([t.to_dict() for t in self.tasks], file, indent=4)

    def get_filtered_tasks(self, Name_filter='', Priority_filter='', Due_date_filter=''):
        return [t for t in self.tasks if
                Name_filter.lower() in t.Name.lower() and
                Priority_filter.lower() in t.Priority.lower() and
                Due_date_filter.lower() in t.Due_Date.lower()]

    def sort_tasks(self, sort_key='Name'):
        self.tasks.sort(key=lambda t: getattr(t, sort_key).lower()if getattr(t, sort_key) else "")

# GUI class
class TaskGUI:
    def __init__(self, root):
        self.manager = TaskManager()
        self.root = root
        self.root.title("Task Manager")
        self.setup_gui()

    def setup_gui(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.e1, self.e2, self.e3 = [tk.Entry(frame) for _ in range(3)]
        for i, (label, entry) in enumerate(zip(["Name", "Priority", "Due Date"], [self.e1, self.e2, self.e3])):
            tk.Label(frame, text=label).grid(row=0, column=i*2)
            entry.grid(row=0, column=i*2+1)

        tk.Button(frame, text="Filter", command=self.apply_filter).grid(row=0, column=6, padx=10)

        self.tree = ttk.Treeview(self.root, columns=["name", "description", "priority", "Due Date"], show="headings")
        for col in ["name", "description", "priority", "Due Date"]:
            self.tree.heading(col, text=col.capitalize(), command=lambda c=col: self.sort(c))
            self.tree.column(col, width=150, stretch=True, anchor="center")

        self.tree.pack(fill="both", expand=True)
        self.refresh(self.manager.tasks)

    def refresh(self, tasks):
        self.tree.delete(*self.tree.get_children())
        for t in tasks:
            self.tree.insert('', 'end', values=(t.Name, t.Description, t.Priority, t.Due_Date))

    def apply_filter(self):
        tasks = self.manager.get_filtered_tasks(self.e1.get(), self.e2.get(), self.e3.get())
        self.refresh(tasks)

    def sort(self, sort_key):
        self.manager.sort_tasks(sort_key)
        self.refresh(self.manager.tasks)

# Run the app
if __name__ == '__main__':
    root = tk.Tk()
    app = TaskGUI(root)
    root.mainloop()
