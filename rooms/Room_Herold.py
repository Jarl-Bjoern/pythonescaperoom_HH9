from EscapeRoom import EscapeRoom
from os import walk
from os.path import dirname, join, realpath
from requests import get

class Room_Herold(EscapeRoom):
    def __init__(self):
        super().__init__()
        self.set_metadata("Rainer Herold", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())
        self.add_level(self.create_level3())

    ### LEVELS ###
    def create_level1(self):
        URL = "http://localhost:5000/index.html"

        task_messages = ["Du wachst in einem Raum auf und siehst einen Laptop, welcher einen Akkustand von 45% hat."
            "Du setzt dich auf den Stuhl und schaust auf den Display.",
            "Auf dem Display steht, dass du 5 Minuten Zeit hast, aus der vorgegebenen URL den HTTP-Header 'server' herauszufiltern",
            f"{URL}",
            "Schreibe eine Methode <code>run(URL)</code>, um den Header zu ermitteln."]
        hints = ["Es gibt verschiedene Module, um Webrequests zu prüfen.",
                 "Verwende pip oder pip3 install requests, sofern das Package noch fehlt.",
                 "Nutze Google, um nach einer Anleitung zu suchen."]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.Header_Request, "data": URL}

    def create_level2(self):
        Text = "H134E23589L34563L23333222244L23335555112334O"

        task_messages = ["Nach der korrekten Eingabe des Codes hoerst du einen alarmieren Ton, auf dem Display erscheint eine neue Nachricht.",
                        "Du hast maximal 5 Minuten Zeit, einen Sortieralgorithmus zu folgendem String über eine Methode run(Text) zu generieren!",
                        f"String: {Text}",
                        "Sortiere alle Großbuchstaben heraus und bilde daraus ein neues Array nach folgendem Schema",
                        "1 - A","2 - B","3 - C"]
        hints = ["Probiere es mit einer Hilfsvariable.",
                "Versuche eine Schleife mit der Länge des Wortes zu generieren."]
        
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.Sort_Chars_In_Text, "data": Text}

    def create_level3(self):
        Work_Path, Script_Path = "rooms/Level_3", dirname(realpath(__file__))
        Directory = join(Script_Path, Work_Path)

        task_messages = ["Du hast den zweiten Teil bestanden. Nun bemerkst du, dass auf dem Display ein neuer Dialog erscheint."
            "Auf dem Display steht, dass du nun 10 Minuten Zeit hast, ein Passwort anhand der vorliegenden Dateien zu generieren",
            "Hinter einem an der Wand aufgehängten Bild siehst du nun ein Eingabepanel für einen 8-stelligen Code.",
            "Schreibe eine Methode <code>run(Directory)</code>, die alle Dateien überprüft und anschließend ein Passwort formt."]
        hints = ["Das Passwort besteht nur aus Groß- und Kleinbuchstaben.",
            "Probiere es mit dem Modul os.",
            "Schaue dir die Funktion join an."]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.List_Files_Build_Pass, "data": Directory}

    ### SOLUTIONS ###
    # Level 1
    def Header_Request(self, URL):
        r = get(f'{URL}')
        return r.headers['server']

    # Level 2
    def Sort_Chars_In_Text(self, Text):
        Word = ""
        Temp_Array = []

        for Text_Char in Text:
            if (Text_Char.isupper()): Word += Text_Char
        for View in range(0, len(Word)):
            if (f'{View+1} - {Word[View]}' not in Temp_Array):
                Temp_Array.append(f'{View+1} - {Word[View]}')

        return Temp_Array

    # Level 3
    def List_Files_Build_Pass(self, Directory):
        Word = ""
        for root, _, files in walk(Directory, topdown=False):
            for file in files:
                with open(join(root, file), 'r') as f:
                    for line in f.read().splitlines():
                        for line_char in line:
                            if (line_char.isupper()): Word += line_char
                            elif (line_char.islower()): Word += line_char
        return Word
