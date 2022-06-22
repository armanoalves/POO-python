from moduloq03 import *
import os
from time import sleep

print(f"{'Batimentos Cardíacos':>30}")

pacient = BatimentosCardiacos()
pacient.set_firstName()
pacient.set_lastName()
pacient.set_birthDate()

while True:
  print(f"{'Menu de seleção':>30}\n")
  print("[1] Idade do parciente")
  print("[2] Frequência cardíaca máxima do parciente")
  print("[3] Frequência cardíaca alvo do parciente")
  print("[0] Sair do seleção")

  choice = int(input("Digite sua opção: "))

  if choice == 0:
    os.system("cls")
    print("Finalizando programa, até a próxima...")
    sleep(3)
    os.system("cls")
    break
  elif choice == 1:
    pacient.age()
  elif choice == 2:
    pacient.heart_rate_max()
  elif choice == 3:
    pacient. target_heart_rate()
