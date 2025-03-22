# uniao_pdf
Código para mesclar PDFs separados em um único arquivo PDF no mesmo diretório.

 Explicação linha por linha:

1. Importação de bibliotecas:
   - `import PyPDF2`: Usada para manipular arquivos PDF.
   - `import os`: Para interagir com o sistema operacional, como listar arquivos.
   - `import re`: Para usar expressões regulares, como encontrar números nos nomes dos arquivos.
   - `import random`: Para misturar aleatoriamente os arquivos sem números.

2. Função `ordenar_arquivos()`:
   - Lista arquivos PDF: `[f for f in os.listdir('.') if f.endswith(".pdf")]` lista todos os arquivos PDF no diretório atual.
   - Função interna `extrair_numero(nome)`:
     - Usa `re.search(r'\d+$', nome)` para encontrar o número no final do nome do arquivo.
     - Retorna uma tupla com o número (ou infinito se não encontrar) e o nome original.
   - Separa arquivos:
     - `arquivos_com_numero`: Arquivos com números no final.
     - `arquivos_sem_numero`: Arquivos sem números no final.
   - Mistura aleatoriamente os arquivos sem número: `random.shuffle(arquivos_sem_numero)`.
   - Ordena os arquivos com número: `arquivos_com_numero.sort(key=extrair_numero)`.
   - Combina as listas: `arquivos_ordenados = arquivos_com_numero + arquivos_sem_numero`.

3. Função `merge_pdfs(arquivos)`:
   - Cria um `PyPDF2.PdfMerger()` para mesclar PDFs.
   - Itera sobre cada arquivo na lista, adicionando-o ao mesclador.
   - Define o nome do arquivo de saída como "Arquivo_final.pdf".
   - Escreve o arquivo mesclado no disco e fecha o mesclador.

4. Execução:
   - Chama `ordenar_arquivos()` para obter a lista ordenada de arquivos.
   - Chama `merge_pdfs(arquivos)` para mesclar os PDFs.
   - Imprime uma mensagem de sucesso após a mesclagem.
