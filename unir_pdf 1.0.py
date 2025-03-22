# Importa as bibliotecas necessárias
import PyPDF2  # Biblioteca para manipulação de PDFs
import os      # Biblioteca para interação com o sistema operacional
import re      # Biblioteca para expressões regulares
import random  # Biblioteca para geração de números aleatórios

# Função para ordenar os arquivos PDF com base no final do nome
def ordenar_arquivos():
    """
    Ordena os arquivos PDF no diretório atual com base nos números presentes no final dos nomes dos arquivos.
    Arquivos sem números são misturados aleatoriamente e colocados no final da lista.
    
    :return: Lista de nomes de arquivos PDF ordenados.
    """
    
    # Lista todos os arquivos PDF no diretório atual
    arquivos = [f for f in os.listdir('.') if f.endswith(".pdf")]
    
    # Função interna para extrair o número do final do nome do arquivo
    def extrair_numero(nome):
        """
        Extrai o número do final do nome do arquivo e retorna uma tupla com o número e o nome original.
        Se não encontrar número, retorna uma tupla com infinito e o nome original.
        
        :param nome: Nome do arquivo.
        :return: Tupla contendo o número (ou infinito) e o nome do arquivo.
        """
        
        # Usa expressão regular para encontrar o número no final do nome
        match = re.search(r'\d+$', nome)
        
        # Se encontrar um número, retorna uma tupla com o número e o nome original
        if match:
            return (int(match.group()), nome)  # Tupla para manter a ordem dos números e o nome original
        else:
            # Se não encontrar número, retorna uma tupla com infinito e o nome original
            return (float('inf'), nome)  # Se não encontrar número, coloca no final
    
    # Separa arquivos com e sem número no final
    arquivos_com_numero = [arquivo for arquivo in arquivos if re.search(r'\d+$', arquivo)]
    arquivos_sem_numero = [arquivo for arquivo in arquivos if not re.search(r'\d+$', arquivo)]
    
    # Mistura aleatoriamente os arquivos sem número
    random.shuffle(arquivos_sem_numero)
    
    # Ordena os arquivos com número
    arquivos_com_numero.sort(key=extrair_numero)
    
    # Combina as listas, mantendo os arquivos com número na ordem correta
    arquivos_ordenados = arquivos_com_numero + arquivos_sem_numero
    
    return arquivos_ordenados

# Função para mesclar os PDFs
def merge_pdfs(arquivos):
    """
    Mescla os PDFs listados em um único arquivo chamado "Arquivo_final.pdf".
    
    :param arquivos: Lista de nomes de arquivos PDF a serem mesclados.
    """
    
    # Cria um objeto para mesclar PDFs
    merger = PyPDF2.PdfMerger()
    
    # Itera sobre cada arquivo na lista
    for arquivo in arquivos:
        # Define o caminho do arquivo como o nome do arquivo (considerando que estão no diretório atual)
        caminho_arquivo = arquivo
        
        # Adiciona o arquivo ao mesclador
        merger.append(caminho_arquivo)
    
    # Define o nome do arquivo de saída
    output_file = "Arquivo_final.pdf"
    
    # Escreve o arquivo mesclado no disco
    merger.write(output_file)
    
    # Fecha o mesclador para liberar recursos
    merger.close()

# Ordena e mescla os PDFs
arquivos = ordenar_arquivos()
merge_pdfs(arquivos)

# Imprime uma mensagem de sucesso
print("PDFs mesclados com sucesso!")
