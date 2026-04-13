# ============================================
# Projet : Calculateur de moyenne d'étudiants
# Auteur  : Gaïus Ahs
# Date    : 2025
# ============================================

def calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes."""
    if len(notes) == 0:
        return 0
    return sum(notes) / len(notes)

def saisir_notes():
    """Demande à l'utilisateur de saisir ses notes."""
    notes = []
    print("=== Calculateur de Moyenne ===")
    nombre = int(input("Combien de notes veux-tu entrer ? "))
    
    for i in range(nombre):
        note = float(input(f"Note {i+1} : "))
        notes.append(note)
    
    return notes

def afficher_resultat(notes, moyenne):
    """Affiche le résultat final."""
    print("\n--- Résultat ---")
    print(f"Notes saisies : {notes}")
    print(f"Moyenne       : {moyenne:.2f}/20")
    
    if moyenne >= 10:
        print("Mention       : Admis ✓")
    else:
        print("Mention       : Ajourné ✗")

# --- Programme principal ---
notes = saisir_notes()
moyenne = calculer_moyenne(notes)
afficher_resultat(notes, moyenne)