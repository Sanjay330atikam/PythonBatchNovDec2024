"""
Purpose: reading a csv file(parsing)
"""
#Method1
with open('my_file.csv',mode='r') as fh:
    file_content = fh.read()
# print(file_content.split())
# print()
# print(file_content.splitlines())

names =[]
for each_line in file_content.splitlines()[1:]:
    # print(each_line)
    # to get name
    name = each_line.split(',')[1]
    names.append(name)

print(f"{names =}")
# names =['sam   ', 'sanju ', 'flair ']

with open('my_file.csv',mode='r') as fh:
    file_content = fh.readlines()

#Method 2
names =[]
for each_line in file_content[1:]:
    # print(each_line)
    # to get name
    name = each_line.split(',')[1]
    names.append(name)

print(f"{names =}")
names =['sam   ', 'sanju ', 'flair ']