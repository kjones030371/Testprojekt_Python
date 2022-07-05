
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
        eingabe = input("Gib den Index des zu löschenden Verein an: ")
        if eingabe == '':
            print("Eingabe abgebrochen")
            break
        elif len(vereine) < 1:
            print("Es gibt keine Vereine mehr")
            break
        elif int(eingabe) < len(vereine):
            vereine.pop(index)
        else:
            print("Diesen Index gibt es nicht")
            break
    return vereine


vereine = neue_vereine(vereine)
vereine_bereinigt = set(vereine)
sortierte_liste(vereine)
loesche_verein(vereine)
print(vereine_bereinigt)
sortierte_liste(vereine)

