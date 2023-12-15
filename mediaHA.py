
# # Aufgabe 1: Vererbung von Klassen 
# # Angenommen, du entwickelst eine Software für eine Bibliothek, die verschiedene Medientypen verwalten kann, darunter Bücher, 
# Filme und Musik. Du möchtest Klassen für jede dieser Medienarten erstellen und dabei die Gemeinsamkeiten und Unterschiede 
# zwischen ihnen nutzen.

# # 1.1 Erstelle eine Basisklasse Medium, die die gemeinsamen Eigenschaften wie Titel und Jahr enthält. 
# # Dann erstelle Unterklassen für Buch, Film und Musik, die spezifische Eigenschaften wie Autor, Regisseur oder Künstler hinzufügen.
# # 1.2 Erstelle eine Methode in der Klasse Medium anzeigen(), 
# # welche folglich von allen weiteren vererbten Klassen aufgerufen werden kann
# # 1.3 Erstelle zu den Unterklassen eine spezifische Methode, die nur von Objekten dieser Klasse aufgerufen werden kann

class Medium:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def anzeigen(self):
        print(f"Titel: {self.title}, Jahr: {self.year}")


class Buch(Medium):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def anzeigen(self):
        super().anzeigen()
        print(f"Autor: {self.author}")

    def spezifische_methode(self):
        print("Diese Methode ist spezifisch für die Buch-Klasse.")


class Film(Medium):
    def __init__(self, title, year, director):
        super().__init__(title, year)
        self.director = director

    def anzeigen(self):
        super().anzeigen()
        print(f"Regisseur: {self.director}")

    def spezifische_methode(self):
        print("Diese Methode ist spezifisch für die Film-Klasse.")


class Musik(Medium):
    def __init__(self, title, year, artist):
        super().__init__(title, year)
        self.artist = artist

    def anzeigen(self):
        super().anzeigen()
        print(f"Künstler: {self.artist}")

    def spezifische_methode(self):
        print("Diese Methode ist spezifisch für die Musik-Klasse.")

medium1 = Medium("Star Wars", 2000)
buch1 = Buch("Atomic Habits", 2020, "James Clear")

buch1.anzeigen()
buch1.spezifische_methode()

medium1.anzeigen()