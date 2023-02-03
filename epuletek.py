from autom import Auto
autok_marka = []
autok_kora = []
def beolvas():
    f = open("auto.txt", "r", encoding="UTF-8")
    fejlec = f.readline()
    sorok = f.readlines()
    f.close()

    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("$")
        autok_marka.append(sor[0])
        autok_kora.append(sor[1])
        i += 1


def flotta():
    db = 0
    i = 0
    while i < len(autok_marka):
        db += 1
        i += 1
    return db

def kor():
    marka = ""
    gyartas = 0
    i = 0
    while i < len(autok_kora):
        if autok_kora[i] < autok_kora[i-1]:
            marka = autok_marka[i]
            gyartas = autok_kora[i]
        i += 1
    return marka,gyartas
