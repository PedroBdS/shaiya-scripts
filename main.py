from funcoes import *

# time.sleep(0.2)

abrir_leilao()

# time.sleep(0.2)

# atualizar_leilao()

# time.sleep(0.2)

cor_nome = cor_do_nome()

valor = printar_preco()

valor.save('valor.png')

# Exemplo de uso
m_gold, m_silver, m_copper = print_para_matriz_UNIFICADA('valor.png')

for linha in m_gold:
    print(' '.join(map(str, linha)))

print()

for linha in m_silver:
    print(' '.join(map(str, linha)))

print()

for linha in m_copper:
    print(' '.join(map(str, linha)))
