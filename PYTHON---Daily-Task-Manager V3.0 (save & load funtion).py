import tkinter as tk
import os

def toggle_always_on_top():
    root.attributes('-topmost', not root.attributes('-topmost'))

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task.get() + "\n")
    print("Tasks saved!")  # Optional: for confirmation in the console

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                create_task(line.strip())

# Create the main window
root = tk.Tk()
root.title("Daily Tasks")

# List to store task entries
tasks = []

# Function to create new task entries
def create_task(task_text=""):
    if len(tasks) < 10:
        task_number = len(tasks) + 1
        frame = tk.Frame(root)
        frame.pack()

        label = tk.Label(frame, text=f"TASK {task_number}: ", width=10)
        label.pack(side=tk.LEFT)

        task_var = tk.StringVar(value=task_text)
        entry = tk.Entry(frame, textvariable=task_var, width=40)
        entry.pack(side=tk.LEFT)
        
        tasks.append(task_var)

# Load tasks from file on startup
load_tasks()

# Button to toggle always on top
top_button = tk.Button(root, text="Toggle Always on Top", command=toggle_always_on_top)
top_button.pack()

# Button to save tasks
save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack()

# Start the GUI event loop
root.mainloop()
