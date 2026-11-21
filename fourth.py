def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.

    :param figurka: Slovník s klíči 'typ' a 'pozice' (např. {"typ": "král", "pozice": (4, 4)})
    :param cilova_pozice: N-tice (řádek, sloupec)
    :param obsazene_pozice: Množina obsazených pozic
    :return: True, pokud je tah možný, jinak False
    """
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]

    cilovy_radek = cilova_pozice[0]
    cilovy_sloupec = cilova_pozice[1]

    # 1. KROK: Je cílová pozice na šachovnici? (řádky i sloupce 1 až 8)
    if cilovy_radek < 1 or cilovy_radek > 8:
        return False
    if cilovy_sloupec < 1 or cilovy_sloupec > 8:
        return False

    # 2. KROK: Je cílová pozice volná?
    if cilova_pozice in obsazene_pozice:
        return False

    # 3. KROK: Pohyb podle typu figury
    rozdil_radku = abs(cilovy_radek - aktualni_pozice[0])
    rozdil_sloupcu = abs(cilovy_sloupec - aktualni_pozice[1])

    if typ == "král":
        # Král se pohne o 1 pole v jakémkoliv směru (stát na místě není tah).
        if rozdil_radku == 0 and rozdil_sloupcu == 0:
            return False
        return rozdil_radku <= 1 and rozdil_sloupcu <= 1

    elif typ == "jezdec":
        # Jezdec se pohybuje ve tvaru L: 2 pole jedním směrem a 1 pole kolmo.
        if rozdil_radku == 2 and rozdil_sloupcu == 1:
            return True
        if rozdil_radku == 1 and rozdil_sloupcu == 2:
            return True
        return False

    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))  # True (o 1 pole dolů)
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))  # False (příliš daleko - o 2 pole)
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))  # False (mimo šachovnici)

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # True (tvar L: 2 nahoru, 1 doprava)
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))  # False (neni tvar L)
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice)) # False (mimo šachovnici)
