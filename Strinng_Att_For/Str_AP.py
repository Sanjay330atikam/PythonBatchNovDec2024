name = "Sanjay"
var = "goud "

full_name = name.__add__(var)
print(full_name.isidentifier())

m = 'Samu'
print(m.isidentifier())#first charcter should be either lower or Upper case


mv = 'Saregamanpasaregapama'
print(mv.find('a',9))
print(mv.find('l'))#gives -1 
#print(mv.index('l'))


n= '         sanjay has earned 120k a year.     '
print(n.strip())
print(n.rstrip())
print(n.lstrip())


i ='7'
print(i.zfill(3))#.used to fill the mentioned spaaces with zeros. 


kk = "Micheal Jordan is Legendary Basket Ball Player"
ll ='12345678910'
print(kk.split())
print(kk.split('Micheal'))
print(kk.split('a'))

print(kk.split(' '))
print(ll.split('0',maxsplit=3))
# # In SPLIT we cant give index positio to split the particualar character.
print()
print(kk.partition('a'))
print(kk.partition('Micheal'))
print(ll.partition('2'))
print(kk.partition('4'))




