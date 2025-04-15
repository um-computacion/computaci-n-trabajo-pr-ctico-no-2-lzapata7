def is_palindrome(value):
    word = value.lower()
    texto_limpio = ""
    for caracter in word:
        if caracter.isalnum():
            texto_limpio += caracter
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ü': 'u', 'ñ': 'n'
    }
    
    for letra_con_tilde, letra_sin_tilde in reemplazos.items():
        texto_limpio = texto_limpio.replace(letra_con_tilde, letra_sin_tilde)

    if texto_limpio ==  texto_limpio[::-1]:
        return True
    else:
        return False

entrada = input("Ingrese una palabra o frase: ")
if is_palindrome(entrada):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")