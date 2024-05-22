from etl import ler_csv, filtrar_produtos, somar_valor

path_arquivo = "vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregue = filtrar_produtos(lista_de_produtos)
valor_dos_produtos_entregue = somar_valor(produtos_entregue)

print(valor_dos_produtos_entregue)