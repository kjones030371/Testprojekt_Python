
def zahlendreher(zahl):
    if zahl > 5:
        zahl = zahl - 1
        print(zahl)
        zahl = zahlendreher(zahl)
        return zahl
    return zahl

zahl = int(input("Gib eine Zahl ein: "))
zahl = zahlendreher(zahl)
print(zahl)
