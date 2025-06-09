#Most of the UI code should be kept in this file and imported by other files
#This code should and will be simpfied later there is some junk in here from old code and reworks 

#Theres a issue with the Ui not scaling to different screen sizes i will have to look into that.

import SavLoad as File #Import the file that handles saving and loading

import customtkinter as CK
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

global CTK; CTK = CK.CTk()#i made this a globle variable so i can edit it in other files and function

#main window
def CreateMainWindow():
    print("Creating Main Window")
    CTK.geometry("1280x720") #720p
    CTK.title("ScriptMaker: Start Menu")

    icon_path = os.path.join(os.path.dirname(__file__), "Script.ico")
    if os.path.exists(icon_path):
        CTK.iconbitmap(icon_path)
    else:
        print("⚠️ Icon not found:", icon_path)


def ClearWindow(): #Function to clear the window
    CTK.config(menu=None) #Removes the menu in the top bar

    for widget in CTK.winfo_children(): #Loops through all widgets and destroys them
        widget.destroy()

#--------------------------------------------------------------------------

#Button Functions
def NewScript(): #Function to create a new script
    title = CreateScriptMenu()
    Script = File.CreateScript(title, {})
    file_path = filedialog.asksaveasfile(
        title="Select a Place To Save Your Script",
        filetypes=[("Json Files", "*.json"), ("All Files", "*.*")]
    )
    if file_path:
        File.SaveScript(file_path.name, Script)

def OpenScript(): #Function to open/load a script
    file_path = filedialog.askopenfile(
        title="Select a Script File",
        filetypes=[("Json Files", "*.json"), ("All Files", "*.*")]
    )
    if file_path:
        file_path = file_path.name
        print(file_path)
        Script = File.LoadScript(file_path)
        print(Script)

def DeleteScript(): #Function to delete a script
    file_path = filedialog.askopenfilename(
        title="Select a Script File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        if messagebox.askyesno("Delete", "Are you sure you want to delete this file?"): 
            os.remove(file_path)
            messagebox.showwarning("Deleted", "File deleted successfully.")

def NewScene(Scene):
    print(Scene)


def NewShot(Scene, Name, Tag):
    print(Scene, Name, Tag)


#--------------------------------------------------------------------------

#Menu Functions
def CreateScriptMenu():
    dialog = CK.CTkInputDialog(text="Enter Your Script Name:", title="Name Your Script")
    dialog = dialog.get_input()
    print(dialog)
    if dialog != None:
        if dialog == "":
            dialog = "untited Script"

        ClearWindow()

        CTK.title("ScriptMaker: " + dialog)
        # Create a native-style menu bar
        menubar = tk.Menu(CTK)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=NewScript)
        file_menu.add_command(label="Open...", command=OpenScript)
        file_menu.add_command(label="Save", command=File.SaveScript)
        file_menu.add_separator()
        file_menu.add_command(label="Back to Start Menu", command=CreateStartMenu)
        file_menu.add_command(label="Exit", command=CTK.quit)

        # Add File menu to the menubar
        menubar.add_cascade(label="File", menu=file_menu)

        # Set the menubar on the window
        CTK.config(menu=menubar)

        CK.CTkFrame(master=CTK, width=1280, height=720, fg_color="#212121").place(x=0, y=0)
        CK.CTkFrame(master=CTK, width=350, height=550, fg_color="#3A3A3A").place(x=25, y=150)
        CK.CTkFrame(master=CTK, width=350, height=550, fg_color="#3A3A3A").place(x=400, y=150)

        CK.CTkButton(master=CTK, text="+", font=("Arial", 30), width=50, height=50, command=NewScene).place(x=25, y=100)
        return dialog
    
def CreateStartMenu():
    ClearWindow()

    CTK.title("ScriptMaker: Start Menu")

    CK.CTkFrame(master=CTK, width=1280, height=720, fg_color="#212121").place(x=0, y=0)
    CK.CTkFrame(master=CTK, width=750, height=650, fg_color="#494949").place(x=25, y=50)

    CK.CTkButton(master=CTK, text="New Script", font=("Arial", 40), command=NewScript).place(x=850, y=100)
    CK.CTkButton(master=CTK, text="Open Script", font=("Arial", 40), command=OpenScript).place(x=850, y=250)
    CK.CTkButton(master=CTK, text="Delete Script", font=("Arial", 40), command=DeleteScript).place(x=850, y=400)

#--------------------------------------------------------------------------



