# Zahlenraetsel
match = 7
points = 1
print("Start Zahlenraetsel")
print("Du musst eine Zahl zwischen 0 und 10 eingeben")
value1 = int(input("Gib einen Wert ein: "))
while match != value1:
    if value1 > 10:
        print("Dein Eingabewert war zu hoch ")
    value1 = int(input("Gib einen Wert ein: "))
    points += 1
    if points > 10:
        value1 = match
if points < 3:
    print("Super, du hast Versuche " + str(points) + " benötigt")
elif points < 6:
    print("Noch gute Leistung, du hast Versuche " + str(points) + " benötigt")
elif points < 11:
    print("Du solltest mehr ueben, du hast Versuche " + str(points) + " benötigt")
else:
    print("Du hast Versuche " + str(points) + " benötigt. Das Programm wurde abgebrochen")

print("Programmende")





























