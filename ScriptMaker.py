#ScriptMaker v0.1   Play This File to Start
#You will need to pip install a few modules for this to work
#{keyboard, customtkinter} from what i know of there may be more

#Modules
import keyboard as key

#Scripts
import UI
import SavLoad as File

#Startup
UI.CreateMainWindow() #Create the main window
UI.CreateStartMenu() #Create the startup menu

#SaveScript
key.add_hotkey('ctrl+s',  (File.SaveScript))


UI.CTK.mainloop() #Start the main event loop