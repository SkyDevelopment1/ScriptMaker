import UI #UI.py

import os
from tkinter import filedialog
import json

#for the project file structure i would like it to be something like
#ProjectName: {SceneName: {ShotName: {Tag: "", Story: ""}}} In tag if its Talking or Yelling or something like that and in story if its a character saying something or something like that then required a character

EditorSettings = os.path.abspath("EditorSettings.json")

def CreateScript(Title:str, SceneTree:dict, Characters:dict):
    Script = {
        "Title": Title,
        "Scenes": SceneTree,
        "Characters": Characters,
    }
    
    return Script

#at the momment i'm trying to load exsamples then Start coding the saving following the same structure as the loading

def SaveScript():
    pass

def LoadScript():
    pass

def SaveEditorSettings():
    pass

def LoadEditorSettings():
    if os.path.exists(EditorSettings):
        with open(EditorSettings, "r", encoding="utf-8") as file:
            LoadedEditorSettings = json.load(file)
            print("Success: " + LoadedEditorSettings)
            return LoadedEditorSettings
    else:
        print("EditorSettings.json not found Path: ", EditorSettings)


def ExportScript(ScriptData): #Exporting should be converting the script data into a text file formated as a movie Script (Scene: SceneName - Shot: ShotName ~ Tag) then the story/Text should be under that
    LoadedScript = LoadScript(ScriptData)
    print(LoadedScript)
