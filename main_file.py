# This is the main file that does all the work

import os
import sys
import extraction

string = input("Enter the command: ")
l = len(string)

CPP = ".cpp"
PY  = ".py"
C   = ".c"

Input_Cpp = "#include<bits/stdc++.h>\nusing namespace std;\nint main(){\n\nreturn 0;\n}\n"
Input_Py  = "if __name__ =='__main__'\n"
Input_C   = "#include<stdio.h>\nint main(){\n\nreturn 0;\n}"

name = extraction.extract_name(string,l)

if CPP in string:
    file = open(name+CPP,"w+")
    file.write(Input_Cpp)
elif PY in string:
    file = open(name+PY,"w+")
    file.write(Input_Py)
elif C in string:
    file = open(name+C,"w+")
    file.write(Input_C)
