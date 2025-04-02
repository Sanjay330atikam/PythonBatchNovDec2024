"""
Purpose: File Operations
    r - read 
    w - write -> If file is not present file will be created
              -> If present existing content will be overwritten

    a - append

    default is read mode
"""
# To open a FILE---!!---
file_handler=open("first_file.txt",mode='w')
print(f"{type(file_handler) =}")
print(f"{file_handler   =}")
print()

#--TO ADD CONTENTS TO FILE--!!
file_handler.write('This is first line\n')
file_handler.write('This is second line\n')
file_handler.close()