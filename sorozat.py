import random
szamok = []

def lottoszamok():
    i = 0
    while i < 5:
        number = int(random.random()*100)+1
        if i < 4:
            print(number, end=";")
        else:
            print(number)
        szamok.append(number)
        i += 1

def egyjegyuek_szama():
    egyjegyu = 0
    i = 0
    while i < len(szamok):
        if szamok[i] < 10:
            egyjegyu += 1
        i += 1
    return egyjegyu


def konzol_kiir(egyjegyu):
    return egyjegyu

def file_kiir():
    fajlom = open("szamok.txt", "w", encoding="UTF-8")
    fajlom.write(f"II/F \n")
    fajlom.write(f"A fejek száma: {egyjegyuek_szama()}")
    fajlom.close()