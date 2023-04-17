import os
import sys
import json
import subprocess

class command():
    def __init__(self, syntax, description):
        self.syntax = syntax
        self.description = description

safemode = False

print("Magma Shell [Version 1.0.0/00001]")
print("Copyright © 2023 Magma Shell | All rights reserved")

with open("settings.json", "r") as f:
    langpack = json.load(f)["settings"]["langpack"]

os.system("title Magma Shell")
cmd = ""
path = os.getcwd()

langfile = open(f"packages/langpacks/{langpack}/lang.json",'r', encoding="utf-8")
langfile = json.load(langfile)

logs = open(f"log.magmashelllogs",'w', encoding="utf-8")
cmd = "ipconfig"
result = subprocess.run([cmd], shell=True, capture_output=True, text=True)
logs.writelines(str(result.stdout))
logs.close()

#Load Packages
print(os.walk("packages/cmdpacks"))

while True:
    cmd = input(f"{path}>")
    if cmd == "exit":
        sys.exit()
    elif cmd.split()[0] == "langpack":
            try:
                if os.path.isdir(f"packages/langpacks/{cmd.split()[1]}"):
                    langpack = cmd.split()[1]
                else:
                    print(langfile["lang"]["invalidLang"])
            except:
                print(langfile["lang"]["invalidLang"])
    else:
        with open(f"packages/langpacks/{langpack}/lang.json",'r', encoding="utf-8") as f:
            print(json.load(f)["lang"]["invalid"])
