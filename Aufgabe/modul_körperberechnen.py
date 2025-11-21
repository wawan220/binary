"""
erstelle eine funktion zur berechnung fon fläche und volumen
"""

def flaeche_berechen(laenge:float,breite:float):
    flaeche=laenge*breite
    return flaeche

def volumen_berechnen(laenge:float,breite:float,hoehe:float):
    volumen=flaeche_berechen(laenge,breite)*hoehe
    return volumen
