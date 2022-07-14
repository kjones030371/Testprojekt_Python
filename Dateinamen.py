def kurzer_dateiname(datei_name):
    anfang = datei_name[0:6]
    ende = datei_name[-3:]
    trenner = datei_name.index('-')
    zahlen = datei_name[trenner + 1:trenner + 3]
    neuer_name = anfang.lower() + zahlen + '.' + ende
    return neuer_name

namen=('Grabung-42-Ebene1-jpg','Grabung-92-Hoehl92.pdf','Dschungel-42-Gebaeude.jpg')
for name in namen:
 print (kurzer_dateiname(name))

