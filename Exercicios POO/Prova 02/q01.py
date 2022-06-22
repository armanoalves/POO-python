from moduloq01 import *

conn, cursor = Pessoa.initialize_db()

while True:
  print(f"{'Menu de seleção':>30}\n")
  print("[1] Incluir novo produto")
  print("[2] Listar todos os produtos")
  print("[3] Adicionar ao estoque")
  print("[4] Retirar do estoque")
  print("[5] Excluir produto")
  print("[6] Sair do banco de dados")
  print("[0] Sair do seleção")

  choice = int(input("Digite sua Opção: "))
  if choice == 0:
    break
  elif choice == 1:
    Pessoa.incluir_novo_produto(conn, cursor)
  elif choice == 2:
    Pessoa.listar_todos_os_produtos(conn, cursor)
  elif choice == 3:
    Pessoa.adicionar_ao_estoque(conn, cursor)
  elif choice == 4:
    Pessoa.retirar_do_estoque(conn, cursor)
  elif choice == 5:
    Pessoa.excluir_produto(conn, cursor)
  elif choice == 6:
    Pessoa.desconect_db(conn, cursor)