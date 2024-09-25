from funcoes import *

time.sleep(0.2)

abrir_leilao()

time.sleep(0.2)

atualizar_leilao()

time.sleep(0.2)

img_nome, img_gold = printar_nome_e_valor()

cor_nome = cor_do_nome(img_nome)

print(f'cor do nome: {cor_nome}')

valor = print_para_valor(img_gold)

print(valor)

img_nome.show()
