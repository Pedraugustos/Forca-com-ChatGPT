# funcoes que fazem o jogo rodar
import os

palavra_forca = ['pensamento'] # substituir depois por uma do ChatGPT

NUM_MAX_ERRO = 5 # Número máximo de tentativas

def escolha_palavra(): # Escolher uma palavra da lista de palavras
    return palavra_forca[0]

palavra = escolha_palavra()
caracteres_usados = []
num_erro = 0

def mostre_palavra_terminal(palavra, caracteres_usados): # Como a palavra aparecerá no terminal "---...-"
    palavra_ao_usuario = ''
    for letra in palavra:
        if letra in caracteres_usados:
            palavra_ao_usuario += letra
        else:
            palavra_ao_usuario += '-'
    print(f'Palavra: {palavra_ao_usuario}')

def mostre_quantidade_de_erros(NUM_MAX_ERRO, num_erro):
    print(f'Número de erros restantes: {NUM_MAX_ERRO - num_erro}')

def mostre_estado_atual(palavra, caracteres_usados, num_erro, NUM_MAX_ERRO): # Estado atual
        os.system('cls')
        mostre_palavra_terminal(palavra, caracteres_usados)
        print(f'Letras já utilizadas: {caracteres_usados}')
        mostre_quantidade_de_erros(NUM_MAX_ERRO, num_erro)

def mensagem_de_vitoria():
    print()
    print('Você ganhou!')
    print(f'A palavra era: {palavra}')
    print()
