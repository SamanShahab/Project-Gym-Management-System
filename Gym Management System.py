import tkinter as tk
from tkinter import messagebox, ttk

root = tk.Tk()
root.title("Gym Management System")
root.geometry("800x400")
root.configure(bg="black")

# Initialize trainers data structure
trainers = {
    "John Doe": "Strength Training",
    "Jane Smith": "Cardio Training",
    "Michael Johnson": "Flexibility Training",
    "Emily Davis": "Endurance Training",
    "William Brown": "Personal Training"
}

appointments = {}
duration = 0
users = {}
usernames = []

def center_window():
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def update_trainer_combobox():
    trainer_name_combobox['values'] = list(trainers.keys())
    trainer_info_combobox['values'] = list(set(trainers.values()))

def load_trainer_info(*args):
    selected_trainer = trainer_name_combobox.get()
    if selected_trainer in trainers:
        trainer_info_combobox.set(trainers[selected_trainer])

def add_trainer():
    trainer_name = trainer_name_combobox.get()
    trainer_info = trainer_info_combobox.get()
    if trainer_name and trainer_info:
        with open("trainer_info.txt", "+a") as file:
            file.write(f"{trainer_name}\n{trainer_info}\n")
        trainers[trainer_name] = trainer_info
        update_trainer_combobox()
        messagebox.showinfo("Success", "Trainer added successfully!")
    else:
        messagebox.showerror("Error", "Please provide both name and info for the trainer.")

def update_trainer():
    trainer_name = trainer_name_combobox.get()
    trainer_info = trainer_info_combobox.get()
    if trainer_name in trainers:
        with open("trainer_info.txt", "r") as file:
            data = file.readlines()
            for line in range(len(data)):
                if trainer_name+"\n" == data[line]:
                    data[line+1] = trainer_info
        with open("trainer_info.txt", "w") as file:
            file.writelines(data) 
        trainers[trainer_name] = trainer_info
        update_trainer_combobox()
        messagebox.showinfo("Success", "Trainer updated successfully!")
    else:
        messagebox.showerror("Error", "Trainer not found!")

def delete_trainer():
    trainer_name = trainer_name_combobox.get()
    if trainer_name in trainers:
        with open("trainer_info.txt", "r") as file:
            data = file.readlines()
            for line in range(len(data)):
                if trainer_name+"\n" == data[line]:
                    copied_data = data.copy()
                    del copied_data[line:line+2]
        with open("trainer_info.txt", "w") as file:
            file.writelines(copied_data)
        del trainers[trainer_name]
        update_trainer_combobox()
        messagebox.showinfo("Success", "Trainer deleted successfully!")
    else:
        messagebox.showerror("Error", "Trainer not found!")

def book_appointment():
    appointment_date = appointment_date_entry.get()
    if appointment_date:
        appointments[appointment_date] = []
        messagebox.showinfo("Success", "Appointment booked successfully!")
    else:
        messagebox.showerror("Error", "Please enter an appointment date.")

def update_duration():
    duration = duration_entry.get()
    if duration:
        duration = int(duration)
        messagebox.showinfo("Success", "Duration updated successfully!")
    else:
        messagebox.showerror("Error", "Please select a duration.")

def book():
    global user_name, weight, gym_plan
    user_name = user_name_entry.get()
    weight = weight_entry.get()
    gym_plan = gym_plan_entry.get()
    if user_name and weight and gym_plan:
        gym_plan_costs = {"Basic": 500, "Premium": 1000, "Elite": 3000}
        fee = gym_plan_costs[gym_plan]
        users[user_name] = {"weight": int(weight), "gym_plan": gym_plan}
        user_name_entry['values'] = list(users.keys())
        messagebox.showinfo("Success", f"Booking successful! Your fee is ${fee}.")
    else:
        messagebox.showerror("Error", "Please provide all user details.")


def save_user_info():
    with open("user_info.txt", "+a") as file:
        user_name = user_name_entry.get()
        weight = weight_entry.get()
        gym_plan = gym_plan_entry.get()
        file.write(f"{user_name}\n{weight}\n{gym_plan}\n")
    if user_name not in usernames:
        usernames.append(user_name)
    

def search_user():
    user_name = user_name_entry.get()
    if user_name in users:
        user_info = users[user_name]
        messagebox.showinfo("Success", f"User found: {user_info}")
    else:
        messagebox.showerror("Error", "User not found!")

def show_user_info():
    try:
        with open("user_info.txt", "r") as file:
            user_info = file.read()
            messagebox.showinfo("User Info", user_info)
    except FileNotFoundError:
        messagebox.showerror("Error", "No user information found!")

def show_trainer_info():
    try:
        with open("trainer_info.txt", "r") as file:
            trainer_info = file.read()
            messagebox.showinfo("Trainer Info", trainer_info)
    except FileNotFoundError:
        messagebox.showerror("Error", "No trainer information found!")

# Create a frame to contain all widgets
main_frame = tk.Frame(root, bg="black")
main_frame.pack(expand=True, fill="both")

# Create frames with background color
trainer_frame = tk.Frame(main_frame, bg="skyblue")
trainer_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

appointment_frame = tk.Frame(main_frame, bg="skyblue")
appointment_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

duration_frame = tk.Frame(main_frame, bg="skyblue")
duration_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

booking_frame = tk.Frame(main_frame, bg="skyblue")
booking_frame.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

# Create labels and comboboxes for trainer management
tk.Label(trainer_frame, text="Trainer Name:", bg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
trainer_name_combobox = ttk.Combobox(trainer_frame, values=list(trainers.keys()))
trainer_name_combobox.grid(row=0, column=1, padx=5, pady=5)

tk.Label(trainer_frame, text="Trainer Info:", bg="#ffffff").grid(row=0, column=2, padx=5, pady=5)
trainer_info_combobox = ttk.Combobox(trainer_frame, values=list(set(trainers.values())))
trainer_info_combobox.grid(row=0, column=3, padx=5, pady=5)

tk.Button(trainer_frame, text="Add Trainer", command=add_trainer, bg="black", fg="white").grid(row=0, column=4, padx=5, pady=5)
tk.Button(trainer_frame, text="Update Trainer", command=update_trainer, bg="black", fg="white").grid(row=0, column=5, padx=5, pady=5)
tk.Button(trainer_frame, text="Delete Trainer", command=delete_trainer, bg="black", fg="white").grid(row=0, column=6, padx=5, pady=5)

# Add the date picker label
tk.Label(appointment_frame, text="Date picker:", bg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
appointment_date_entry = tk.Entry(appointment_frame)
appointment_date_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Button(appointment_frame, text="Book Appointment", command=book_appointment, bg="black", fg="white").grid(row=0, column=2, padx=5, pady=5)

tk.Label(duration_frame, text="Duration (hours):", bg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
duration_entry = ttk.Combobox(duration_frame, values=[1, 2, 3, 4, 5, 6])
duration_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Button(duration_frame, text="Update Duration", command=update_duration, bg="black", fg="white").grid(row=0, column=2, padx=5, pady=5)

tk.Label(booking_frame, text="User Name:", bg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
user_name_entry = ttk.Combobox(booking_frame, values=usernames)
user_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(booking_frame, text="Weight:", bg="#ffffff").grid(row=0, column=2, padx=5, pady=5)
weight_entry = ttk.Combobox(booking_frame, values=list(range(1, 101)))
weight_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(booking_frame, text="Gym Plan:", bg="#ffffff").grid(row=0, column=4, padx=5, pady=5)
gym_plan_entry = ttk.Combobox(booking_frame, values=["Basic", "Premium", "Elite"])
gym_plan_entry.grid(row=0, column=5, padx=5, pady=5)

tk.Button(booking_frame, text="Book", command=lambda: [book(), save_user_info()], bg="black", fg="white").grid(row=0, column=6, padx=5, pady=5)
tk.Button(booking_frame, text="Search User", command=search_user, bg="black", fg="white").grid(row=0, column=7, padx=5, pady=5)

# Add button to show user info from file, "user_info.txt"
tk.Button(main_frame, text="Show User Info", command=show_user_info, bg="pink", fg="black").grid(row=4, column=0, sticky="ew", padx=20, pady=10)

# Add button to show trainer info from file, "trainers_info.txt"
tk.Button(main_frame, text="Show Trainer Info", command=show_trainer_info, bg="#FDFD96", fg="black").grid(row=5, column=0, sticky="ew", padx=20, pady=10)

# Add Exit button 
tk.Button(main_frame, text="Exit", command=root.destroy, bg="white", fg="black").grid(row=6, column=0, sticky="ew", padx=20, pady=10)
# Center the main frame within the window
center_window()

# update trainer info when trainer name is selected
trainer_name_combobox.bind("<<ComboboxSelected>>", load_trainer_info)

root.mainloop()
