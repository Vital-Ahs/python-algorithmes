note = float(input("Entrer la note : "))
if note>=16:
    print("Excellent")
elif note>=14:
    print("Bien")
elif note>=10:
    print("Passable")
else:
    print("Insuffisant")

heure = int(input("Entrer l'heure actuelle : "))
if heure < 6:
    print("Bonne nuit")
elif heure < 12:
    print("Bonjour")
elif heure < 18:
    print("Bon après-midi")
else:
    print("Bonsoir")

