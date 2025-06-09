#ScriptMaker v0.1   Play This File to Start
#You will need to pip install a few modules for this to work
#{keyboard, customtkinter} from what i know of there may be more

#Modules
import keyboard as key
from tkinter import filedialog
import os

#Scripts
import UI
import SavLoad as File

#Global Variables
global EditorSettings; EditorSettings = File.LoadEditorSettings()
global CurrentScript; CurrentScript = None

if not os.path.exists(EditorSettings["SavedEditorSettings"]["SavePath"]): #Check if the save path exists if it doesn't Ask for it
    Folder = filedialog.askdirectory(title="Select a Folder To Save Your Scripts")
    if os.path.exists(Folder):
        EditorSettings["SavedEditorSettings"]["SavePath"] = Folder
        File.SaveEditorSettings()
    

#Startup
UI.CreateMainWindow() #Create the main window
UI.CreateStartMenu() #Create the startup menu


#SaveScript
key.add_hotkey('ctrl+s',  (File.SaveScript))


UI.CTK.mainloop() #Start the main event loop