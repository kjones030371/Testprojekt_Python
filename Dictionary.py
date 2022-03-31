# Dictionary -- Key/Value Paare

spam = {}
key = input("Gib den Schluessel ein: ")
value = input("Zugehöriger Wert: ")
spam[key] = value
print (spam)

ergebnis_11_meter = {"John": 3, "Schroedinger": 1}
for schluessel in ergebnis_11_meter:
    print("Spieler", schluessel,"hat", ergebnis_11_meter[schluessel], "Tore geschossen")

for ein_tupel in ergebnis_11_meter.items():
    print(ein_tupel)

for spieler, ergebnis in ergebnis_11_meter.items():
    print(spieler, ergebnis)


