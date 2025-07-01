file_handler = open("Third_file.txt",mode="w")
print(f"{type(file_handler) =}")
print(f"{file_handler}")

# adding contetnt
file_handler.write("Sanjay \n")
file_handler.write("Goud\n")

file_handler.close()