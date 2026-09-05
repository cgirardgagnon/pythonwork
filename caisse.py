produit = input("Que voulez-vous acheter?\n")
prix = float(input("Quel est le prix du produit?\n"))
quantite = int(input("Combien de produit voulez-vous acheter?\n"))
membre = input("Êtes-vous membre (Oui/Non)\n")

total = quantite*prix
rabais_membreet50 = total*0.15
rabais_10 = total*0.10
total_membre = total - rabais_10
total_membre50 = total - rabais_membreet50
total_nonmembre50 = total - rabais_10

print:(f"Vous voulez acheter {quantite} {produit} au prix de {prix} $.")


if membre == "Oui" and total >= 50:
    print(f"Votre total après rabais de 15% est de {total_membre50:.2f} $.")

elif membre == "Oui" and total < 50:
    print(f"Votre total après rabais de 10% est de {total_membre:.2f} $.")

elif membre == "Non" and total >= 50:
    print(f"Votre total après rabais de 10% est de {total_nonmembre50:.2f} $.")

else:
    print(f"Votre total est de {total:.2f}")
