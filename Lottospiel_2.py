# Lottospiel
# author: Christian Krienzer
# Date: 31.01.2022
# Version: 1.0

lotto_numbers = [4, 14, 34, 37, 40, 49]

# do_print: Das Lottoergebnis wird auf dem Bildschirm dargestellt
def do_print(match, numbers, lotto_numbers):
    if match == 1:
        print("Du hast im Lotto eine richtige Zahl")
    else:
        print("Du hast im Lotto " + str(match) + " richtige Zahlen")
    numbers.sort()
    lotto_numbers.sort()
    print("Dein Tippschein:", end= "\t")
    print(str(numbers))
    print("Die Gewinnzahlen:", end='\t')
    print(str(lotto_numbers))

#  do_diff: Vergleicht die Lottozahlen mit dem Tippschein des Users
def do_diff(numbers, lotto_numbers):
    match = 0
    for user_number in numbers:
        for lotto_number in lotto_numbers:
            if user_number == lotto_number:
                print("Vergleich: " + str(user_number) + "==" + str(lotto_number))
                match += 1
    return match

# do_input: Tippschein des Users wird befuellt und geprueft
def do_input(lotto_numbers):
    # Eingabe
    numbers = [0, 0, 0, 0, 0, 0]
    user_input = 0
    n = 0
    print("Lottospiel")
    print("Du musst 6 Zahlen zwischen 1 und 49 eingeben")
    while n < 6:
        user_input = int(input("Gib die " + str(n + 1) + ". Lottozahl ein: "))
        # Pruefung der Eingabe zwischen 1 und 49
        if user_input > 0 and 50 > user_input:
            for elements in numbers:
                # Pruefung doppelter Eingaben
                if elements == user_input:
                    tmp = True
                    break
                else:
                    tmp = False
            if tmp == False:
                numbers[n] = user_input
                n += 1
            else:
                print("Deine Zahl gibt es schon -- Bitte nochmal eingeben")
        else:
            print("Deine Zahl liegt nicht zwischen 1 und 49 -- Bitte nochmal eingeben")
    return numbers

numbers = do_input(lotto_numbers)
match = do_diff(numbers, lotto_numbers)
do_print(match, numbers, lotto_numbers)









