
vereine = []
index = 0

def neue_vereine(vereine):
    abbruch_laenge = 3
    while True:
        eingabe = input("Gib den Vereinsnamen ein: " )
        if len(eingabe) > abbruch_laenge:
            vereine.append(eingabe)
        else:
            break
    return vereine

def sortierte_liste(vereine):
    vereine.sort()
    zaehler = 0
    for element in vereine:
        print(str(zaehler) + ": " + element)
        zaehler += 1

def loesche_verein(vereine):
    while True:
        index = int(input("Gib den Index des zu löschenden Verein an: "))
        if index < len(vereine):
            vereine.pop(index)
        else:
            print("Diesen Index gibt es nicht")
            break
    return vereine


vereine = neue_vereine(vereine)
sortierte_liste(vereine)
loesche_verein(vereine)
sortierte_liste(vereine)

