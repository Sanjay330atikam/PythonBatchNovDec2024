print('%d %d'%(12,24))
print('My age is %d and my salary is %d thousand '%(25,100))
print('My age is %3d and my salary is %3d thousand '%(25,100))
print()

print('My name is %s and my weight is %f'%('sanjay',185.89))


num = 123.456789123
print('%d'%num)
print('%f'%num)
print('%10f'%num)
print('%10.5f'%num)

import math
print('%f'%math.pi)
print('%10f'%math.pi)
print('%10.5f'%math.pi)
print()

ll='123456'
print('{}'.format('SanjayGoud'))
print('{:<20}'.format('SanjayGoud'))
print('{:>20}'.format('SanjayGoud'))
print('{:$^20}'.format('SanjayGoud'))
print('{:0=10}'.format(123456))
print('{:10}'.format(123456))
print('{:a=10}'.format(123456))
print(ll.zfill(10))


print(f"{'name':>30}")
print(f"{'sanjay'}")