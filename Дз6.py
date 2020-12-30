def func1():
    print('Добро пожаловать в веб приложения')

def func2():
    print('Вывод интересующей информации ')
l=[]
def func4(): 
    
    while True:
        global l
        x=input('Регистрация пользователя \t')
        if x not in l:
            l.append(x)
            return l
        else:
            print('Имя занято')
            break       

def func5(dec1):
    def dec2():
        b=input('Введите имя пользователя для авторизации \t')
        global l
        if b not in l:

            print ('Пользовател не зарегитрирован')
            return dec2
                    
        dec1()
    return dec2


@func5
def func3():
    print('Данные которые доступны авторизованным пользователям')      

while True:
    a=int(input('Меню выбора действий. Вывод приведствия нажмите 1.Вывод информации нажмите 2. Получить недостающую информацию нажмите 3(нужна авторизации). Регистрация пользователя нажмите 4. Выход нажмите 7 \t'))
    if 1==a:
        func1()
        
    if 2==a:
        func2()
        
    if 3==a:
        func3()
   
    if a==7:
        print('Выход')
        break

    if a==4:
        func4()


 
  






   
        



    


    
