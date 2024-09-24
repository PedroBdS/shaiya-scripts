import pyautogui
from PIL import Image

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

# A conexão com o servidor foi encerrada. ERROR 10053
# Posição do mouse: (854, 461), Cor do pixel: (17, 16, 16)
# Posição do mouse: (895, 493), Cor do pixel: (16, 16, 16)

coordenada1 = (854, 461)  # Coordenada inicial (x1, y1)
coordenada2 = (895, 493)  # Coordenada final (x2, y2)

capturar_tela(coordenada1, coordenada2, 'ERROR_10053.png')