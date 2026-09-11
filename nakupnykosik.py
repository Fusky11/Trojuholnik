ovocie = ["jablko", "banan", "hruska", "marhula", "slivka"]
zelenina = ["mrkva", "petrzlen", "celer", "zemiak"]
sladkosti = ["cokolada", "cukor"]

nakupny_kosik = []

while True:
    print("co chcete pridat do kosika?")
    vstup = input()
    if vstup == "uz nic" or vstup == "koniec":
        break 
    else: 
        nakupny_kosik.append(vstup)

print("-------------------------------------------------------------------------------------------")

for polozka in nakupny_kosik: 
    if polozka in ovocie:
        print(f"{polozka} je ovocie")
    elif polozka in zelenina:
        print(f"{polozka} je zelenina")
    else:
        print(f"{polozka} je nieco ine")
