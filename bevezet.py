autonev = []
autodatum = []

def auto_nev_ev():
    i = 0
    while i < 2:
        auto_nev = input(f"Kérlek adj meg egy autó márkát!")
        autonev.append(auto_nev)
        auto_datum = int(input(f"Kérlek adj meg egy autó gyártási évet!"))
        autodatum.append(auto_datum)
        i += 1

def auto_szoveg():
    i = 0
    while i < len(autonev):
        print(f"{i+1}.\t Autó neve:{autonev[i]}")
        print(f"\t Gyártási dátum: {autodatum[i]}")
        i += 1


def auto_gyartas():
    i = 0
    while i < len(autodatum):
        if autodatum[i] == 2023:
            print(f"\t Ez a/az {autonev[i]} friss gyártás!")
        if autodatum[i] < 2000:
            print(f"\t Ez a/az {autonev[i]} öreg autó gyártás!")
        if autodatum[i] >= 2000 and autodatum[i] < 2023:
            print(f"\t Ez a/az {autonev[i]} átlagos korú gyártás!")
        i += 1







