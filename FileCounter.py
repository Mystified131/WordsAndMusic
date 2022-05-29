#This code imports the necessary modules.

import os
import datetime

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))
  

#srchstr = 'G:\\OriginalAudio\\Sounds\\Acid_Loops'

srchstr = 'E:\\Acid_Loops'

print("")

print("Scanning and counting files. This might take 5-10 minutes.")

print("")

content =[]
contentogg = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav"): 
    
            content.append(str(filepath))

        if  filepath.endswith(".ogg"): 
    
            contentogg.append(str(filepath))
       

totr = len(content)

totro = len(contentogg)

totot = totr + totro

print("")

print("Total wav files in this directory are: ", totr)

print("")

print("")

print("Total ogg files in this directory are: ", totro)

print("")

print("")

print("Total wav and ogg files in this directory are: ", totot)

print("")


## THE GHOST OF THE SHADOW ##
