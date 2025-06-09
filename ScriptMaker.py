#ScriptMaker v0.1

#Modules
import keyboard as key

#Scripts
import UI
import SavLoad as File

#Startup
UI.CreateMainWindow()
print("ScriptMaker v0.1")
UI.CreateStartMenu()

#SaveEditor
key.add_hotkey('ctrl+s',  (lambda: print("Saving...")))


UI.CTK.mainloop() #Start the main event loop