import os
import subprocess
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

print("=== BIT.TRIP RUNNER2 - RESTORE ANGLAIS ===")
print()

jeu = filedialog.askdirectory(
    title="Choisis le dossier du jeu"
)

if not jeu:
    exit()

original = filedialog.askdirectory(
    title="Choisis le dossier ORIGINAL anglais"
)

if not original:
    exit()

nombre = 0

for dossier, sous_dossiers, fichiers in os.walk(original):

    for fichier in fichiers:

        source = os.path.join(
            dossier,
            fichier
        )

        chemin = os.path.relpath(
            source,
            original
        )

        destination = os.path.join(
            jeu,
            chemin
        )

        if not os.path.exists(destination):
            continue

        temporaire = destination + ".temp"

        resultat = subprocess.run([
            "cmd",
            "/c",
            "copy",
            "/y",
            source,
            temporaire
        ])

        if resultat.returncode == 0:
            os.replace(
                temporaire,
                destination
            )

            print("Restauré :", chemin)
            nombre += 1

        else:
            if os.path.exists(temporaire):
                os.remove(temporaire)

            print("Erreur :", chemin)

print()
print("Restauration terminée !")
print("Fichiers restaurés :", nombre)

input("Appuie sur Entrée pour quitter...")