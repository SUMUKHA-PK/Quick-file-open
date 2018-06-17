# This module gets the name of the file to be opened
# I am expecting valid commands and creating the parsing logic i.e, "editor_name file_name.extension" format

def extract_name(string,l):
    j = get_space(string,l)
    name = ""
    for i in range(j,l):
        if string[i]=='.':
            break
        name+=string[i]
    return name

def get_space(string,l):
    for i in range(1,l):
        if string[i]==' ':
            return i+1
