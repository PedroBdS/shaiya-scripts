from funcoes import *

shaiya_iniciou = iniciar_shaiya('PedroGeromito')

if not shaiya_iniciou:
    print(f'Falha ao entrar no Shaiya')
    exit()
    
print(f'Shaiya iniciado com sucesso')

time.sleep(1)

abrir_leilao()

atualizar_leilao()

cor_nome = cor_do_nome()
