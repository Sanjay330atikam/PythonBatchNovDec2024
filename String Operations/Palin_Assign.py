test_sentence = input("Enter a sentence ignoring whitespace:")
print('test_sentence = ',test_sentence)

reverse_sentence = test_sentence[::-1]
print('reverse_sentence = ',reverse_sentence)

print('test_sentence == reverse_sentence = ',test_sentence==reverse_sentence)
if(test_sentence==reverse_sentence):
    print("Given sentence is in plaindrome")
else:
    print("Give sentence is not in Plaindrome")