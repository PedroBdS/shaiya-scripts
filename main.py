from funcoes import *

shaiya_aberto = checar_cor((939, 1061), (251, 239, 185))

if not shaiya_aberto:
    iniciar_shaiya('PedroGeromito')

abrir_leilao()
time.sleep(0.4)
click_ingame((931, 444))

while True:

    nome, valor = atualizar_leilao()

    comprar = comparar_item(nome, valor)

    if comprar:

        CONFERIR_E_COMPRAR(nome, valor)
        print(f'Autorizada compra de {nome} por {valor}')

        exit()

    if keyboard.is_pressed('F1'):
        print("Encerrando.")
        exit()
