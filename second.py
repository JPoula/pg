CISLA_0_AZ_9 = ["nula", "jedna", "dva", "tři", "čtyři",
                "pět", "šest", "sedm", "osm", "devět"]
CISLA_10_AZ_19 = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct",
                  "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
CELE_DESITKY = ["", "", "dvacet", "třicet", "čtyřicet",
                "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]


def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    cele_cislo = int(cislo)

    if cele_cislo < 0 or cele_cislo > 100:
        return "Číslo musí být od 0 do 100"
    if cele_cislo == 100:
        return "sto"
    if cele_cislo < 10:
        return CISLA_0_AZ_9[cele_cislo]
    if cele_cislo < 20:
        return CISLA_10_AZ_19[cele_cislo - 10]

    desitky = cele_cislo // 10
    jednotky = cele_cislo % 10
    if jednotky == 0:
        return CELE_DESITKY[desitky]
    return f"{CELE_DESITKY[desitky]} {CISLA_0_AZ_9[jednotky]}"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
