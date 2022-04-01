import os
import random
import palabras
import diagramas


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def quietar_tilde(palabra):
    '''Retorna: palabra sin tilde en el caso de que contenga.'''
    if 'Á' in palabra:
        return palabra.replace('Á', 'A')
    elif 'É' in palabra:
        return palabra.replace('É', 'E')
    elif 'Í' in palabra:
        return palabra.replace('Í', 'I')
    elif 'Ó' in palabra:
        return palabra.replace('Ó', 'O')
    elif 'Ú' in palabra:
        return palabra.replace('Ú', 'U')
    else:
        return palabra


def comprobar_letra(letra, letras_ingresadas):
    '''Retorna: True si la letra ingresada es válida.'''
    if not letra.isalpha():
        print('ERROR: has ingresado un carácter incorrecto.\n')
    elif len(letra) > 1:
        print('ERROR: has ingresado más de una letra.\n')
    elif letra.upper() in letras_ingresadas:
        print(f'ERROR: ya has ingresado la letra {letra.upper()}.\n')
    else:
        return True


def jugar():
    # Definición de variables
    palabra_original = random.choice(palabras.palabras)
    palabra_adivinar = quietar_tilde(palabra_original)
    letras_adivinar = set(palabra_adivinar)
    letras_ingresadas = []
    vidas = 6

    # Bucle de juego
    while vidas > 0 and len(letras_adivinar) > 0:
        print(' '.join([letra if letra in letras_ingresadas else '_' for letra in palabra_adivinar]))
        print(diagramas.diagramas[vidas])
        print('Letras ingresadas:', "-".join(letras_ingresadas))
        letra_usuario = input('\nIngrese una letra: ')

        clearConsole()

        if comprobar_letra(letra_usuario, letras_ingresadas) == True:
            letras_ingresadas.append(letra_usuario.upper())
            if letra_usuario.upper() in letras_adivinar:
                letras_adivinar.remove(letra_usuario.upper())
            else:
                vidas -=1

    # Fin del juego
    if vidas == 0:
        print(diagramas.diagramas[vidas])
        print(f'¡Ahorcado! La palabra era: {palabra_original}.\n')
    else:
        print(f'¡Ganaste! La palabra era: {palabra_original}.\n')


# Inicio
print('''
              +-------------------------------------------------+
              |                   AHORCADO                      |
              |             Versión: Informática                |
              +-------------------------------------------------+

                                INSTRUCCIONES
La computadora seleccionará de forma aleatoria una palabra utilizada en informática
y tu tarea será adivinarla. Cuentas con 6 intentos errados antes de terminar AHORCADO.
''')
ENTER = input('Pulse ENTER para comenzar.')

while True:
    clearConsole()
    jugar()

    # Bucle para comprobar que el usuario ingrese 's, n, S o N.
    while True:
        seguir_jugando = input('¿Quiere jugar de nuevo? [S/N] ')
        clearConsole()
        if not seguir_jugando.isalpha():
            print('ERROR: has ingresado un carácter incorrecto.\n')
        elif seguir_jugando.upper() == 'S' or seguir_jugando.upper() == 'N':
            seguir_jugando = seguir_jugando.upper()
            break
        else:
            print('ERROR: has ingresado una letra incorrecta.\n')

    if seguir_jugando == 'N': break