from funcoes import *

shaiya_aberto = checar_cor((939, 1061), (251, 239, 185))

if not shaiya_aberto:
    iniciar_shaiya('PedroGeromito')

abrir_leilao()
time.sleep(0.4)
click_ingame((931, 444))

while True:
    if keyboard.is_pressed('F1'):
        print("Encerrando.")
        exit()

    if not leilao_posicao_correta():
        corrigir_leilao()

    atualizar_leilao(delay= 0)

    try:
        # nome_1, valor_1, nome_2, valor_2, nome_3, valor_3, nome_4, valor_4 = ler_leilao()
        print(f'Fazendo leitura')
        nome_1, valor_1, nome_2, valor_2, nome_3, valor_3 = ler_leilao()

    except:
        continue

    if not valor_1:
        corrigir_leilao()
        continue
    
    '''
    print(f'Primeiro item: {nome_1}')
    print(f'Primeiro valor: {valor_1}')
    # print(f'Primeiro qtd: {ler_qtd(1)}')
    print(f'Segundo item: {nome_2}')
    print(f'Segundo valor: {valor_2}')
    # print(f'Segundo qtd: {ler_qtd(2)}')
    print(f'Terceiro item: {nome_3}')
    print(f'Terceiro valor: {valor_3}')
    '''


    # comprar4 = comparar_item(nome_4, valor_4)

    # if comprar4:
    #     print(f'Autorizada compra de {nome_4} por {valor_4}')
    #     CONFERIR_E_COMPRAR(nome_4, valor_4, 4)
    #     continue

    comprar3 = comparar_item(nome_3, valor_3)

    if comprar3:
        print(f'Autorizada compra de {nome_3} por {valor_3}')
        CONFERIR_E_COMPRAR(nome_3, valor_3, 3)
        continue

    comprar2 = comparar_item(nome_2, valor_2)

    if comprar2:
        print(f'Autorizada compra de {nome_2} por {valor_2}')
        CONFERIR_E_COMPRAR(nome_2, valor_2, 2)
        continue

    comprar1 = comparar_item(nome_1, valor_1)

    if comprar1:
        print(f'Autorizada compra de {nome_1} por {valor_1}')
        CONFERIR_E_COMPRAR(nome_1, valor_1, 1)
        continue
    

    if keyboard.is_pressed('F1'):
        print("Encerrando.")
        exit()
