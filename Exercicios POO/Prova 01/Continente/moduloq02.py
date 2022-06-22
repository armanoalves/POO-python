import os

class Continente:
  def __init__(self, name = None, paises = None):
    self.__name = name
    self.__paises = []

  def get_name(self):
    return self.__name
  def set_name(self):
    self.__name = str(input("Digite o nome do continente: "))

  def get_paises(self):
    return self.__paises
  def set_paises(self):
    while True:
      os.system("cls")

      obj = Pais()
      obj.set_name()
      obj.set_population()
      obj.set_dimension()
  
      self.__paises.append(obj)

      choice = str(input("Deseja adcionar mais paises ? [S/N]")).strip().upper()
      if choice == "N":
        os.system("cls")
        break

  def continent_dimension(self):
    value = 0
    for i in self.__paises:
      value = value + i.get_dimension()
    os.system("cls")
    print(f"A dimensão total do continente é: {value:.2f}\n")
    os.system("pause")
    os.system("cls")

  def continent_populations(self):
    value = 0
    for i in self.__paises:
      value = value + i.get_population()
    os.system("cls")
    print(f"A população total do continente é: {value:.2f}\n")
    os.system("pause")
    os.system("cls")

  def bigger_populations(self):
    bigger = 0
    name_of_biggest = ""
    for i in self.__paises:
      if i.get_population() > bigger:
        bigger = i.get_population()
        name_of_biggest = i.get_name()
    os.system("cls")
    print(f"O nome do pais com a maior população é: {name_of_biggest} com {bigger:.2f} habitantes\n")
    os.system("pause")
    os.system("cls")

  def small_populations(self):
    small = self.__paises[0].get_population()
    name_of_smallest = self.__paises[0].get_name()
    for i in self.__paises:
      if i.get_population() < small:
        small = i.get_population()
        name_of_smallest = i.get_name()
    os.system("cls")
    print(f"O nome do pais com a menor população é: {name_of_smallest} com {small:.2f} habitantes\n")
    os.system("pause")
    os.system("cls")

  def bigger_dimension(self):
    bigger = 0
    name_of_biggest = ""
    for i in self.__paises:
      if i.get_dimension() > bigger:
        bigger = i.get_dimension()
        name_of_biggest = i.get_name()
    os.system("cls")
    print(f"O nome do pais com maior dimensão territorial é: {name_of_biggest} com {bigger:.2f} km²\n")
    os.system("pause")
    os.system("cls")

  def small_dimension(self):
    small = self.__paises[0].get_dimension()
    name_of_smallest = self.__paises[0].get_name()
    for i in self.__paises:
      if i.get_dimension() < small:
        small = i.get_dimension()
        name_of_smallest = i.get_name()
    os.system("cls")
    print(f"O nome do pais com menor dimensão territorial é: {name_of_smallest} com {small:.2f} km²\n")
    os.system("pause")
    os.system("cls")

  def reason_between_biggest_and_smallest(self):
    small = self.__paises[0].get_dimension()
    bigger = 0
    reason = 0
    for i in self.__paises:
      if i.get_dimension() > bigger:
        bigger = i.get_dimension()

      if i.get_dimension() < small:
        small = i.get_dimension()

    reason = bigger / small
    os.system("cls")
    print(f"A razão territorial entre o menor pais com o maior é: {reason:.2f}\n")
    os.system("pause")
    os.system("cls")


class Pais:
  def __init__(self, name = None, population = None, dimension = None):
    self.__name = name
    self.__population = population
    self.__dimension = dimension

  def get_name(self):
    return self.__name
  def set_name(self):
    self.__name = str(input("Digite o nome do País: "))

  def get_population(self):
    return self.__population
  def set_population(self):
    self.__population = float(input("Digite a população do País: "))
  
  def get_dimension(self):
    return self.__dimension 
  def set_dimension(self):
    self.__dimension = float(input("Digite a dimensão do País: "))




    
  


      
         