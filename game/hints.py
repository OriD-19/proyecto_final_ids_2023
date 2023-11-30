from game.testing import test_function


def match_word(word_guess, word):
    """
    Receives a formatted string of the word that the user has guessed so far.
        This means, a string with placeholders returned by "format_guessed_word".
    Also receives a single word, included in the "words" file.

    Returns a boolean value if the given word with placeholders is a possible
        match for the given word or not.
    """

    if len(word_guess) != len(word):
        return False

    for idx in range(len(word_guess)):
        if word_guess[idx] != word[idx] and word_guess[idx] != "_":
            return False

        if word_guess[idx] == "_" and word[idx] in word_guess:
            return False

    return True


def get_possible_matches(formatted_word_guess, word_list):
    """
    Recieves a formatted string, just as the "match_word" function
        (string with placeholders for non-guessed letters).
    And a list of words, which are those from the "words.txt" input file.

    Returns a list of all possible word matches that a current guess could have.
    """
    # make processing a bit easier by removing whitespace
    f = formatted_word_guess.replace("_ ", "_")

    return [word for word in word_list if match_word(f, word)]


if __name__ == "__main__":
    # Testing the functions

    c = 0

    c += test_function(
        get_possible_matches,
        ["caso"],
        "cas_ ",
        ["casa", "caso", "cama", "carro", "copa"],
    )

    c += test_function(
        get_possible_matches,
        ["lata", "rata", "masa"],
        "_ a_ a",
        ["gato", "lata", "rata", "perro", "vendedor", "colcha", "raro", "masa"],
    )
