
die_vereine = [
    "1. FC Dinkel",
    "SpVgg Hornberg",
    "1. FC Übern Berg",
    "2. FC Für die Katz",
    "SpVgg Hanebüchen"
]

weitere_vereine = [
    "1. FC Dreikäsehoch",
    "Die Bananen",
    "Die Vollpfosten"
]
die_vereine.append("Schutterballer")
die_vereine.extend(weitere_vereine)
die_vereine.remove("SpVgg Hornberg")
die_vereine.insert(1, "Die Superlativen")
#die_vereine.insert(2, weitere_vereine)

die_copy_liste = die_vereine.copy()


die_vereine.sort()
print(die_vereine)
die_vereine.sort(reverse=True)
print(die_vereine)
print(die_copy_liste)

tore = [5, 7, 1, 3, 9, 11, 0]
versuche = len(tore)
bestes_ergebnis = max(tore)
schlechtestes_ergebnis = min(tore)
print(versuche, bestes_ergebnis, schlechtestes_ergebnis)

print(tore[3:5])

eine_liste = list(range(2, 9, 2))
print("Eine Liste: ", eine_liste)

spieler_liste = ["Hansi", "Bernd", "Diego", "Basti", "Riccardo", "John"]

for index in range(0, 6, 2):
    print(spieler_liste[index], spieler_liste[index+1])

for i in range(0, len(spieler_liste), 2):
    print(spieler_liste[i:i+2])

for spieler in enumerate(spieler_liste):
    print(spieler)

for nummer, spieler in enumerate(spieler_liste):
    print("Der Spieler", spieler, "hat die Numer", nummer)

spam = [7, "hallo", 3, 42]
def magische42(listen_wert):
    if listen_wert == 42:
        return -1
    if type(listen_wert) == str:
        return len(listen_wert)
    if type(listen_wert) == int:
        return listen_wert

spam.sort(key=magische42)
print(spam)

magische42(spam)
geloescht = spam.pop(1)
zaehler = spam.count("hallo")
print(zaehler)
print (geloescht)

print(spam)


