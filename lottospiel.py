import random
#Lottospiel

lottozahlen = [4, 14, 34, 37, 40, 49]
zahlen = [0, 0, 0, 0, 0, 0]
n = 0
treffer = 0
tmp = random.uniform(1, 49)


print("Lottospiel")
print("Du musst 6 Zahlen zwischen 1 und 49 eingeben")
# Eingabe
while n < 6:
    zahlen[n] = int(input("Gib die " + str(n+1) + ". Lottozahl ein: "))
    if zahlen[n] > 0 and 50 > zahlen[n]:
        n += 1
    else:
        print ("Deine Zahl liegt nicht zwischen 1 und 49 -- Bitte nochmal eingeben")
print(zahlen)

# Vergleich
for eingabezahl in zahlen:
    for lottozahl in lottozahlen:
        # print("Vergleich: " + str(eingabezahl) + "==" + str(lottozahl))
        if eingabezahl == lottozahl:
            print ("Vergleich: " + str(eingabezahl) + "==" + str(lottozahl))
            treffer += 1
# Auswertung
if treffer == 1:
    print(" Du hast im Lotto eine richtige Zahl")
else:
    print(" Du hast im Lotto " + str(treffer) + " richtige Zahlen")





