import pyautogui
from PIL import Image

def print_unique_colors(image_path):
    # Abre a imagem
    image = Image.open(image_path)
    
    # Converte a imagem para RGB (caso não esteja nesse formato)
    image = image.convert('RGB')
    
    # Obtém os pixels da imagem
    pixels = image.getdata()
    
    # Usa um set para armazenar as cores únicas
    unique_colors = set(pixels)
    
    # Printa cada cor única
    for color in unique_colors:
        print(color)

def capturar_tela(coordenada1, coordenada2, arquivo_saida='captura.png'):
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
    
    # Salvar a captura de tela em PNG
    screenshot.save(arquivo_saida)
    
    print(f"Imagem salva como {arquivo_saida}")

'''
Erros relatados:

# A conexão com o servidor foi encerrada. ERROR 10053
# Posição do mouse: (854, 461), Cor do pixel: (17, 16, 16)
# Posição do mouse: (895, 493), Cor do pixel: (16, 16, 16)


'''
# printar erros
# capturar_tela((854, 461), (895, 493), 'A_conexão_com_o_servidor_foi_encerrada.png')

'''
Posição do mouse: (1187, 397), Cor do pixel: (51, 50, 22)
Posição do mouse: (1287, 407), Cor do pixel: (51, 50, 22)
'''

capturar_tela((1182, 397), (1287, 407), './images/janela_do_preco.png')




