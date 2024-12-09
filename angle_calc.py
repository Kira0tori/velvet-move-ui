import numpy as np


def calculate_signed_angle_between_vectors(start1, end1, start2, end2):
    start1 = np.array(start1)
    end1 = np.array(end1)
    start2 = np.array(start2)
    end2 = np.array(end2)

    # Calcul des vecteurs
    vector1 = end1 - start1
    vector2 = end2 - start2

    # Produit scalaire
    dot_product = np.dot(vector1, vector2)

    # Magnitudes des vecteurs
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)

    # Produit vectoriel
    cross_product = np.cross(vector1, vector2)

    # Calcul de l'angle non signé
    cos_angle = dot_product / (magnitude1 * magnitude2)
    cos_angle = np.clip(cos_angle, -1.0, 1.0)
    angle_rad = np.arccos(cos_angle)

    # Utilisation du produit vectoriel pour déterminer le signe de l'angle
    sign = np.sign(cross_product[2])  # Utilisation de la composante z du produit vectoriel pour déterminer le signe
    signed_angle_rad = angle_rad * sign

    # Conversion en degrés
    signed_angle_deg = np.degrees(signed_angle_rad)

    return signed_angle_deg
