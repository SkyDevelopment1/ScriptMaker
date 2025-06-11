#ScriptMaker v0.1   Play This File to Start
#You will need to pip install a few modules for this to work
#{keyboard, customtkinter} from what i know of there may be more

#Modules
import keyboard as key
import customtkinter as CK
from tkinter import filedialog
import os

import Shared
    

#Startup
def Startup():#Startup function
    App = Shared.UI.CreateMainWindow() #Create the main window
    Shared.UI.CreateStartMenu() #Create the startup menu

    if not os.path.exists(Shared.File.LoadEditorSettings()["SavedEditorSettings"]["SavePath"]): #Check if the save path exists if it doesn't Ask for it
        Folder = filedialog.askdirectory(title="Select a Folder To Save Your Scripts")
        if os.path.exists(Folder):
            print("Line 21: ", Shared.EditorSettings)
            Shared.EditorSettings["SavedEditorSettings"]["SavePath"] = str(Folder)
            Shared.File.SaveEditorSettings()
    

    key.add_hotkey('ctrl+s',  (Shared.File.SaveScript)) #Hotkey to save the script 

    App.mainloop()

    


if __name__ == "__main__":
    Startup()