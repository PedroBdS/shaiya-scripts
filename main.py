from funcoes import *

time.sleep(0.2)

abrir_leilao()

time.sleep(0.2)

atualizar_leilao()

time.sleep(0.2)

cor_nome = cor_do_nome()

valor = ler_preco()

valor_formatado = formatar_nome(valor, (255,255,255))

valor_formatado.show()