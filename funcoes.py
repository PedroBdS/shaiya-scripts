import pyautogui
import time
import keyboard
from PIL import ImageGrab, Image
import numpy as np

matriz_mestre = [
    (0,0,1,0,0,0,0,0),
    (0,1,0,0,0,0,0,1),
    (0,1,0,0,0,0,1,0),
    (0,0,0,0,1,1,0,0),
    (0,0,1,1,0,0,1,0),
    (0,1,1,1,1,1,1,0),
    (1,0,0,0,0,0,0,0),
    (0,1,1,0,1,1,1,0),
    (0,1,1,1,0,0,1,0)
]

def click_ingame(coordenada, delay=0):
    coordenada2 = (coordenada[0]+1, coordenada[1])

    pyautogui.moveTo(coordenada)
    pyautogui.mouseDown()
    time.sleep(delay)
    pyautogui.moveTo(coordenada)
    time.sleep(delay)
    pyautogui.moveTo(coordenada)
    time.sleep(delay)
    pyautogui.mouseUp()

def esperar_cor_e_clicar(coordenada, cor=False, delay=0, ingame=True, nome=False):

    nome = False

    pyautogui.moveTo(coordenada)
    if not ingame:
        while True:
            if not cor:
                time.sleep(delay)
                pyautogui.click(coordenada)
                break
            if ImageGrab.grab().getpixel((coordenada)) == (cor):
                time.sleep(delay)
                pyautogui.click(coordenada, duration=delay)
                break
            if nome != False:
                print(f'esperando cor {nome}')
        return

    if ingame:
        while True:
            if not cor:
                time.sleep(delay)
                click_ingame(coordenada)
                break
            if ImageGrab.grab().getpixel((coordenada)) == (cor):
                time.sleep(delay)
                click_ingame(coordenada, delay=delay)
                break
            if nome != False:
                print(f'esperando cor {nome}')
        return

def esperar_cor(coordenada, cor, nome=False):
    nome = False
    while True:
        if ImageGrab.grab().getpixel((coordenada)) == (cor):
            break
        if nome != False:
            print(f'esperando cor {nome}')

def checar_cor(coordenada, cor):
    if ImageGrab.grab().getpixel((coordenada)) == (cor):
        return True
    else:
        return False

def iniciar_shaiya(conta):
    time.sleep(0.2)

    # Pressiona a tecla Windows
    keyboard.press('windows')
    keyboard.release('windows')

    # Espera um pouco para o menu iniciar abrir
    time.sleep(0.2)

    # Digita "fawkes"
    pyautogui.write('fawkes')

    # Pressiona Enter
    pyautogui.press('enter')

    # PLAY Posição do mouse: (670, 552), Cor do pixel: (236, 56, 36)
    esperar_cor_e_clicar((670, 552),(236, 56, 36), ingame=False, nome='PLAY')

    # Connect Posição do mouse: (1841, 1021), Cor do pixel: (233, 69, 53)
    esperar_cor_e_clicar((1841, 1021), (233, 69, 53), ingame=False, nome='Connect')

    # Login Posição do mouse: (1006, 819), Cor do pixel: (22, 21, 22)
    esperar_cor_e_clicar((1006, 819), (22, 21, 22), nome='Login')
    pyautogui.write(conta)

    # Senha Posição do mouse: (996, 875), Cor do pixel: (23, 24, 27)
    esperar_cor_e_clicar((996, 875), (23, 24, 27), nome='Senha')
    pyautogui.write('Bolinho123321!')

    # Entrar Posição do mouse: (991, 965), Cor do pixel: (68, 33, 33)
    esperar_cor_e_clicar((991, 965), (68, 33, 33), nome='Entrar')

    time.sleep(0.3)

    # Por favor espere um momento antes de iniciar novamente a sessão.
    # Posição do mouse: (1023, 509), Cor do pixel: (34, 34, 37)

    if checar_cor((1023, 509), (34, 34, 37)):
        return False

    # A conexão com o servidor foi encerrada.
    # Posição do mouse: (1077, 504), Cor do pixel: (28, 24, 24)

    if checar_cor((1077, 504), (28, 24, 24)):
        return False

    # Servidor Posição do mouse: (951, 658), Cor do pixel: (24, 24, 24)
    esperar_cor_e_clicar((951, 658), (24, 24, 24), nome='Servidor')
                         
    # OK Posição do mouse: (921, 971), Cor do pixel: (63, 32, 32)
    esperar_cor_e_clicar((921, 971), (63, 32, 32), nome='OK')

    # Esperar tela personagens Posição do mouse: (803, 455), Cor do pixel: (11, 8, 5)
    esperar_cor((803, 455), (11, 8, 5), nome='Esperar tela personagens')

    # P1 Posição do mouse: (468, 255), Cor do pixel: (27, 22, 15)
    # esperar_cor_e_clicar((468, 255), nome='P1')

    # P2 Posição do mouse: (468, 378), Cor do pixel: (30, 12, 41)
    esperar_cor_e_clicar((468, 378), nome='P2')

    # P3 Posição do mouse: (468, 508), Cor do pixel: (17, 19, 26)
    # esperar_cor_e_clicar((468, 508), nome='P3')

    # P4 Posição do mouse: (468, 634), Cor do pixel: (16, 23, 21)
    # esperar_cor_e_clicar((468, 634), nome='P4')

    # P5 Posição do mouse: (468, 768), Cor do pixel: (18, 21, 28)
    # esperar_cor_e_clicar((468, 768), nome='P5')

    # Início do jogo Posição do mouse: (1385, 1024), Cor do pixel: (250, 249, 247)
    esperar_cor_e_clicar((1385, 1024), (250, 249, 247), nome='')

    # Confirmar ingame Posição do mouse: (939, 1061), Cor do pixel: (251, 239, 185)
    esperar_cor((939, 1061), (251, 239, 185), nome='')

    return True

def comparar_img(img1, img2):
    
    # Verificar se as dimensões são diferentes
    # if imagem1.size != imagem2.size:
    #     return False
    
    # Converter as imagens para arrays NumPy para comparar pixel a pixel
    img_array1 = np.array(img1)
    img_array2 = np.array(img2)
    
    # Verificar se os arrays são idênticos
    return np.array_equal(img_array1, img_array2)

def printar_coordenadas(cord1, cord2):
    # Obter as coordenadas de referência
    x1, y1 = cord1
    x2, y2 = cord2
    
    # Definir a área de captura (top, left, width, height)
    top = min(y1, y2)
    left = min(x1, x2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    
    # Capturar a área da tela
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    return screenshot

def identificar_erros():
    tela_img = printar_coordenadas((854, 461), (895, 493))

def abrir_leilao():

    # Posição do mouse: (595, 246), Cor do pixel: (73, 73, 72)
    # Posição do mouse: (597, 249), Cor do pixel: (35, 34, 36)
    # Posição do mouse: (596, 253), Cor do pixel: (24, 24, 26)

    # botao fechar Posição do mouse: (1324, 260), Cor do pixel: (86, 35, 37)

    # Abrir leilão Posição do mouse: (1422, 1036), Cor do pixel: (249, 178, 102) 


    if not(checar_cor((595, 246), (73, 73, 72)) and checar_cor((597, 249), (35, 34, 36))):
        click_ingame((1422, 1036))

    if not(checar_cor((595, 246), (73, 73, 72)) and checar_cor((597, 249), (35, 34, 36))):
        click_ingame((1422, 1036))

    if not(checar_cor((595, 246), (73, 73, 72)) and checar_cor((597, 249), (35, 34, 36))):
        click_ingame((1422, 1036))

    if not(checar_cor((595, 246), (73, 73, 72)) and checar_cor((597, 249), (35, 34, 36))):
        print('Não foi possível abrir o leilão')

def capturar_tela(coordenada1, coordenada2, arquivo_saida=False):
    # Obter as coordenadas de referência
    x1, y1 = coordenada1
    x2, y2 = coordenada2
    
    # Definir a área de captura (top, left, width, height)
    top = min(y1, y2)
    left = min(x1, x2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    
    # Capturar a área da tela
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    
    if not arquivo_saida:
        return screenshot
    
    # Salvar a captura de tela em PNG
    screenshot.save(arquivo_saida)
    

    print(f"Imagem salva como {arquivo_saida}")

def cor_do_nome():

    # segundo item do leilão
    esperar_cor_e_clicar((931, 444), ingame=True)

    imagem = capturar_tela((809, 378), (810, 387))

    cores_predefinidas = [
    (255, 255, 255),
    (255, 255, 0),
    (255, 128, 0),
    (255, 0, 255),
    (128, 255, 255),
    (128, 0, 255),
    (0, 255, 64),
    (0, 128, 255)
    ]

    pixels = list(imagem.getdata())
    
    for pixel in pixels:
        if pixel in cores_predefinidas:
            return pixel
        
    print(f'Falha ao identificar a cor do nome.')
    return (0, 0, 0)

def atualizar_leilao():
    click_ingame((1250, 312))

def formatar_nome(image, cor_rgb):

    img = image.convert('RGB')  # Garantir que a imagem está no formato RGB
    
    # Criar uma nova imagem vazia (preta e branca)
    nova_img = Image.new('L', img.size)
    pixels = nova_img.load()

    # Obter os dados da imagem original
    img_pixels = img.load()

    # Percorrer todos os pixels
    for i in range(img.size[0]):  # Largura
        for j in range(img.size[1]):  # Altura
            # Se o pixel for da cor informada, pintá-lo de branco (255), senão preto (0)
            if img_pixels[i, j] == cor_rgb:
                pixels[i, j] = 255  # Branco
            else:
                pixels[i, j] = 0    # Preto

    return nova_img

def printar_preco():
    valor = capturar_tela((1182, 398), (1287, 406))
    valor_formatado = formatar_nome(valor, (255,255,255))
    return valor_formatado

def process_matrix(matriz):
# Obter as dimensões da matriz
    linhas, colunas = matriz.shape
    
    # Inicializar uma lista para armazenar as colunas unificadas
    colunas_unificadas = []

    # Iterar sobre a matriz em blocos de 6 colunas
    for i in range(0, colunas, 6):
        # Obter o bloco atual
        bloco = matriz[:, i:i+6]
        
        # Verificar se o bloco tem pelo menos 2 colunas
        if bloco.shape[1] >= 2:
            # Extrair a primeira e a segunda coluna do bloco
            colunas_unificadas.append(bloco[:, :2])
    
    # Unificar as colunas extraídas em uma nova matriz
    matriz_unificada = np.concatenate(colunas_unificadas, axis=1)
    
    return matriz_unificada

def print_para_matriz_UNIFICADA(imagem):

    img = Image.open(imagem)
    img = img.convert('1')   
    matriz = np.array(img, dtype=int)

    # matriz1 = remover_primeiras_colunas_zeradas(matriz)
    for i in range(matriz.shape[1]):
        if np.any(matriz[:, i] == 1):
            matriz1 = matriz[:, i:]
            break

    # m_gold, matriz3 = quebrar_na_primeira_sequencia_zerada(matriz1)
    n_colunas = matriz1.shape[1]
    for i in range(n_colunas - 3):
        # Verificar se as 4 colunas consecutivas a partir da i-ésima são todas zeradas
        if np.all(matriz1[:, i] == 0) and np.all(matriz1[:, i+1] == 0) and np.all(matriz1[:, i+2] == 0) and np.all(matriz1[:, i+3] == 0):
            # Parte esquerda: até a coluna imediatamente antes da sequência zerada
            m_gold = matriz1[:, :i]
            
            # Parte direita: da coluna após a sequência zerada até o final
            matriz3 = matriz1[:, i+4:]
            
            break

    # matriz4 = remover_primeiras_colunas_zeradas(matriz3)
    for i in range(matriz3.shape[1]):
        # Verificar se a coluna atual é toda composta por zeros
        if np.any(matriz3[:, i] == 1):
            matriz4 = matriz3[:, i:]
            break
        
    # m_silver, matriz5 = quebrar_na_primeira_sequencia_zerada(matriz4)
    n_colunas = matriz4.shape[1]
    for i in range(n_colunas - 3):
        # Verificar se as 4 colunas consecutivas a partir da i-ésima são todas zeradas
        if np.all(matriz4[:, i] == 0) and np.all(matriz4[:, i+1] == 0) and np.all(matriz4[:, i+2] == 0) and np.all(matriz4[:, i+3] == 0):
            # Parte esquerda: até a coluna imediatamente antes da sequência zerada
            m_silver = matriz4[:, :i]
            
            # Parte direita: da coluna após a sequência zerada até o final
            matriz5 = matriz4[:, i+4:]
            
            break

    # m_copper = remover_primeiras_colunas_zeradas(matriz5)
    for i in range(matriz5.shape[1]):
        # Verificar se a coluna atual é toda composta por zeros
        if np.any(matriz5[:, i] == 1):
            m_copper = matriz5[:, i:]
            break
    
    m_gold = process_matrix(m_gold)

    m_silver = process_matrix(m_silver)

    m_copper = process_matrix(m_copper)

    return m_gold, m_silver, m_copper

def ler_matrizes_preco(matriz):

    indices_iguais = []

    matriz = matriz.T
    tuplas = matriz_mestre
    for index, tupla in enumerate(tuplas):
        for i in range(1, 8, 2):  # linhas ímpares (1, 3, 5, 7)
            if all(matriz[i][j] == tupla[j] for j in range(8)):
                indices_iguais.append(index)
                break  # Se encontrar um igual, não precisa verificar as outras linhas
    
    return indices_iguais