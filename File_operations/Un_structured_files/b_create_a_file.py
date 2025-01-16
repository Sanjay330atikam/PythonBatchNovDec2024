"""
Purpose:Creating a file and adding content
"""

fh = open('second_file.txt',mode='w',encoding='utf-8')
print('Name of the file:',fh.name)
print('Opening mode:',fh.mode)
print()


#---ADDDING CONTENTS TO FILE---
fh.write("This is first line \n")
fh.write("This is second line \n")
fh.flush()# to avoid the data lekages in file

print("Closed or not",fh.closed)
fh.close()
print("Closed or not:",fh.closed)


# REOPENING THE SAME FILE - IN WRITE MODE
# while reopening all the contents will vbe overwritten with 
# the existing contents in the file
sh = open('second_file.txt',mode='w',encoding='utf')
sh.write("This is Third line \n")
sh.flush()
sh.close()

# ADDING CONTENTS TO THE EXISTING FILE - APPEND
# contents can be added to existing file without overwritting
s = open('second_file.txt',mode='a')
s.write("This is Fourth Line \n")
s.flush()
s.close()


# TRUNCATE()-This method is used to restrict the file to the given number of content 
a = open('second_file.txt','a')
a.truncate(15)
# Before Truncate
    # This is Third line 
    # This is Fourth Line 
# After Truncate(15)
    # This is Third l


# open and read file after truncate()
f = open('second_file.txt','r')
print(f.read())