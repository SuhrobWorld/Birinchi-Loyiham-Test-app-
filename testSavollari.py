from datetime import datetime
import random 
randomnNumber = random.randrange(0,60)
secondWrongNumber = random.randrange(0,60)
now = datetime.now()

javob = now.strftime("%H:%M")
wrong = now.strftime("%H")


tel = int(input("Telefon raqamingizni kiriting\n>>>>"))
birth = input("Tug'ilgan sanani kiriting(misol: 25 02 1998)")

q = print("Savollar boshlandi...") 
q1 = input("1)Universitet necha kursdan iborat bo'ladi? \nA)3\nB)1\nC)4\n>>>> ")
if q1.lower() == 'c':
    print("Javobingiz to'g'rri\n")
else:
    print("Javob noto'g'ri\n")
q2 = input("2)Iqtisod talabasisiz.Qancha kantrakt to'laysiz? \nA)8mln\nB)4mln\nC)5mln\n>>>> ")
if q2.lower() == 'a':

    print("Javobingiz to'gri\n")
else:
    print("Javob notog'ri\n")
q3 = input("3) 2+2*2-2/2*2-2-2*2+2 // Qiymatini toping \nA)2\nB)0\nC)4\n>>>> ")
if q3.lower() == 'b':
    print("Javobingiz to'g'ri\n")
else:
    print("Javob noto'g'ri\n")
q4 = input("4)Payg'ambarimiz yashab o'tgan yillari \nA)570-631\nB)571-632\nC)570-630\n>>>> ")
if q4.lower() == 'b':
    print("Javobingiz to'g'ri\n")
else:
    print("Javob noto'g'ri\n")
q5 = input("5)Shom nomozi necha rakat? \nA)Uch rakat farz va ikki rakat Sunnat\nB)To'yrt rakat farz\nC)To'rt rakat farz ikki rakat sunnat\n>>>> ")
if q5.lower() == 'a':
    print("Javobingiz to'g'ri\n")
else:
    print("Javob noto'g'ri\n")
q6 = input(f'6)Aniq vaqt yoki "~1 minutb" yozing \nA){javob}\nB){wrong}:{randomnNumber}\nC){wrong}:{secondWrongNumber}\n>>>>')
if q6.lower() == 'a':
    print("Javobingiz to'g'ri\n")
else:
    print("Javob noto'g'ri\n")
q7 = input("7)O'zbekiston qachon mustaqil bo'lgan? \nA)1999\nB)1990\nC)1991\n>>>>")
if q7.lower() == 'c':
    print("Javobingiz to'g'rri\n")
else:
    print("Javob noto'g'ri\n")

x = birth.split()
q8 = input("8)Tug'ilgan kuningizni yozing(misol:08,15,02)\n>>>>")
if q8 == x[0]:
    print("Javobingiz to'g'ri\n")
else:
    print("Javob noto'g'ri\n")
q9 = input("9)Stiv Jobs kim? \nA)Fransya tatbirkori\nB)Apple asoschisi\nC)Micrasoft asoschisi\n>>>>")
if q9.lower() == 'b':
    print("Javobingiz to'g'rri\n")
else:
    print("Javob noto'g'ri\n")
q10 = input("10)Paport nechayoshdan beriladi? \nA)16\nB)17\nC)18\n>>>>")
if q10.lower() == 'a':
    print("Javobingiz to'g'rri\n")
else:
    print("Javob noto'g'ri\n")
q11 = input("11)Oltin medal kimlarga beriladi? \nA)Kambag'alarga\nB)G'oliblarga\nC)Ikkinchi o'rinlarga")
if q11.lower() == 'b':
    print("Javobingiz to'g'rri\n\n")
else:
    print("Javob noto'g'ri\n\n") 
print("Test yakunlandi....\n\n")
 


