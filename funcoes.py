import pyautogui
import time
import keyboard
from PIL import ImageGrab, Image
import numpy as np
import pytesseract
import csv

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

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

def click_ingame(coordenada, delay=0):
    coordenada2 = (coordenada[0]+1, coordenada[1])

    pyautogui.moveTo(coordenada)
    pyautogui.mouseDown()

    pyautogui.moveTo(coordenada)

    pyautogui.moveTo(coordenada)

    pyautogui.mouseUp()

def matriz_para_tuplas(matriz):
    return [tuple(int(valor) for valor in linha) for linha in matriz]

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

    if not(checar_cor((595, 246), (73, 73, 72)) and checar_cor((597, 249), (35, 34, 36))):
        click_ingame((1422, 1036))
        time.sleep(0.3)
        click_ingame((1250, 312))
       

    if not(checar_cor((595, 246), (73, 73, 72)) and checar_cor((597, 249), (35, 34, 36))):
        print('Não foi possível abrir o leilão')
        return False

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

def cor_do_nome(imagem):

    pixels = list(imagem.getdata())
    
    for pixel in pixels:
        if pixel in cores_predefinidas:
            return pixel
        
    print(f'Falha ao identificar a cor do nome.')
    return (0, 0, 0)

def checar_novo_item():

    # novo_nome = ler_nome()
    novo_valor = ler_valor()

def atualizar_leilao(delay=False):
    if not delay:
        click_ingame((1250, 312))
        return
    time.sleep(0.05)
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

def separa_matriz(matriz):
    # Converte a matriz para um array NumPy (caso ainda não seja)
    matriz = np.array(matriz)
    
    # Verifica se o número de colunas é par
    if matriz.shape[1] % 2 != 0:
        raise ValueError("O número de colunas deve ser par")
    
    # Seleciona as colunas ímpares (índices 0, 2, 4, ...)
    colunas_impares = matriz[:, ::2]
    
    # Seleciona as colunas pares (índices 1, 3, 5, ...)
    colunas_pares = matriz[:, 1::2]
    
    return matriz_para_tuplas([tuple(linha) for linha in colunas_impares.T]), matriz_para_tuplas([tuple(linha) for linha in colunas_pares.T])

def converte_para_numero(matriz_impar, matriz_par):
    resposta = ''
    i = 0
    for numero in matriz_impar:
        for num in matriz_mestre:
            if numero == num:
                if numero == (0,1,1,1,1,1,1,0):
                    if matriz_par[i][3]==1:
                        resposta= resposta+str(6)
                        break
                    else:
                        resposta= resposta+str(0)
                        break
                resposta= resposta+str(matriz_mestre.index(num)+1)
                break
        i += 1
    return int(resposta)
                
def numero_para_valor(gold, silver, copper):
    return gold*1000000000 + silver*100000 + copper

def ler_valor():



    imagem = capturar_tela((1182, 398), (1287, 406))

    imagem = formatar_nome(imagem, (255,255,255))
    imagem = imagem.convert('1')   
    matriz = np.array(imagem, dtype=int)

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

    m_gold_a, m_gold_b = separa_matriz(m_gold)

    m_silver_a, m_silver_b = separa_matriz(m_silver)

    m_copper_a, m_copper_b = separa_matriz(m_copper)

    gold = converte_para_numero(m_gold_a, m_gold_b)
    # print(f'Gold: {gold}')

    silver = converte_para_numero(m_silver_a, m_silver_b)
    # print(f'silver: {silver}')

    copper = converte_para_numero(m_copper_a, m_copper_b)
    # print(f'copper: {copper}')

    valor = numero_para_valor(gold, silver, copper)

    return valor

def extrair_texto_imagem(imagem):

    # Usa o pytesseract para extrair o texto
    texto = pytesseract.image_to_string(imagem)  # 'lang' define o idioma, aqui é português
    
    return texto

def ler_nome():
    imagem_nome = capturar_tela((808, 376), (1025, 390))
    cor_nome = cor_do_nome(imagem_nome)
    img_nome_tratado = formatar_nome(imagem_nome, cor_nome)
    nome = extrair_texto_imagem(img_nome_tratado)

    img_nome_tratado.save('teste_lerNome.png')

    return nome

def comparar_item(nome, valor, arquivo='lista.csv'):

    with open(arquivo, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for linha in reader:
            if linha[0] == nome:
                valor_arquivo = float(linha[1])  # Converte o valor para float
                if valor > valor_arquivo:
                    return False
                elif valor < valor_arquivo:
                    return True
                else:
                    return True
    
    with open(arquivo, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([nome, 0])  # Adiciona o nome com valor 0
        print(f'NOVO ITEM ADICIONADO: {nome}')
    return False