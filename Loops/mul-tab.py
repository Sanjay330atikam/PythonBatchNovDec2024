# # two independent while loop
# first = 0
# while first < 5:
#     first +=1
#     print(first)

#second = 0
# while second < 5:
#     second +=1
#     print(second)

#second while loop under first loop 
first = 0
while first < 10:
       first +=1
       print(f"{first=}")


       second = 0
       while second < 10:
              second += 1
              #print(f"\t{second = }")
              #print("first * second = " ,first * second)
              #ols style formatting.
              #print('%d * %d = %d'%(first,second,first * second))
              #print('%2d * %2d = %3d'%(first,second,first * second))

              # new style formating
              #print('{} * {} = {}'.format(first,second,first * second))
              #print('{0} * {1} = {2}'.format(first,second,first * second))
              #print('{0:1} * {1:1} = {2:2}'.format(first,second,first * second))
              #print('{:2} * {:2} = {:3}'.format(first,second,first * second))

              # F - strings
              print(f"{first} * {second} = {first * second}")
       print("=" * 15)
              
       

     

