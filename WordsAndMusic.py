#This code imports the necessary modules.

import os
import datetime

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))
  

srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Acid_Loops'

content =[]

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav"): 
            #content.append(filepath)
            astr = str(file)
            bstr = astr[0:-4]
            x = bstr.split()
            for elem in x:
                y = elem.isalpha()
                if y:
                    content.append(elem)

worddic= {}

for elem in content:
    if elem not in worddic:
        worddic[elem] = 1
    if elem in worddic:
        anum = worddic[elem]
        bnum = anum + 1
        worddic[elem] = bnum


songmagic = sorted(worddic.items(), key=lambda x: x[1], reverse=True)

mlen = len(songmagic)
muslen = str(mlen)

op = "musicwords " + tim + ".txt"

outfile = open(op, "w")

outfile.write("Here are words found in these files, in order of the number of times they appear:" + '\n')
outfile.write("There are a total of " + muslen + " words included in this list." + '\n')
outfile.write('\n')

for elem in songmagic:

    astr = elem[0] + ": " + (str(elem[1])) + '\n'
    outfile.write(astr)

outfile.close()

print("")
print("Your word list has been created, and that document can be found in the same folder as this code. Thank you.")
print("")

opp = "notepad.exe musicwords " + tim + ".txt"

os.system(opp)

## THE GHOST OF THE SHADOW ##
