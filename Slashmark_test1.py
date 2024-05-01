import tkinter as tk
from tkinter import messagebox
# empty list to store tasks
tasks = []
# display the to-do list
def display_tasks():
    task_list.delete(0, tk.END)
    if not tasks:
        task_list.insert(tk.END, "Your to-do list is empty.")
        
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            task_list.insert(tk.END, f"{i}. {task['task']} ({status})")

# add a task to the to-do list
def add_task():
    task_name = task_entry.get()
    if task_name:
        task = {"task": task_name, "completed": False}
        tasks.append(task)
        display_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# mark a task as completed
def mark_completed():
    selected_task = task_list.curselection()
    if selected_task:
        task_index = selected_task[0]
        tasks[task_index]["completed"] = True
        display_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task.")

# remove a task
def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_index = selected_task[0]
        removed_task = tasks.pop(task_index)
        display_tasks()
    else:
        messagebox.showwarning("Warning", "Please select a task.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=5, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

task_list = tk.Listbox(root, width=50, height=10)
task_list.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

mark_button = tk.Button(root, text="Mark Completed", command=mark_completed)
mark_button.grid(row=2, column=0, padx=5, pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=2, column=1, padx=5, pady=5)
display_tasks()

root.mainloop()
