print('{}.py').format('Борисовец Олег Геннадьевич')






a='Не знаю, как там в Лондоне, я не была. Может, там собака - друг человека. А у нас управдом - друг человека!'



#1 Посчитать количество символов
print("Посчитать количество символов")
print(len(a))

#2 Развернуть строку
print('Развернуть строку')
print(a[::-1])

#3 Сделать каждое слово с большой буквы
print('Сделать каждое слово с большой буквы')
print(a.title())


#4 Сделать весь текст прописными буквами
print('Сделать весь текст прописными буквами')
print(a.upper())


#5 Найти число вхождений "нд", "ам", "о" в строку 
b=(a.lower()) # (сделал всю строку маленькими буквами для того что бы  подсчет вхождений карректно работал. так как если с большой буквы то этот элемент не будет подсичан)
print('число вхождений нд')
print(b.count('нд'))
print("число вхождений ам")
print(b.count('ам'))
print("число вхождений о")
print(b.count('о'))


#6 Собственные упражнения
print ("Удалить симвалы с 0 по 8")
print(a[:0]+a[8:])
 
#7 Вывести в консоль исходную строку
print('Исходная строка')
print(a)

 



  
