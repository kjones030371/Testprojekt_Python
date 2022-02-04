import locale

locale.setlocale(locale.LC_ALL, 'de_DE')
weitere_berechnung = 'J'
umsatz = 0

def kassenvorgang():
    preis = input('Gib den Preis ein:\t\t')
    rabatt = input('Gib den Rabatt in % ein:\t')
    zahlung = input('Der Kunde zahlt: \t\t ')
    preis = locale.atof(preis)
    zahlung = locale.atof(zahlung)
    rabatt_in_prozent = locale.atof(rabatt)
    rabatt_in_euro = (preis / 100) * rabatt_in_prozent
    rabatt_preis = preis - rabatt_in_euro
    if rabatt_preis > zahlung:
        print("Die Zahlung ist zu wenig -- Bitte um Neueingabe ")
        kassenvorgang()
    else:
        rueckgeld = zahlung - rabatt_preis
        print('Der Rabatt beträgt: ', locale.format_string('%.2f', rabatt_in_euro))
        print('Der neu berechnete Preis ist: ', locale.format_string('%.2f', rabatt_preis))
        print('Wechselgeld:\t\t', locale.format_string('%.2f', rueckgeld, ))
    return rabatt_preis

print("Kassensystem")
while weitere_berechnung == 'J' or weitere_berechnung == 'j':
    umsatz = umsatz + kassenvorgang()
    weitere_berechnung = input("Haben Sie noch eine weitere Eingabe (J == Ja oder N == nein): ")
print("Der Umsatz beträgt: ", umsatz)
print("Programmende")

