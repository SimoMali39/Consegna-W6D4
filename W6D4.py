import math

def calcola_perimetro_quadrato(lato):
    return 4 * lato

def calcola_perimetro_cerchio(raggio):
    return 2 * math.pi * raggio

def calcola_perimetro_rettangolo(base, altezza):
    return 2 * (base + altezza)

scelta = input("Scegli la figura geometrica per cui vuoi calcolare il perimetro (quadrato, cerchio, rettangolo): ").lower()

if scelta == "quadrato":
    lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
    perimetro = calcola_perimetro_quadrato(lato)
    print(f"Il perimetro del quadrato di lato {lato} è {perimetro}")
elif scelta == "cerchio":
    raggio = float(input("Inserisci il raggio del cerchio: "))
    perimetro = calcola_perimetro_cerchio(raggio)
    print(f"La circonferenza del cerchio di raggio {raggio} è {perimetro}")
elif scelta == "rettangolo":
    base = float(input("Inserisci la lunghezza della base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    perimetro = calcola_perimetro_rettangolo(base, altezza)
    print(f"Il perimetro del rettangolo di base {base} e altezza {altezza} è {perimetro}")
else:
    print("Scelta non valida. Riprova.")