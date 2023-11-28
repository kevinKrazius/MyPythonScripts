woerterbuch = {
    "cat": "Katze",
    "bird": "Vogel",
    "car": "Auto",
    "speed": "Geschwindigkeit",
    "fly": "Fliege",
    "sky": "Himmel",
    "kid": "Kind",
    "dog": "Hund",
    "rat": "Ratte",
    "ich": "i"
}

def uebersetze(wort):
    if wort in woerterbuch:
        return woerterbuch[wort]
    else:
        return "Wort ist nicht im Wörterbuch!"
    
eingabe = input("Gib einen englischen Begriff ein, den du übersetzen möchtest: ")

uebersetzung = uebersetze(eingabe)
print(uebersetzung)