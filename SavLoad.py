import ScriptMaker
import UI #UI.py

import os
from tkinter import filedialog
import json

#for the project file structure i would like it to be something like
#ProjectName: {SceneName: {ShotName: {Tag: "", Story: ""}}} In tag if its Talking or Yelling or something like that and in story if its a character saying something or something like that then required a character

EditorSettingsPath = os.path.abspath("EditorSettings.json")

def CreateScript():
    Title = UI.CK.CTkInputDialog(text="Enter Your Script Name:", title="Name Your Script").get_input()

    Script = {
        "Title": Title,
        "Scenes": "",
        "Characters": "",
    }
    
    return Script

#at the momment i'm trying to load exsamples then Start coding the saving following the same structure as the loading

def SaveScript():
    Script = ScriptMaker.CurrentScript
    if os.path.exists(EditorSettingsPath) and os.path.exists(ScriptMaker.EditorSettings["SavedEditorSettings"]["SavePath"]):
        pass
    elif not os.path.exists(EditorSettingsPath): #if the first if statement fails then check whats wrong
        pass
    elif not os.path.exists(ScriptMaker.EditorSettings["SavedEditorSettings"]["SavePath"]): #if it issue is not the editor settings then check the save path
        pass 
    else: #something is wrong
        Warning("Error Saving Script")

def LoadScript():
    pass

def SaveEditorSettings():
    if os.path.exists(EditorSettingsPath):
        with open(EditorSettingsPath, "w", encoding="utf-8") as file:
            json.dump(ScriptMaker.EditorSettings, file, indent=4)
            print("EditorSettings.json saved successfully")
    else:
        print("EditorSettings.json not found Path: ", EditorSettingsPath)

def LoadEditorSettings():
    if os.path.exists(EditorSettingsPath):
        with open(EditorSettingsPath, "r", encoding="utf-8") as file:
            LoadedEditorSettings = json.load(file)
            return LoadedEditorSettings
    else:
        print("EditorSettings.json not found Path: ", EditorSettingsPath)


def ExportScript(ScriptData): #Exporting should be converting the script data into a text file formated as a movie Script (Scene: SceneName - Shot: ShotName ~ Tag) then the story/Text should be under that
    LoadedScript = LoadScript(ScriptData)
    print(LoadedScript)
