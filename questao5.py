# 5) Escreva um programa que inverta os caracteres de uma string.

# recebo input dentro da variavel
string_input = input("Digite uma frase ou palavra de seu desejo para que seja revertida: ")

# funcao para reverter string
def reverteString(string):
    palavra_reversa = ""

    for letra in string:
        palavra_reversa = letra + palavra_reversa

    return palavra_reversa

# guardo retorno da func numa var
result = reverteString(string_input)

# resposta
print("\nPalavra revertida: " + result)
