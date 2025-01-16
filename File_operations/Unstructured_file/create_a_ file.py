"""
Purpose: FIle Operations
   read -r 
   write -w -> If file not present,file will be created
               if present existing content will be overwritten
    append -a 

    default: it is a read mode           
"""

# open('a_first_file.txt')
# python: can't open file '/workspaces/PythonBatchNovDec2024/File_operations/Unstructured_file/Create_a_file.py': [Errno 2] No such file or directory

# open('a_first_file.txt',mode='r')
# on Create_a_file.py
# python: can't open file '/workspaces/PythonBatchNovDec2024/File_operations/Unstructured_file/Create_a_file.py': [Errno 2] No such file or directory

open('a_first_file.txt',mode='w')
print("Sanjay")