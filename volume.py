import math
import sys
import csv


def calculer_volume_sphere(rayon):
    volume = (4 / 3) * math.pi * rayon**3
    return volume


if len(sys.argv) >= 2:
    rayon_sphere = int(sys.argv[1])
    volume_sphere = calculer_volume_sphere(rayon_sphere)
    with open("resultats_spheres.csv", mode="w", newline="") as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerow(["Rayon", "Volume"])
        writer.writerow([rayon_sphere, volume_sphere])
