The folder builder project was created as part of a documentation control initiative for the Technology & Innovation Department (TID).  A python program was written to create a new project folder that contained standardized sub-folders, used mainly for process engineering projects. A simple GUI was created using Tkinter, as many of the personnel in TID not are acquainted with the command prompt or have Python on their computer. Pyinstaller was used to convert the python program to an executable program that works with the Windows OS.

The python program ensures that there are no leading or legging spaces, no unauthorized special characters in the folder name, that snake case is used for the folder name, and an option for adding a start date to the project folder name.  The program should add the project folder to the parent directory where the program is located.  However, there is an option to add the project folder to any existing path.  

As this is a simplified program, any folders with incorrect naming conventions, creating folders that already exist, or using directory paths that do not exist caused the program to exit with a warning message as to why the folders were not created.

This project is not fully complete at this time.  Standard folders and potentially additionally sub-folders still need to be selected by the PM.  The main GUI may have radial buttons added to it such that standardized folders can be created for specific work groups within TID that perform different function beyond process engineering.  

![Untitled](https://github.com/user-attachments/assets/eb963e2b-9e5c-44e7-ab71-f417bb696de9)
