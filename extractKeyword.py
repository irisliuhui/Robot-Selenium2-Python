#!/usr/bin/python
# Filename: extract.py
# used for extract keywords and variables to reference.

import fnmatch
import os
import re

path = r'C:/workspace/RobotCase/Robot/Resource/'
destFile = 'keywords.txt'

filePattern = fnmatch.translate('*.tsv')

#sourceF = str(raw_input('Enter an source file name : '))
#print [sourceF]
#shutil.rmtree('keywords.tsv')
if os.path.isfile(destFile):
    os.remove(destFile)

key1 = "*Variables*"
key2 = "####"
key3 = "*Keywords*"
key4 = "*** "
key5 = "	"



f2 = file(destFile, 'a') # open for 'w'riting

for fileName in os.listdir(path):
    if re.match(filePattern, fileName):
        print f2.write(fileName+'\t')

# if no mode is specified, 'r'ead mode is assumed by default
#exact the keyword defined.
for fileName in os.listdir(path):
    if re.match(filePattern, fileName):
        f = file(path+fileName)
        print f2.write('\n\n--------------'+fileName+'-------------- \n')
        while True:
            line = f.readline()
            #line.strip() 
            #f2.write(line)
            if len(line) == 0: # Zero length indicates EOF
                break
            #elif key1 in line:
            elif line.startswith(key3):
                while True:                 
                    #print [line]
                    #line = f.readline()
                    if line.startswith(key5):
                        line = f.readline()
                    elif (len(line) == 0):
                        break
                    else:
                        print f2.write(line)
                        line = f.readline()
                    continue

#extract the para name
            elif line.startswith(key2) or line.startswith(key1):
                while True:
                    print f2.write(line.split(key5)[0])
                    print f2.write('\n')
                    #print [line]
                    line = f.readline()
                    if len(line) == 0: # Zero length indicates EOF
                        break
                    continue
        f.close() # close the file

                #print f2.write(line)
    # Notice comma to avoid automatic newline added by Python

#S.startwith(prefix[,start[,end]]) 
#S.strip([chars]) 
f2.close()
