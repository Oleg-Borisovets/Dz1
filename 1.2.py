import os

board=list("""
1|2|3
-----
4|5|6
-----
7|8|9
""")


while True:
    user1=input('Выберете чем будите играть 0/x\t')
    if user1=='x':
        user2 = '0'
        break
    if user1=='0':
        user='x'
        break
    else:
        print('Введен неверный симвал')
print("".join(board))



while True:
    a=input('Выберите ячейку\t')
    
    if a!='1' and a!='2' and a!='3' and a!='4' and a!='5' and a!='6' and  a!='7' and  a!='8' and a!='9':
        
        print('Выброна неверная ячейка')
    else:
       
        if a=='1':f=1
        if a=='2':f=3
        if a=='3':f=5
        if a=='4':f=13
        if a=='5':f=15
        if a=='6':f=17
        if a=='7':f=25
        if a=='8':f=27
        if a=='9':f=29
        os.system('cls')
        if board[f]=='x' or board[f]=='0':
            print('Ячейка занята')
        else:
                  

            board[f]=user1  


        if board[1]==board[3]==board[5] or board[13]==board[15]==board[17] or board[25]==board[27]==board[29] or board[1]==board[13]==board[25] or board[3]==board[15]==board[27] or board[5]==board[17]==board[29] or board[1]==board[15]==board[29] or board[5]==board[15]==board[25]:
            print('Победа', user1)
            break

        if board[1]!='1' and board[3]!='2' and board[5]!='3' and board[13]!='4' and board[15]!='5' and board[17]!='6' and board[25]!='7' and board[27]!='8' and board[29]!='9':
            print('Победила дружба')
            break

        print("".join(board))


        
        if user1=='x':
            user1='0'
        else:
            user1='x'
        
