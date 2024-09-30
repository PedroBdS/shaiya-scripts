from funcoes import *

leilao_aberto_1 = ler_valor()

if not leilao_aberto_1:
    # corrigir_leilao()
    leilao_aberto_1 = ler_valor()

gold, prata, cobre = valor_para_gold(leilao_aberto_1)
valor_final = gold_para_valor(gold, prata, cobre)

print(leilao_aberto_1)

print(f'{gold}, {prata}, {cobre}')


print(f'{valor_final}')