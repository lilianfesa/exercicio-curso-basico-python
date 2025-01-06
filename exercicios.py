#Exercicios - Funções

#1. Faça um programa, com uma função que necessite de três
#argumentos, e que forneça a soma desses três argumentos.

# Função que recebe três argumentos e retorna a soma
def somar_tres_argumentos(a, b, c):
    return a + b + c

# Testando a função
resultado = somar_tres_argumentos(5, 3, 2)
print("A soma dos três argumentos é:", resultado)

#2. Reverso do número. Faça uma função que retorne o reverso de um
#número inteiro informado. Por exemplo: 127 -> 721.

# Função que retorna o reverso de um número
def reverso_numero(numero):
    # Converte o número para string, inverte e converte novamente para inteiro
    return int(str(numero)[::-1])

# Testando a função
numero = 127
resultado = reverso_numero(numero)
print(f"O reverso do número {numero} é {resultado}")


# Função que retorna o reverso de um número
def reverso_numero(numero):
    # Converte o número para string, inverte e converte novamente para inteiro
    return int(str(numero)[::-1])

# Solicita ao usuário que digite um número
numero = int(input("Digite um número inteiro: "))

# Chama a função e armazena o resultado
resultado = reverso_numero(numero)

# Exibe o resultado
print(f"O reverso do número {numero} é {resultado}")



#3. Escreva um script que pergunta ao usuário se ele deseja converter
#uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
#cada opção, crie uma função.
#Plus: Crie uma terceira, que é um menu para o usuário escolher a opção
#desejada, onde esse menu chama a função de conversão correta.

# Função para converter de Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Função para converter de Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função principal que pede a escolha do usuário
def conversao_temperatura():
    print("Escolha uma opção de conversão:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    
    # Solicita ao usuário que escolha a opção
    escolha = input("Digite 1 ou 2: ")
    
    if escolha == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit}°F.")
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {celsius}°C.")
    else:
        print("Opção inválida! Por favor, escolha 1 ou 2.")

# Executa a função de conversão
conversao_temperatura()



#4. Crie um programa que leia quanto dinheiro uma pessoa tem na
#carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
#Considere a tabela de conversão abaixo:
#Dólar Americano: R$ 4,91
#Peso Argentino: R$ 0,02
#Dólar Australiano: R$ 3,18
#Dólar Canadense: R$ 3,64
#Franco Suiço: R$ 0,42
#Euro: R$ 5,36
#Libra esterlina: R$ 6,21


# Função para realizar a conversão de reais para as moedas estrangeiras
def converter_dinheiro(valor_em_reais):
    # Tabelas de conversão
    conversao = {
        "Dólar Americano (USD)": 4.91,
        "Peso Argentino (ARS)": 0.02,
        "Dólar Australiano (AUD)": 3.18,
        "Dólar Canadense (CAD)": 3.64,
        "Franco Suíço (CHF)": 0.42,
        "Euro (EUR)": 5.36,
        "Libra Esterlina (GBP)": 6.21
    }

    # Exibe a quantidade de cada moeda que o valor em reais pode comprar
    for moeda, taxa in conversao.items():
        quantidade = valor_em_reais / taxa
        print(f"Com R$ {valor_em_reais:.2f}, você pode comprar {quantidade:.2f} {moeda}.")

# Solicita o valor que a pessoa tem na carteira
valor = float(input("Quanto dinheiro você tem na carteira? R$ "))

# Chama a função de conversão
converter_dinheiro(valor)


#5. Crie uma função chamada contar_vogais que recebe uma string
#como parâmetro. Implemente a lógica para contar o número de vogais
#na string e retorne o total de vogais. Solicite ao usuário para inserir uma
#frase e utilize a função para contar as vogais

# Função para contar o número de vogais na string
def contar_vogais(frase):
    # Definir as vogais
    vogais = "aeiouAEIOU"
    # Contar as vogais na frase
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador

# Solicita ao usuário para inserir uma frase
frase_usuario = input("Digite uma frase: ")

# Chama a função contar_vogais e exibe o resultado
resultado = contar_vogais(frase_usuario)
print(f"A frase inserida tem {resultado} vogais.")


#6. Vamos construir um jogo de forca. O programa escolherá
#aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
#secreta será representada por espaços em branco, um para cada letra
#da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
#tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
#na palavra secreta, ela será revelada nas posições correspondentes. Se
#a letra não estiver na palavra, uma mensagem de erro deverá ser
#informada. Após um número máximo de erros, o jogador perde. O jogo
#continua até que o jogador adivinhe a palavra ou exceda o número
#máximo de tentativas. 
#Dica: Você precisará importar uma biblioteca para resolver esse exercício

import random

# Lista de palavras predefinidas
palavras = ['python', 'java', 'javascript', 'ruby', 'forca', 'programacao', 'desenvolvimento']

# Função para jogar o jogo de forca
def jogar_forca():
    # Escolhe uma palavra aleatoriamente
    palavra_secreta = random.choice(palavras)
    
    # Cria uma lista com espaços em branco para as letras da palavra secreta
    letras_descobertas = ['_'] * len(palavra_secreta)
    
    tentativas = 6  # Número de tentativas
    letras_erradas = []  # Armazena as letras erradas

    # Jogo continua enquanto houver tentativas e a palavra não for adivinhada
    while tentativas > 0 and ''.join(letras_descobertas) != palavra_secreta:
        print('\nPalavra secreta: ' + ' '.join(letras_descobertas))
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        
        # O jogador insere uma letra
        tentativa = input("Digite uma letra: ").lower()
        
        # Verifica se a entrada é válida (uma única letra)
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue
        
        # Verifica se a letra já foi tentada
        if tentativa in letras_descobertas or tentativa in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        # Verifica se a letra está na palavra secreta
        if tentativa in palavra_secreta:
            # Revela a letra nas posições corretas
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == tentativa:
                    letras_descobertas[i] = tentativa
            print("Boa! Letra correta.")
        else:
            # Se a letra não estiver na palavra, decrementa as tentativas e armazena a letra errada
            tentativas -= 1
            letras_erradas.append(tentativa)
            print("Errou! A letra não está na palavra.")
    
    # Verifica se o jogador ganhou ou perdeu
    if ''.join(letras_descobertas) == palavra_secreta:
        print("\nParabéns! Você adivinhou a palavra secreta:", palavra_secreta)
    else:
        print("\nVocê perdeu! A palavra secreta era:", palavra_secreta)

# Chama a função para iniciar o jogo
jogar_forca()
