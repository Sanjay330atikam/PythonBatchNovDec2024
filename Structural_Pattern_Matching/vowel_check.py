letter = input(str("Enter any character : "))
if letter in "aeiou":
    print(f"{letter} is a LOWER VOWEL CHARACTER")
elif letter in "AEIOU":
    print(f"{letter} is a UPPER VOWEL CHARACTER")
else:
    print(f"{letter} by constant")

letter = input(str("Enter any character : "))
match letter:
    case "a" | "e" | "i" | "o" | "u":
        print(f"{letter} is a LOWER VOWEL CHARACTER")
    case "A" | "E" | "I" | "O" | "U":
       print(f"{letter} is a UPPER VOWEL CHARACTER")
    case _:
        print(f"{letter} may be constant")

# case in "aeiou": THis case operator doesnot give efficient answer when we use in operator 
#  print(f"{letter} is a LOWER VOWEL CHARACTER")
# case in "AEIOU"
#       print(f"{letter} is a UPPER VOWEL CHARACTER")


letter = input(str("Enter any character : "))
if letter in "aeiou":
    print(f"{letter} is a LOWER VOWEL CHARACTER")
elif letter in "AEIOU":
    print(f"{letter} is a UPPER VOWEL CHARACTER")
else:
    print(f"{letter} by constant")