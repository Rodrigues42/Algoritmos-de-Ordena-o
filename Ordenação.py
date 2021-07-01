import pygame
from random import randint
from time import sleep
from pygame import display


PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)


def criarLista(quantidade):

    '''Cria um dicionario no formato: {indice: [dimensão do retangulo a ser ordenado] }'''

    lista = {}

    for i in range(quantidade):

        lista[i] = []

    return lista


def criarObjetos(lista, comprimentoTela, alturaTela):

    '''Cria os objetos dado uma lista no formato { indice: [dimensões] }'''

    largura = (comprimentoTela - len(lista)) / len(lista)
    alturaAleatoria = randint(10, (alturaTela - 10))
    posicaoX = 0
    posicaoY = 0

    for i in lista:

        lista[i] = [posicaoX, posicaoY, largura, alturaAleatoria]
        posicaoX += largura + 1
        alturaAleatoria = randint(10, alturaTela - 10)

    return lista


def desenhar(lista, janela, cor1, tempo):

    '''Desenha na tela os objetos dada uma lista'''

    janela.fill(0)
    sleep(tempo)
    pygame.display.update()

    for objeto in lista:

        posicaoX = lista[objeto][0]
        posicao_Y = lista[objeto][1]
        largura = lista[objeto][2]
        altura = lista[objeto][3]

        pygame.draw.rect(janela, cor1, pygame.Rect(posicaoX, posicao_Y, largura, altura))
    
    pygame.display.update()


def SelectionSort(lista, janela, cor1, cor2, cor3, tempo):

    for i in range(len(lista)):

        j = i + 1
        menor = lista[i][3]
        auxi = j-1

        while j < len(lista):

            if menor > lista[j][3]:

                menor = lista[j][3]
                auxi = j
            j += 1
        
        pygame.draw.rect(janela, cor2, (lista[i]))
        pygame.draw.rect(janela, cor3, (lista[auxi]))
        display.update()

        if menor != lista[i][3]:

            lista[i][3], lista[auxi][3] = menor, lista[i][3]
            desenhar(lista, janela, cor1, tempo)


def InsertionSort(lista, janela, cor1, cor2, cor3, tempo):

    for i in range(1, len(lista)):

        key = lista[i][3]
        pygame.draw.rect(janela, cor2, (lista[i]))
        display.update()
        k = i

        while k > 0 and key < lista[k-1][3]:
            lista[k][3] = lista[k-1][3]
            k -= 1

        pygame.draw.rect(janela, cor3, (lista[k]))
        display.update()
        
        desenhar(lista, janela, cor1, tempo)
        lista[k][3] = key

    print(lista)


def run(algoritmo=1, quantidade=80, compTela=800, altTela=600, cor1=AZUL, cor2=VERMELHO, cor3=VERDE, tempo=0.1):

    '''Roda o algoritmo de ordenação 
    
    1: SelectionSort
    
    '''

    comprimentoTela = compTela
    alturaTela = altTela

    pygame.init()
    janela = pygame.display.set_mode((comprimentoTela, alturaTela))

    if algoritmo == 1:
        pygame.display.set_caption('Selection Sort')
    elif algoritmo == 2:
        pygame.display.set_caption('Insertion Sort')
    else:
        pass

    lista = criarLista(quantidade)
    objetos = criarObjetos(lista, compTela, alturaTela)
    desenhar(objetos, janela, cor1, tempo)

    if algoritmo == 1:
        SelectionSort(objetos, janela, cor1, cor2, cor3, tempo)
    elif algoritmo == 2:
        InsertionSort(objetos, janela, cor1, cor2, cor3, tempo)
    else:
        print("Algoritmo não encontrado")

    # Mantem a tela até clicar em fechar
    continua = True
    while continua:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continua = False

# Versão do Pygame 2.0.1
# Para rodar o script basta chamar: run()
# 1 - Selection Sort
# 2 - Insertion Sort
# ...

run(1)
run(2)
