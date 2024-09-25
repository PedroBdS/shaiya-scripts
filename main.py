from funcoes import *
from abrir_shaiya import *

shaiya_aberto = checar_cor((939, 1061), (251, 239, 185))

if not shaiya_aberto:
    iniciar_shaiya('PedroGeromito')


abrir_leilao()
time.sleep(0.4)
click_ingame((931, 444))

while True:

    atualizar_leilao()

    nome = ler_nome()

    valor = ler_valor()

    comprar = comparar_item(nome, valor)

    # print(f'Comprar = {comprar}')

    if keyboard.is_pressed('q'):
        print("Encerrando.")
        break

