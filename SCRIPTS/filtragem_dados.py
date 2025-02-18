import pyodbc
import csv

server = '######\\SQLEXPRESS'  # Nome do servidor
database = 'TESTESSQL'  # Nome do banco de dados

conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
caminho_fixo = r"C:\Users\#####\Desktop\Projetos\SQL\resultados.csv" # Caminho fixo para salvar arquivo csv
filtro = input("Digite o filtro para buscar o nome do usuário (ou deixe vazio para todos): ")


try:
    # Conectar ao banco de dados
    print("Tentando conectar ao banco de dados...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Conexão bem-sucedida!")

     # Criar a consulta SQL com o filtro
    if filtro:  # Se o filtro não estiver vazio
        consulta_sql = f"SELECT * FROM usuarios WHERE nome LIKE ?"
        cursor.execute(consulta_sql, ('%' + filtro + '%',))  # Adicionando o filtro
    else:
        consulta_sql = "SELECT * FROM usuarios"
        cursor.execute(consulta_sql)

    # Obter os resultados
    usuarios = cursor.fetchall()

    # Verificar se retornou resultados
    if usuarios:
        print("Dados encontrados:")
        for usuario in usuarios:
            print(usuario)

        # Perguntar se o usuário deseja salvar os resultados em um CSV
        salvar = input("\nDeseja salvar os resultados em um arquivo CSV? (s/n): ").lower()

        if salvar == 's':
            # Nome do arquivo CSV
            nome_arquivo = "resultados.csv"

            # Obter os nomes das colunas (campos) da tabela
            colunas = [desc[0] for desc in cursor.description]

            # Abrir o arquivo CSV para escrita
            with open(caminho_fixo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                
                # Escrever o cabeçalho (nomes das colunas)
                escritor_csv.writerow(colunas)
                
                # Escrever os dados
                for usuario in usuarios:
                    escritor_csv.writerow(usuario)

            print(f"Os resultados foram salvos no arquivo: {nome_arquivo}")
        else:
            print("Os resultados não foram salvos.")
    else:
        print("Nenhum dado encontrado com o filtro especificado.")

    # Fechar a conexão
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
