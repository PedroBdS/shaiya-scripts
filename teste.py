from funcoes import *

valor = ler_valor()

print(f'Valor lido: {valor}')

ouro, prata, cobre = converter_para_moedas(valor)

print(f"Reconversão:\nOuro: {ouro}, Prata: {prata}, Cobre: {cobre}")