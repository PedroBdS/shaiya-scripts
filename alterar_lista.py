from funcoes import *

nome_lido = ler_nome()

valor_na_lista = int(encontrar_valor(nome_lido))

gold, silver, copper = valor_para_gold(valor_na_lista)

print(f'\nNome: {nome_lido}')
print(f'Valor: {gold}  {silver}  {copper}\n')

alterar = input('Alterar valor? (S/N): ')

if alterar == 'S':
    valor_moedas = str(input('Digite o valor em ouro prata e cobre separando os valores por um espaço.\n\nNovo valor: '))

    gold_novo, silver_novo, copper_novo = valor_moedas.split()[0], valor_moedas.split()[1], valor_moedas.split()[2]
    print((f'\n\n{nome_lido}Valor atual: {gold}  {silver}  {copper} \nNovo  valor: {gold_novo}  {silver_novo}  {copper_novo}\n'))
    confirmar = input('(S/N): ')

    if confirmar == 'S':
        valor_novo = gold_para_valor(gold_novo, silver_novo, copper_novo)
        atualizar_item_csv(nome_lido, valor_novo)
