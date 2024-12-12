# Escape Sequences
#   \t = tab Space 
#   \n = new line 
#   \r = rare feed
##\t,\n will function their functionally like giving newline and tab space
# without displaying in the output
print("Sanjay Goud")
print("Sanjay\tGoud")
print("Sanjay\nGoud")

print("Sanjay\rGoud")
print("Goud\rSanjay")
print("12345\rDOG")
print("DOG\r12345")


data_set = range (-100, 10_000)
data_set_length = len(data_set)

#'_' used to replace multiple value and store it in buffer variables.
# for num in data_set:
#     print(num)

for loop_index,_ in enumerate(data_set): 
  percent_completed = (loop_index / data_set_length) * 100
  percent_completed= round (percent_completed,2)
  print(f"\r{loop_index =},{data_set_length =},{percent_completed},",end="")
  print(f"{percent_completed:5} completed",end='')