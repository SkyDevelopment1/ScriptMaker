import os
from tkinter import filedialog
import json
import time

import Shared

#for the project file structure i would like it to be something like
#ProjectName: {SceneName: {ShotName: {Tag: "", Story: ""}}} In tag if its Talking or Yelling or something like that and in story if its a character saying something or something like that then required a character

EditorSettingsPath = os.path.abspath("EditorSettings.json")


def CreateScript():
    Title = Shared.UI.CK.CTkInputDialog(text="Enter Your Script Name:", title="Name Your Script").get_input()

    if Title == None or Title == "":
        Title = "Untitled Script"

    Script = {
        "Title": Title,
        "Scenes": "",
        "Characters": "",
    }
    
    Shared.CurrentScript = Script
    return Script

#at the momment i'm trying to load exsamples then Start coding the saving following the same structure as the loading

def SaveScript():
    Script = Shared.CurrentScript

    if os.path.exists(EditorSettingsPath) and os.path.exists(Shared.EditorSettings["SavedEditorSettings"]["SavePath"]):
        with open(os.path.join(Shared.EditorSettings["SavedEditorSettings"]["SavePath"], Script["Title"] + ".json"), "w", encoding="utf-8") as file:
            Script = json.dump(Script, file, indent=4)
            Shared.ProjectFile = Script
            Shared.UI.CreateScriptMenu()

    elif not os.path.exists(EditorSettingsPath): #if the first if statement fails then check whats wrong
        pass
    elif not os.path.exists(Shared.EditorSettings["SavedEditorSettings"]["SavePath"]): #if it issue is not the editor settings then check the save path
        pass 
    else: #something is wrong
        Warning("Error Saving Script")

def LoadScript(JsonPath: str): #Need to code a order system it can get out of order of events if i dont code it
    
    if os.path.exists(EditorSettingsPath) and os.path.exists(Shared.EditorSettings["SavedEditorSettings"]["SavePath"]):#success
        with open(JsonPath, "r", encoding="utf-8") as file:

            Script = json.load(file)
            Shared.CurrentScript = Script
            Shared.UI.ChangeWindowTitle("Script Maker " + Script["Title"])
            return Script
        
    elif not os.path.exists(EditorSettingsPath): #if the first if statement fails then check whats wrong
        pass
    elif not os.path.exists(Shared.EditorSettings["SavedEditorSettings"]["SavePath"]): #if it issue is not the editor settings then check the save path
        pass 
    else: #something is wrong
        Warning("Error Saving Script")

def NewScene():
    SceneName = Shared.UI.CK.CTkInputDialog(text="Enter Your Scene Name:", title="Name Your Scene").get_input()
    Shared.CurrentScript["Scenes"][SceneName] = {}
    print(SceneName)


def NewShot(Scene):
    Name = Shared.UI.CK.CTkInputDialog(text="Enter Your Shot Name:", title="Name Your Shot").get_input()
    Tag = Shared.UI.CK.CTkInputDialog(text="Enter Your Shot Tag:", title="Name Your Shot").get_input()

    if Tag == None:
        Tag = ""
    if Tag == "Talking" or Tag == "Yelling":
        Character = Shared.UI.CK.CTkInputDialog(text="Enter Your Character Name:", title="Name Your Character").get_input()
        Shared.CurrentScript["Characters"].append(Character)
        Tag = "Talking: " + Character

    Shared.CurrentScript["Scenes"][Scene][Name] = {"Tag": Tag, "Story": ""}
    print(Scene, Name, Tag)

def SaveEditorSettings():
    if os.path.exists(EditorSettingsPath):
        with open(EditorSettingsPath, "w", encoding="utf-8") as file:
            json.dump(Shared.EditorSettings, file, indent=4)
            print("EditorSettings.json saved successfully")
    else:
        print("EditorSettings.json not found Path: ", EditorSettingsPath)

def LoadEditorSettings():
    
    if os.path.exists(EditorSettingsPath):
        with open(EditorSettingsPath, "r", encoding="utf-8") as file:
            LoadedEditorSettings = json.load(file)
            Shared.EditorSettings = LoadedEditorSettings.copy()
            return LoadedEditorSettings
    else:
        print("EditorSettings.json not found Path: ", EditorSettingsPath)


def ExportScript(): #Exporting should be converting the script data into a text file formated as a movie Script (Scene: SceneName - Shot: ShotName ~ Tag) then the story/Text should be under that
    with open("Example.json", "r", encoding="utf-8") as file:
        LoadedScript = json.load(file)

    if LoadedScript:
        TextScript = LoadedScript["Title"] + "\n\n\n"

        for Scene in LoadedScript["Scenes"]:
            for Shot in LoadedScript["Scenes"][Scene]:
                TextScript += "(Scene: " + Scene + " - Shot: " + Shot

                if LoadedScript["Scenes"][Scene][Shot]["Tag"] != "":#if there no tag for the shot then skip this
                    TextScript += " ~ Tag: " + LoadedScript["Scenes"][Scene][Shot]["Tag"]
                    if LoadedScript["Scenes"][Scene][Shot]["Tag"] == "Talking" or LoadedScript["Scenes"][Scene][Shot]["Tag"] == "Yelling":
                        TextScript += " * " + LoadedScript["Scenes"][Scene][Shot]["Character"]
                 
                TextScript += ")"
                TextScript += "\n" + LoadedScript["Scenes"][Scene][Shot]["Story"] + "\n\n"

                print(TextScript)

            if os.path.exists(Shared.EditorSettings["SavedEditorSettings"]["SavePath"]):
                with open(os.path.join(Shared.EditorSettings["SavedEditorSettings"]["SavePath"], LoadedScript["Title"] + ".txt"), "w", encoding="utf-8") as file:
                    file.write(TextScript)

        return TextScript
    else:
        print("Failed to export script!!!")

Shared.EditorSettings = LoadEditorSettings() 

