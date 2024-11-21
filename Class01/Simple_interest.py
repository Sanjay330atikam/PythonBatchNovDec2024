A = 11937.50
P = 10000.00
R = 3.875
T = 5
I = A - P
number = '$'+ str(I)
print('Interest is =',number)
r = R%100
rate = str(r) + '%'
print('Rate is =',rate)
# A = P +(1 + (r*T))
# print(A)
Interest = P +(1 + (r*T))
Simple_Interest = '$' + str(Interest)
print('Simple_Interest is =',Simple_Interest)