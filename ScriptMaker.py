#ScriptMaker v0.1   Play This File to Start
#You will need to pip install a few modules for this to work
#{keyboard, customtkinter} from what i know of there may be more

#Modules
import keyboard as key
from tkinter import filedialog
import os
    

#Startup
def Startup():
    import Shared
    Shared.UI.CreateMainWindow() #Create the main window
    Shared.UI.CreateStartMenu() #Create the startup menu

    if not os.path.exists(Shared.EditorSettings["SavedEditorSettings"]["SavePath"]): #Check if the save path exists if it doesn't Ask for it
        Folder = filedialog.askdirectory(title="Select a Folder To Save Your Scripts")
        if os.path.exists(Folder):
            Shared.EditorSettings["SavedEditorSettings"]["SavePath"] = Folder
            Shared.File.SaveEditorSettings()

    key.add_hotkey('ctrl+s',  (Shared.File.SaveScript))

    Shared.CTK.mainloop() #Start the main event loop


if __name__ == "__main__":
    Startup()