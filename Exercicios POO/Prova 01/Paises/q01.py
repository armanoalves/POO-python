from moduloq01 import *
from time import sleep
import os

List = []

print(f"{'Adicione os paises':>30}")

print("Adicione pelo menos dois paises para continuar o precesso")
print("\n")
print("Iniciando programa....")
sleep(3)

for i in range(2):
  os.system("cls")
  print(f"{i+1:>20}° Pais")
  contry = Pais()
  List.append(contry)
  contry.set_code()
  contry.set_name()
  contry.set_dimension()
  contry.set_populacion()
  contry.set_border()

os.system("cls")
while True:
  print(f"{'Menu de seleção':>30}\n")
  print("[1] Verificar se dois objetos representam o mesmo país")
  print("[2] Verificar se um país é limítrofe de outro")
  print("[3] Verificar a densidade populacional do país")
  print("[4] Verificar os paises vizinhos em comum entre dois paises")
  print("[5] Verificar os paises em ordem alfabética")
  print("[6] Criar um novo país")
  print("[0] Sair do seleção")

  op = int(input("Digite sua opção: "))

  if op == 0:
    os.system("cls")
    print("Finalizando programa, até a próxima...")
    sleep(3)
    os.system("cls")
    break

  elif op == 1:
    os.system("cls")
    print(f"{'Pais atual':>25}: {contry.get_name()}")
    qt = str(input("Digite o nome do pais para comparar com o atual: ")).strip().capitalize()
    for i in List:
      if qt == i.get_name():
        contry.check_equality(i.get_code())

  elif op == 2:
    os.system("cls")
    print(f"{'Pais atual':>25}: {contry.get_name()}")
    qt = str(input("Digite o nome do pais para verificar: ")).strip().capitalize()
    for i in List:
      if qt == i.get_name():
        contry.check_borderline(qt)

  elif op == 3:
    contry.density()

  elif op == 4:
    os.system("cls")
    print(f"{'Pais atual':>25}: {contry.get_name()}")
    qt = str(input("Digite o nome para verificar: ")).strip().capitalize()
    for i in List:
      if qt == i.get_name():
        contry.common_neighbors(i)  
        
  elif op == 5:
    x = []
    for i in List:
      x.append(i.get_name())
    x.sort()
    os.system("cls")
    print(f"Lista em ordem alfabetica: {x}")
    os.system("pause")
    os.system("cls")

  elif op == 6:
    contry = Pais()
    List.append(contry)
    contry.set_code()
    contry.set_name()
    contry.set_dimension()
    contry.set_populacion()
    contry.set_border()
    
