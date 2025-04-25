# import libraries
import os
import datetime
import tkinter as tk
from tkinter import ttk

# GUI Code

# Functions
def func_error_message(err):
    """This function creates a GUI for an error message"""
    window_error = tk.Tk()
    window_error.title("Error Message")
    window_error.geometry("300x100+50+50")
    window_error.minsize(300,50)
    error_message = ttk.Label(window_error, text="Folder not created.")
    error_message2= ttk.Label(window_error, text= err)
    error_message.pack()
    error_message2.pack()

def func_build_project_folder(dir: str, folder_name: str):
    """This function will contain the folder names that need to be created for a standard Metro TID project.  It is being added as a function as TID has process engineering, analytics, and instrumentation groups.  We may want to have individual project folder build-out for each group."""

    # Create the parent directory and subfolders
    parent = dir + "/" + folder_name

    subfolders = ("00_PM", "10_Data", "20_Engineering", "30_Drawings", "40_Invoices", '50_Change_orders', "60_Emails", "70_Photos")

    #check if parent exists
    if os.path.exists(parent):
        window.destroy()
        err_message = "Parent already exists"
        func_error_message(err_message)
    else:
        #create the folders
        print(parent)
        os.mkdir(parent)

        for sub in subfolders:
            subs = parent + "/" + sub
            os.mkdir(subs)

def func_delete():
    """Create a function to delete entry widgets and its associated values that can be passed to the rest of the python program"""
    global path_dir, project_folder, add_date, parent_dir_bool

    # delete values in entry bars
    path_entry.delete(0, tk.END)
    folder_name_entry.delete(0,tk.END)
    add_date_var.set(0)
    parent_dir_var.set(0)

    # delete values in variables
    path_dir = str(path_entry.get())
    project_folder = str(folder_name_entry.get())
    add_date = int(add_date_var.get())
    parent_dir_bool = int(parent_dir_var.get())

def func_parent_dir():
    """When the parent directory box is checked, it adds the parent directory path into the file path entry box. Opposite is true when unchecked."""
    if int(parent_dir_var.get()) == 1:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, os.getcwd())
    else:
        path_entry.delete(0, tk.END)

def func_submit():
    """This is the main function and executes when the submit button is pressed.  It checks the integrity of directory location to ensure it exists and add a set of project folders to the desired directory location"""
    global path_dir, project_folder, add_date

    path_dir = str(path_entry.get())
    project_folder = str(folder_name_entry.get())
    add_date = int(add_date_var.get())

    #clean folder names
    project_folder = project_folder.strip() #remove spaces
    project_folder = project_folder.replace(" ", "_") #snake casing of name

    #adds todays date to the end of the folder name
    if add_date == 1:
        today_str = datetime.date.today()
        today_str = "_"+str(today_str.strftime("%Y%m%d"))
        project_folder = project_folder + today_str

    #check for invalid characters that cannot be in a folder name
    invalid_chars_folders = ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]

    if any(c in project_folder for c in invalid_chars_folders):
        window.destroy()
        err_message = "Folder name cannot have special characters."
        func_error_message(err_message)

    #ensure folder name is added
    if len(project_folder) < 1:
        window.destroy()
        err_message = "Folder name is required."
        func_error_message(err_message)

    #allows for path to be copied from File Explorer without causing Python errors due to using single backslash
    path_dir = path_dir.replace('\\', '/')

    #check if directory path exists
    if not os.path.exists(path_dir):
        window.destroy()
        err_message = "Path does not exist"
        func_error_message(err_message)

    #build the project folders in the directory path
    func_build_project_folder(dir=path_dir, folder_name=project_folder)

    window.destroy()

#Tkinter for GUI creation
# Windows
window = tk.Tk()
window.title("Folder Builder")
window.geometry("900x350+50+50")
window.minsize(900,350)

# Frames in GUI
frame = ttk.Frame(window, borderwidth=2)
frame2 = ttk.Frame(window, borderwidth=2)
frame.pack()
frame2.pack()

folder_frame = ttk.LabelFrame(frame, text="Folder Naming Options")
file_frame = ttk.LabelFrame(frame2, text="File Location Option")

folder_frame.grid(row=0, column=0, padx=10, pady=10)
file_frame.grid(row=1, column=0,padx=10, pady=10)

# Widgets in Frames
folder_name_label = ttk.Label(folder_frame,
                              text="New project folder name",
                              anchor="w", justify='left')

folder_name_entry = ttk.Entry(folder_frame,
                             width = 100)

add_date_var = tk.IntVar()
add_date_check_button = ttk.Checkbutton(folder_frame,
                         text = "Add a date to end of project folder name",
                         onvalue=1, offvalue=0,
                         variable=add_date_var)

path_label = ttk.Label(file_frame,
                           text = "Directory Path for new project folders",
                           anchor="w", justify="left",
                           )

path_entry = ttk.Entry(file_frame,
                           width=100 )

parent_dir_var = tk.IntVar()
parent_dir_check_button = ttk.Checkbutton(file_frame,
                         text = "Check to use the parent directory for new folder location.",
                         onvalue=1, offvalue=0,
                         command=func_parent_dir,
                         variable=parent_dir_var)

cwd_label = ttk.Label(file_frame,anchor="w", justify="left")
cwd_label.config(text=f"Current Directory: {os.getcwd()}", wraplength=1500)

enter_button = ttk.Button(window, text="Submit", command=func_submit)

delete_button = ttk.Button(window, text="Delete", command=func_delete)

# widget geometry - grid / pack
folder_name_label.grid(row=0, column=0, sticky="w")
folder_name_entry.grid(row=0, column=1, pady=10, sticky="e")
add_date_check_button.grid(row=1, column=0, sticky="w", columnspan=2)
path_label.grid(row=0, column=0, sticky="w")
path_entry.grid(row=0, column=1, pady=10, sticky="e")
parent_dir_check_button.grid(row=1, column=0, sticky="w", columnspan=2 )
cwd_label.grid(row=2, column=0, sticky="w", columnspan=2, rowspan=3)
enter_button.pack()
delete_button.pack()

window.mainloop()
