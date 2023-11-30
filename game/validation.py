import string
from game.testing import test_function

def word_guessed(secret_word, letter_list):
    """
    Receives two parameters:
        secret_word, which is the word that the user has to guess.
            Since it comes from the "words" file, it is in lowercase.
            Encoded un utf-8 (spanish).
        letter_list, which is the list of letters that the user 
            has guessed so far.
            This list must not contain duplicates, since the game
            does not allow duplicate letters to be guessed.
        

    Returns a boolean: if the user has found the word.
    """

    # Delete duplicate letters from the secret word
    secret_letters = list(dict.fromkeys(secret_word))

    # Compare lists with exact values (therefore, sort them before)
    return sorted(secret_letters) == sorted(letter_list)

def validate_user_letter(user_input):
    """
    Receives a input from the user.

    Returns the same input formatted correctly (lowercase letter).
    Otherwise, an empty string if the input is not valid.
    """

    extra_letters = string.ascii_letters + "ñÑáóúíé"
    # print (string.ascii_letters)

    if len(user_input) == 1 and user_input in extra_letters:
        return user_input.lower()

    # DESCOMENTAR LA SIGUIENTE LINEA PARA MAS SALSA 👹
    # print("No sea pasmado e introduzca un solo dato del alfabeto ascii")

    return ""

if __name__ == '__main__':
    # Just for testing purposes

    c = 0
    # Testing word_guessed
    c += test_function(word_guessed, True, "bañera", ['b', 'ñ', 'r', 'a', 'e'])
    c += test_function(word_guessed, False, "camión", ['c', 'a'])
    c += test_function(word_guessed, True, "solo", ['s', 'o', 'l'])

    # Testing validate_user_letter
    c += test_function(validate_user_letter, 'a', 'A')
    c += test_function(validate_user_letter, 'ñ', 'ñ')
    c += test_function(validate_user_letter, 'ñ', 'Ñ')
    c += test_function(validate_user_letter, '', '.')
    c += test_function(validate_user_letter, '', ':   ')

    if c == 0:
        print("All test cases have been succesful!!!")
    else:
        print(c, "test cases have failed :(")
