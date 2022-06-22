from moduloq02 import *
from time import sleep
List_contry = []
import os
print(f"{'Adicione os continentes':>30}")

continent = Continente()
continent.set_name()
os.system("cls")
while True:
  print(f"{'Menu de seleção':>30}\n")
  print("[1] Adcionar países ao continente")
  print("[2] Dimensão total do continente")
  print("[3] População total do continente")
  print("[4] País com maior população no continente")
  print("[5] País com menor população no continente")
  print("[6] País com maior dimensão territorial")
  print("[7] País com menor dimensão territorial")
  print("[8] Razão entre o país com maior dimensão com o menor")
  print("[0] Sair do seleção")

  choice = int(input("\nDigite sua opção: "))
  if choice == 0:
    os.system("cls")
    print("Finalizando programa, até a próxima...")
    sleep(3)
    break

  elif choice == 1:
    contry = Pais()
    continent.set_paises()

  elif choice == 2:
    continent.continent_dimension()

  elif choice == 3:
    continent.continent_populations()

  elif choice == 4:
    continent.bigger_populations()

  elif choice == 5:
    continent.small_populations()

  elif choice == 6:
    continent.bigger_dimension()
  
  elif choice == 7:
    continent.small_dimension()

  elif choice == 8:
    continent.reason_between_biggest_and_smallest()




