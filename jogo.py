# funcoes que fazem o jogo rodar
import os

palavra_forca = ['pensamento'] # substituir depois por uma do ChatGPT

def escolha_palavra(): # Escolher uma palavra da lista de palavras
    return palavra_forca[0]

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

def mensagem_de_derrota():
    print()
    print('Você perdeu!')
    print(f'A palavra era: {palavra}')
    print()

NUM_MAX_ERRO = 5
palavra = escolha_palavra()
caracteres_usados = []
num_erro = 0

while num_erro < NUM_MAX_ERRO:
    mostre_estado_atual(palavra, caracteres_usados, num_erro, NUM_MAX_ERRO)
    tent_letra=input('Selecione uma letra: ')

    if tent_letra not in palavra:
         num_erro += 1
         caracteres_usados = caracteres_usados + [tent_letra]

    if tent_letra in palavra:
        caracteres_usados = caracteres_usados + [tent_letra]
        if set(palavra).issubset(caracteres_usados):
            mostre_estado_atual(palavra, caracteres_usados, num_erro, NUM_MAX_ERRO)
            mensagem_de_vitoria()
            exit()
    
    elif num_erro == NUM_MAX_ERRO:
        mostre_estado_atual(palavra, caracteres_usados, num_erro, NUM_MAX_ERRO)
        mensagem_de_derrota()
        exit()