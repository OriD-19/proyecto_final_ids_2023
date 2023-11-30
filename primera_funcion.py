palabra_secreta = "apple"
letras_adivinadas = []
print(f"Letras adivinadas: {letras_adivinadas}")

def ha_adivinado_palabra(palabra_secreta, letras_adivinadas):
    while set(palabra_secreta) - set(letras_adivinadas):
        letra = input("Adivine una letra: ")
        letras_adivinadas.append(letra)
        print(f"Letras adivinadas: {letras_adivinadas}")

        if letra in palabra_secreta:
            print("Letra correcta")
        else:
            print("Letra incorrecta")
    print(f"Felicidades. Has adivinado la palabra: {palabra_secreta}")
ha_adivinado_palabra(palabra_secreta, letras_adivinadas)
