# -*- coding: utf-8 -*-
from game import word, hints, validation
from sys import argv


def load_words(hardmode=False):
    words = []
    if not hardmode:
        # Modo facil del juego
        with open("words.txt", encoding="utf-8") as f:
            for line in f:
                dot = line.index(".")
                words.append(line[dot + 1 :].rstrip("\n").strip().lower())
    else:
        # Modo dificil
        with open("diccionario.txt", encoding="utf-8") as f:
            for line in f:
                words.append(line.strip(" \n"))

    return words


if __name__ == "__main__":
    words = []
    dificil = False

    if len(argv) > 1:
        # The user decided to play hard gamemode
        assert argv[1] == "dificil", (
            "Para jugar el modo dificil, escribe 'dificil' luego del nombre del archivo"
        )
        dificil = True

    words = load_words(hardmode=dificil)
