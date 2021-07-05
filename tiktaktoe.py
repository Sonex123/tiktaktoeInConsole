import os


def printField(f):
    print(f[1], "|", f[2], "|", f[3])
    print("-- --- --")
    print(f[4], "|", f[5], "|", f[6])
    print("-- --- --")
    print(f[7], "|", f[8], "|", f[9])


def checkWon(field):
    check = False
    a = field[1]
    b = field[2]
    c = field[3]
    d = field[4]
    e = field[5]
    f = field[6]
    g = field[7]
    h = field[8]
    i = field[9]

    if a + b + c == "XXX":
        return [True, "X"]
    elif a + b + c == "OOO":
        return [True, "O"]

    elif d + e + f == "XXX":
        return [True, "X"]
    elif d + e + f == "OOO":
        return [True, "O"]

    elif g + h + i == "XXX":
        return [True, "X"]
    elif g + h + i == "OOO":
        return [True, "O"]

    elif a + e + i == "XXX":
        return [True, "X"]
    elif a + e + i == "OOO":
        return [True, "O"]

    elif c + e + g == "OOO":
        return [True, "O"]
    elif c + e + g == "XXX":
        return [True, "X"]

    elif a + d + g == "XXX":
        return [True, "X"]
    elif a + d + g == "OOO":
        return [True, "O"]

    elif b + e + h == "XXX":
        return [True, "X"]
    elif b + e + h == "OOO":
        return [True, "O"]

    elif c + f + i == "XXX":
        return [True, "X"]
    elif c + f + i == "OOO":
        return [True, "O"]

    return [False, ""]


def fullField(field):
    for i in field.values():
        if i == " ":
            return False
    return True


field = {
    1: " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " ",
}

last = "X"
won = False

while not won:
    printField(field)
    print("Aktueller Spieler:", last)
    c = False
    while not c:
        try:
            ind = int(input("Wo möchtest du setzen? "))
            if ind < 1 or ind > 9:
                print("Gib ein gültiges Feld an!")
                continue
        except:
            print("Gib ein gültiges Feld an!")
            continue
        if field[ind] == " ":
            field[ind] = last
            c = True
        else:
            print("Das Feld ist bereits belegt!")

    os.system("clear")
    if last == "X":
        last = "O"
    else:
        last = "X"

    ret = checkWon(field)
    if ret[0]:
        print(f"Spieler {ret[1]} hat das Spiel gewonnen!")
        printField(field)
        break
    if fullField(field):
        print("Es ist unentschieden!")
        printField(field)
        break
