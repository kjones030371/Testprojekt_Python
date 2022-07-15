def kurzer_dateiname(datei_name):
    anfang = datei_name[0:6]
    ende = datei_name[-3:]
    trenner = datei_name.index('-')
    zahlen = datei_name[trenner + 1:trenner + 3]
    anfang = anfang.lower()
    if anfang.isalpha() and ende.isalpha() and zahlen.isnumeric():
        neuer_name = f"{anfang}{zahlen}.{ende}"
        neuer_name = neuer_name.lower()
        return neuer_name
    else:
        None

namen=('Grabung-42-Ebene1-jpg','Grabung-xx-Hoehl92.pdf','Dschungel-42-Gebaeude.jpg')
for name in namen:
    neuer_name = kurzer_dateiname(name)
    laenge = len(name)
    ergebnis = f"'{name}' mit {laenge} Zeichen. Neuer Name: '{neuer_name}'"
    print(ergebnis)


