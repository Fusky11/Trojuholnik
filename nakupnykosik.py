ovocie = ["jablko", "banan", "hruska", "marhula", "slivka"]
zelenina = ["mrkva", "petrzlen", "celer", "zemiak"]
sladkosti = ["cokolada", "cukor"]

nakupny_kosik = ["cukor", "mlieko", "cokolada", "jablko", "jogurt", "chlieb", "banan", "hruska", "marhula", "slivka", "mrkva", "petrzlen", "celer", "zemiak"]

for polozka in nakupny_kosik: 
 if polozka in ovocie:
    print(f"{polozka} je ovocie")
 elif polozka in zelenina:
    print(f"{polozka} je zelenina")
 else:
    print(f"{polozka} je nieco ine")
