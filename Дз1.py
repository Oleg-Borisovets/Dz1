a = int(input('Введите вес в кг' ))
b = int(input('Введите рост в см' )) 
c=int(a/(b*b)*10000)
   print('Ваш индекс массы теда равен',c)
f=(c-20)+1
g='20=============================50'
h=(g[0:f]+ '|' +g[f+1:])
   print(h)
