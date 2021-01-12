#!/usr/bin/env python3
#changes all occurences of 'ä' to 'ae', 'ö' to 'oe', 'ü' 'ue', 'ß' to 'ss' and space to '_' in filenames of files in the same folder as this script.
#Ändert alle 'ä' zu 'ae', 'ö' zu 'oe', 'ü' zu 'ue', 'ß' zu 'ss' und Leerzeichen zu '_' in Dateinamen im Ordner, in dem sich das Skript befindet.

import os
from os import listdir
from os.path import isfile, join

path = './'

try:
    fileList = [f for f in listdir(path) if isfile(join(path, f))]

    for f in fileList:
        newName = f.replace('ä', 'ae')
        newName = newName.replace('ö', 'oe')
        newName = newName.replace('ü', 'ue')
        newName = newName.replace('ß', 'ss')
        newName = newName.replace(' ', '_')
        if f != newName:
            os.rename(f, newName)
except(FileNotFoundError):
    print("File not found")
