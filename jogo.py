# funcoes que fazem o jogo rodar

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

def mostre_quantidade_de_erros(num_tent_rest):
    print(f'Número de erros restantes: {num_tent_rest}')