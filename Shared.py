#there was issues with all the imports in all the files so i moved them all here aswell as global variables
import UI
import SavLoad as File
import ScriptMaker

def GlobalVariables():
    global EditorSettings; EditorSettings = None
    global CurrentScript; CurrentScript = None

    global CTK; CTK = None#i made this a globle variable so i can edit it in other files and function

GlobalVariables()