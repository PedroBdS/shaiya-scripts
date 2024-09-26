from funcoes import *

nome_lido = ler_nome()

valor_na_lista = encontrar_valor(nome_lido)

gold, silve, copper = valor_para_gold(valor_na_lista)

print(f'Nome: {nome_lido}\nValor: {gold}  {silve}  {copper}')