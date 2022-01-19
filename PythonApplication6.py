from MyModule import *
rus_words=[]
eng_words=[]
rus_words=failist_lugemine("rus.txt",rus_words)
eng_words=failist_lugemine("eng.txt",eng_words)

while True:
   menu=input("Rääkida-R, \nKõik sõnad -S, \nTõlkida-T,\nUus sõna-U, \nViga-V, \nKontroll-k;\nLõpp-L")
   if menu.upper()=="U":
       rus_list=uus_sõna("rus.txt", input("новое слово:"))
       eng_list=uus_sõna("eng.txt", input("new word:"))
   elif menu.upper()=="S":
        print(rus_words)
        print(eng_words)
