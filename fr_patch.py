import os
import subprocess
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

print("=== BIT.TRIP RUNNER2 - PATCH FRANÇAIS ===")
print()

jeu = filedialog.askdirectory(
    title="Choisis le dossier du jeu ORIGINAL"
)

if not jeu:
    exit()

dossier = os.path.dirname(os.path.abspath(__file__))
patchs = os.path.join(dossier, "patch")
xdelta = os.path.join(dossier, "xdelta3.exe")

if not os.path.exists(xdelta):
    print("xdelta3.exe introuvable !")
    input("Appuie sur Entrée pour quitter...")
    exit()

if not os.path.exists(patchs):
    print("Dossier patchs introuvable !")
    input("Appuie sur Entrée pour quitter...")
    exit()

nombre = 0

for dossier_patch, sous_dossiers, fichiers in os.walk(patchs):

    for fichier in fichiers:

        if not fichier.endswith(".xdelta"):
            continue

        patch = os.path.join(
            dossier_patch,
            fichier
        )

        chemin = os.path.relpath(
            patch,
            patchs
        )

        chemin = chemin[:-7]

        original = os.path.join(
            jeu,
            chemin
        )

        if not os.path.exists(original):
            print("Fichier introuvable :", chemin)
            continue

        temporaire = original + ".temp"

        resultat = subprocess.run([
            xdelta,
            "-d",
            "-s",
            original,
            patch,
            temporaire
        ])

        if resultat.returncode == 0:
            os.replace(
                temporaire,
                original
            )

            print("Patché :", chemin)
            nombre += 1

        else:
            if os.path.exists(temporaire):
                os.remove(temporaire)

            print("Erreur :", chemin)

print()
print("Patch terminé !")
print("Fichiers patchés :", nombre)

input("Appuie sur Entrée pour quitter...")