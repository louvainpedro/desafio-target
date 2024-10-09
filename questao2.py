'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a
sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

'''

def pertenceFibonacci(n):
    if n < 0:
        return False # fibonacci n tem num. negativos

    a = 0 # param 1
    b = 1 # param 2

    while b < n:
        temp = b
        b = a + b
        a = temp

    return n == b #retorna true ou false dependendo do input do user

# realizei o teste do codigo via terminal chamando o comando 'python', para passar os inputs.
aux = int(input("Olá! Digite um número INTEIRO para saber se este pertence à sequência de Fibonacci: "))
result = pertenceFibonacci(aux) # atribuo o retorno da funcao direto na variavel

if result: # reposta
    print(f"O número {aux} pertence à sequência de Fibonacci!")
else:
    print(f"O número {aux} não pertence à sequência de Fibonacci!")
