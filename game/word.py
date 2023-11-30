from string import ascii_lowercase
from game.testing import test_function



def format_guessed_word(secret_word, letter_list):
    """
    Assumes secret_word is a lowercase string.
    letter_list is a list of characters, previously validated.

    Returns a string that corresponds with the guessed letters of
        the secret word. It leaves placeholders for the rest of the
        letters that have not been guessed.
    """
    output = ""
    for letter in secret_word:
        if letter in letter_list:
            output += letter
        else:
            output += "_ "
    return output


def get_remaining_letters(letter_list):

    """
    Assumes letter_list is a list of characters previously validated.

    Returns a string with all the characters in the alphabet that have not
         been used for a guess by the user.
    """

    extra = "ñáéíóú"
    return "".join(
        [letter for letter in ascii_lowercase + extra if letter not in letter_list]
    )


if __name__ == "__main__":
    # Testing the functions
    c = 0

    # Test format_guessed_word
    c += test_function(format_guessed_word, "cac_ _ _ la", "cacerola", ["c", "l", "a"])
    c += test_function(format_guessed_word, "i_ _ i_ i_ _ _ ", "invisible", ["i"])
    c += test_function(format_guessed_word, "_ _ _ _ _ _ _ ", "materno", [])

    print(get_remaining_letters(["a", "b", "c"]))

    if c == 0:
        print("All test cases have been succesful!!!")
    else:
        print(c, "test cases have failed :(")
