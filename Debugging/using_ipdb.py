# " " " 
# # Purpose: Debugging with ipdb
# # To install ipdb 
# # pip install -U ipdb --user
# pip install -U ipdb --user
# # Task- display all even numbers

# To make ipdb as a default while using the breakpoint(),
# export PYTHONBREAKPOINT = ipdb.set_trace

# " " "
numbers = range (1,100)

# import ipdb; ipdb.set_trace()
breakpoint()

for each_num in numbers:
    if each_num % 2==0:#each_num % 2
        print(f"{each_num =}")

