test_string=input("enter a string =")
print('test_case = ',test_string)

reverse_string = test_string[::-1]
print('reverse_string = ',reverse_string)

print('test_case == reverse_string =',test_string == reverse_string)

if (test_string == reverse_string):
    print("Given String is Plaindrom")
else: 
     print("Given string is not palindrome")