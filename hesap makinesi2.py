print("""

Taschenrechner

DRÜCKEN SIE 1, UM EINE SAMMLUNG ZU ERSTELLEN.
DRÜCKEN SIE 2, UM ENTFERNEN AUSZUFÜHREN.
DRÜCKE 3, UM EINE MULTIPLIKATION DURCHZUFÜHREN.
DRÜCKEN SIE 4, UM EINEN SPLIT ZU MACHEN.

""")

prozess = str(input("aktion auswählen: "))

if prozess == "1":
    nummer1 = int(input("nummer1 eingeben: "))
    nummer2 = int(input("nummer2 eingeben: "))
    print("Fazit:", nummer1 + nummer2)
elif prozess == "2":
    nummer1 = int(input("nummer1 eingeben: "))
    nummer2 = int(input("nummer2 eingeben: "))
    print("Fazit:", nummer1 - nummer2)
elif prozess == "3":
    nummer1 = int(input("nummer1 eingeben: "))
    nummer2 = int(input("nummer2 eingeben: "))
    print("Fazit:", nummer1 * nummer2)
elif prozess == "4":
    nummer1 = int(input("nummer1 eingeben: "))
    nummer2 = int(input("nummer2 eingeben: "))
    print("Fazit:", nummer1/nummer2)
else:
    print("Sie haben eine ungültige Transaktion eingegeben...")
