first = 10
while first >= 1:
    print(first)
    first -= 1

    second = 10
    while second >=1:
        if second == 9:
            break 
        print(f"{first} * {second} =",first * second)
        second -= 1   
        
# first = 0
# while first < 10:
#        first +=1
#        print(f"{first=}")


#        second = 0
#        while second < 10:
#               second += 1
              

#               # F - strings
#               print(f"{first} * {second} = {first * second}")
#        print("=" * 15)