LUCKY_NUMBER = 45
guessed_number = int(input("Enter a number between 0 to 100 of your choice.!! = "))
print(f"{LUCKY_NUMBER}")
print(f"{guessed_number}")
print(f"{LUCKY_NUMBER==guessed_number}")

if(LUCKY_NUMBER==guessed_number):
    print("HURRAYH YOU GUESSED CORRECTLY    !!!")
elif guessed_number>LUCKY_NUMBER:
    print("PLEASE TRY AGAIN BY REDUCING YOUR GUESSED NUMBER")
elif guessed_number<LUCKY_NUMBER:
    print("PLEASE TRY AGAIN BY INCREASING YOUR GUESSED NUMBER")