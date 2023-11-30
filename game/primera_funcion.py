palabra_secreta = "apple"
letras_adivinadas = []
print(letras_adivinadas)

def ha_adivinado_palabra(palabra_secreta, letras_adivinadas):
    letra = input("Adivine una letra: ")
    #letras_adivinadas.append(letra)
    #print(letras_adivinadas)

    if letra in palabra_secreta:
        print("Letra correcta")
    else:
        print("Letra incorrecta")
ha_adivinado_palabra(palabra_secreta, letras_adivinadas)
