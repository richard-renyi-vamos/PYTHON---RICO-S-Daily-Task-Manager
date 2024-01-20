import tkinter as tk

def toggle_always_on_top():
    root.attributes('-topmost', not root.attributes('-topmost'))

# Create the main window
root = tk.Tk()
root.title("Daily Tasks")

# List to store task entries
tasks = []

# Function to create new task entries
def create_task():
    if len(tasks) < 10:
        task_number = len(tasks) + 1
        frame = tk.Frame(root)
        frame.pack()

        label = tk.Label(frame, text=f"TASK {task_number}: ", width=10)
        label.pack(side=tk.LEFT)

        task_var = tk.StringVar()
        entry = tk.Entry(frame, textvariable=task_var, width=40)
        entry.pack(side=tk.LEFT)
        
        tasks.append(task_var)

# Create 10 tasks initially
for _ in range(10):
    create_task()

# Button to toggle always on top
top_button = tk.Button(root, text="Toggle Always on Top", command=toggle_always_on_top)
top_button.pack()

# Start the GUI event loop
root.mainloop()
