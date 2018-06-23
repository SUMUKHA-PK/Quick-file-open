# Quick-file-open

Introduction:
  Whenever you need to write code, it needs pre-processor directives that are cumbersome to write everytime you start a new project.
  This is a simple program to help in getting that task done.

Currently support for C, CPP , Java and Python exists and in future I intend to extend for other programming languages.
Also, currently the script must first be run and then the command must be typed in.  
Further extensions are to use the script from any location, add files in any location and provide support without running the script.  

File Structure:
  1. main_file     : Script that needs to be run to be run to complete desired tasks.
  2. extraction.py : This module helps in parsing the data.

Update :  
  Support for accessing script anywhere is added.    
  To do so, first enter ```chmod +x /path_to_file/main_file.py```   
  Then wherever you want to create the file run the command ```python3 main_file.py```  
  Follow further instructions according to script  
