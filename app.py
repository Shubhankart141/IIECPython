import os
import pyttsx3

print("Welcome to menu driven program")
pyttsx3.speak("Welcome to menu driven program")
while True:
  print("chat with me with your requirements : "  , end='')
  p = input() 
	
  if (("run" in p) or ("excute" in p ) or ("open" in p ) or ("launch" in p ) or ("do not" not in p ) or ("never" not in p) or ("don't" not in p)) and (("chrome" in p) or ("google" in p)):
    pyttsx3.speak("Your choice is chrome")   
    os.system("chrome")

  elif (("run" in p) or ("excute" in p ) or ("open" in p ) or ("launch" in p ) or ("do not" not in p ) or ("never" not in p) or ("don't" not in p)) and  (("notepad" in p) or ("editor" in p)) : 
    pyttsx3.speak("Your choice is notepad")    
    os.system("notepad")

  elif (("run" in p) or ("excute" in p ) or ("open" in p ) or ("launch" in p ) or ("do not" not in p ) or ("never" not in p) or ("don't" not in p)) and (("player" in p) or ("media" in p)):
    pyttsx3.speak("Your choice is media player")    
    os.system("wmplayer")

  elif (("run" in p) or ("excute" in p ) or ("open" in p ) or ("launch" in p ) or ("do not" not in p ) or ("never" not in p) or ("don't" not in p)) and ("zoom" in p):
    pyttsx3.speak("Your choice is zoom app")    
    os.system("zoom")

  elif (("run" in p) or ("excute" in p ) or ("open" in p ) or ("launch" in p ) or ("do not" not in p ) or ("never" not in p) or ("don't" not in p)) and (("panel" in p) or ("control" in p)):
    pyttsx3.speak("Your choice is control panel")    
    os.system("control panel")
	  
  elif (("run" in p) or ("excute" in p ) or ("open" in p ) or ("launch" in p ) or ("do not" not in p ) or ("never" not in p) or ("don't" not in p)) and (("virtual box" in p) or ("vm" in p)):
    pyttsx3.speak("Your choice is oracal vm virtual box")    
    os.system("VirtualBox")

  elif (("run" in p) or ("excute" in p ) or ("open" in p ) or ("launch" in p ) or ("do not" not in p ) or ("never" not in p) or ("don't" not in p)) and ("paint" in p):
    pyttsx3.speak("Your choice is mspaint")    
    os.system("mspaint")

  elif (("run" in p) or ("excute" in p ) or ("open" in p ) or ("launch" in p ) or ("do not" not in p ) or ("never" not in p) or ("don't" not in p)) and (("shareit" in p) or ("share" in p)):
    pyttsx3.speak("Your choice is shareit")    
    os.system("shareit")

  elif (("run" in p) or ("excute" in p ) or ("open" in p ) or ("launch" in p ) or ("do not" not in p ) or ("never" not in p) or ("don't" not in p)) and (("python" in p) or ("code editer" in p)):
    pyttsx3.speak("Your choice is python code editer")    
    os.system("python")

  elif (("run" in p) or ("excute" in p ) or ("open" in p ) or ("launch" in p ) or ("do not" not in p ) or ("never" not in p) or ("don't" not in p)) and (("codeblocks" in p) or ("c code editer" in p)):
    pyttsx3.speak("Your choice is codeblocks ")    
    os.system("codeblocks")

  elif (("run" in p) or ("excute" in p ) or ("open" in p ) or ("launch" in p ) or ("do not" not in p ) or ("never" not in p) or ("don't" not in p)) and ("teamviewer" in p):
    pyttsx3.speak("Your choice is teamviewer")    
    os.system("teamviewer")

  elif  ("exit" in p) or ("quit" in p):
    pyttsx3.speak("Thank you sir")
    break

  else:
    print("sry sir I am unable to give this service.....  We will update in upcoming version .... If you want to exit then please type exit or quit")
    pyttsx3.speak("sry sir I am unable to give this service.....  We will update in upcoming version .... If you want to exit then please type exit or quit")  
