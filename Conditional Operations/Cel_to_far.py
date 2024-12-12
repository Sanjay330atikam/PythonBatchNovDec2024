# constant = (9/5)+32
# User_input = input("Enter your temperature = ")
# if User_input == "C" or User_input == "c":
#     temperature = float(User_input[:-1])
#     unit ="Celsius"
# else:
#     print("Please enter temperature with C")

# print(f"The temperature is {temperature} {unit}")
# # farenheit = (input*float(constant))
# # print(farenheit,f"{'F'}")


print(f"{'Celsius to Farenheit Conversion'}".upper())
value = input("Enter your temperature in Clesisus : ")

if value[-1] == 'C' or value[-1] == 'c':
    temperature = float(value[:-1]) 
    unit = 'Celsius'
else:
    print(" Eenter the temperature with a valid unit 'C'!!!.")
    exit()

print(f"The temperature is {temperature}° {unit}.")

constant = (temperature * 9/5) + 32
print(constant,f"{'Farenheit'}")

print(f"{'Farenheit to Celsius Conversion'}".upper())

value = input("Enter your temperature in Farenheit : ")
if value[-1] == 'F' or value[-1]=='f':
    temperature = float(value[:-1])
    unit = 'Farenheit'

else:
    print("Enter the temperature with a valid unit 'F'!!!!! ")

print(f"The temperature is {temperature}° {unit}.")

constant = (temperature - 32) * 5/9
print(constant.__round__(2),f"{'Celsisus'}")

