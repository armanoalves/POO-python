class Pessoa:

  #Função responsavel por inicializar o banco de dados e estabelecer uma conexão
  def initialize_db():
    import psycopg2

    host = "localhost"
    dbname = "Banco-POO"
    user = "postgres"
    password = "963852741"

    conn_string = "host={0} dbname={1} user={2} password={3}".format(host, dbname, user, password)

    conn = psycopg2.connect(conn_string)
    print("Connection established")

    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS produto")
    print("Finished dropping table (if exists)")

    cursor.execute("CREATE TABLE produto (id serial PRIMARY KEY, nome VARCHAR(50), quantidade INTEGER);")
    print("Finished creating table")

    return conn, cursor

  #Função responsavel por inserir novos produtos na tabela 
  def incluir_novo_produto(conn, cursor):
    nome = input("Digite o nome do produto: ")
    quantidade = input("Digite a quantidade do produto: ")

    cursor.execute("INSERT INTO produto (nome, quantidade) VALUES (%s, %s);", (nome, quantidade))

    conn.commit()

    input("Dados inseridos com Sucesso - Tecle <Entre> para continuar")

  #Função responsavel por apresentar todos os produtos que estão na tabela
  def listar_todos_os_produtos(conn, cursor):

    cursor.execute("SELECT * FROM produto;")
    
    rows = cursor.fetchall()

    for row in rows:
        print("Data row = (%s, %s, %s)"%(str(row[0]), str(row[1]), str(row[2])))

    input("Tecle <Entre> para continuar")

  #Função responsavel por adicionar uma certa quantidade de produtos no estoque
  def adicionar_ao_estoque(conn, cursor):

    name = input("Digite o nome do produto: ")

    cursor.execute(f"SELECT * FROM produto WHERE nome = '{name}'")

    rows = cursor.fetchall()
    if len(rows) > 0:
      info = rows[0]
      produto_qty = info[2]
      qty = int(produto_qty)
      quantidade = int(input("Digite a quantidade do produto: "))
      qty = qty + quantidade
      cursor.execute(f"UPDATE produto SET quantidade = '{qty}' WHERE nome = '{info[1]}';")
      print("change completed")
    else:
      print("Produto inexistente")

    conn.commit()
    input("Tecle <Entre> para continuar")

  #Função responsavel por retirar uma certa quantidade de produtos no estoque
  def retirar_do_estoque(conn, cursor):

    name = input("Digite o nome do produto: ")

    cursor.execute(f"SELECT * FROM produto WHERE nome = '{name}'")  
    rows = cursor.fetchall()
    mostrar = True
    if len(rows) > 0:

      info = rows[0]
      produto_qty = info[2]
      qty = int(produto_qty)
      quantidade = int(input("Digite a quantidade do produto: "))
      qty = qty - quantidade
      if qty >= 0:
        cursor.execute(f"UPDATE produto SET quantidade = '{qty}' WHERE nome = '{info[1]}';")
        print("change completed")
      else:
        print("Não é possível fazer a saída de estoque  – quantidade menor que o valor desejado")
        mostrar = False
    elif mostrar == True:
      print("Produto inexistente")

    conn.commit()
    input("Tecle <Entre> para continuar")
  
  #Função responsavel por apagar um certo produto de dentro da tabela
  def excluir_produto(conn, cursor):
    nome = input("Digite o nome do produto: ")

    cursor.execute("DELETE FROM produto WHERE nome = %s;", (nome,))
    print("Deleted 1 row of data")

    conn.commit()

    input("Tecle <Entre> para continuar")

  #Função responsavel por desconectar o banco de dados e desestabelecer a conexão
  def desconect_db(conn, cursor):
    cursor.close()
    conn.close()
    print("Connection closed")  