wheat = 25
q1    = 30
rice = 12
q2    = 50

a1 = wheat * q1
a2 = rice * q2
total = a1 + a2
print('total selling_price =',total)
subsidy=(total*20)/100
print('subsidy Amount =',subsidy)
final_SP = total-subsidy
print('final Price=',final_SP)
