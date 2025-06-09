import UI
import json

def CreateScript(Title:str, SceneTree:dict, Characters:dict):
    Script = {
        "Title": Title,
        "Scenes": SceneTree,
        "Characters": Characters,
    }
    
    return Script

def SaveScript(ScriptPath, ScriptData):
    pass

def LoadScript(ScriptPath):
    pass

def SaveEditor():
    pass

def ExportScript(ScriptData):
    LoadedScript = LoadScript(ScriptData)
    print(LoadedScript)
