import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Função que lê um arquivo CSV e retorna uma lista de dicionários,
    onde cada dicionário representa uma linha do arquivo.
    
    Args:
        nome_do_arquivo_csv (str): O caminho para o arquivo CSV.
        
    Returns:
        list[dict]: Uma lista de dicionários contendo os dados do CSV.
    """
    lista = []
    try:
        with open(nome_do_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                lista.append(linha)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_do_arquivo_csv}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")    
    return lista

def filtrar_produtos(lista: list[dict]) -> list[dict]:
    """
    Função que filtra produtos entregue = True
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)       
    return (lista_com_produtos_filtrados)

def somar_valor(lista_com_produtos_filtrados: list[dict]) -> int:
    """
    Soma todos os produtos que estão na lista
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:  
        valor_total += int(produto.get("price"))
    return valor_total






