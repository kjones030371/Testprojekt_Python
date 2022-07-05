datei_name = "Grabung-42-Ebene1-jpg"
print(len(datei_name))

anfang = datei_name[0:6]
print(anfang)

ende = datei_name[-3:]
print(ende)

trenner = datei_name.index('-')
print(trenner)

zahlen = datei_name[trenner+1:trenner+3]
print(zahlen)
# So soll es sein
