a = [3,4,12,76,22,41,28,1234,67,52,'table','chair','towel','apple','floor','end','cat','car','dog','pig']
list_int = [x for x in a if isinstance(x,int)]
list_str = [x for x in a if isinstance(x,str)]

list_int.sort()
list_str.sort()
b = list_int + list_str
c = [x for x in list_int if x%2==0]
d = [x.upper() for x in list_str]

print('Головний список:', a)
print('Відсортований список' , b)
print('Числа кратні двом' , c)
print('Список слів записані капсом' , d)
