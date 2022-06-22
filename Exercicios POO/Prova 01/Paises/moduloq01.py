import os

class Pais:
  def __init__(self, code = None, name = None, dimension = None, populacion = None):
    self.__code = code
    self.__name = name
    self.__dimension = dimension
    self.__populacion = populacion
    self.__border = []

  def get_code(self):
    return self.__code
  def set_code(self):
    while True:
        x1 = str(input("Digite o codigo do país: ")).strip().upper()
        if len(x1) == 3:
          self.__code = x1
          break

  def get_name(self):
    return self.__name
  def set_name(self):
    self.__name = str(input("Digite o nome do país: ")).strip().capitalize()

  def get_dimension(self):
    return self.__dimension
  def set_dimension(self):
    self.__dimension = float(input("Digite a dimensão do país: "))

  def get_populacion(self):
    return self.__populacion
  def set_populacion(self):
    self.__populacion = float(input("Digite a população do país: "))

  def get_border(self):
    return self.__border
  def set_border(self):
    while True:
      x = str(input("Digite o nome do pais que faz fronteira, [N] para não adcionar mais: ")).strip().capitalize()
      if x == 'N' or x == 'n':
        break
      self.__border.append(x)

  def check_equality(self, object):
    if(self.__code == object):
      os.system("cls")
      print("Os objetos representam o mesmo Pais!")
      os.system("pause")
      os.system("cls")
    else:
      os.system("cls") 
      print("Os Objetos não representam o mesmo Pais!")
      os.system("pause")
      os.system("cls")


  def check_borderline(self, borderline):
    if (self.__border.count(borderline) == 1):
      os.system("cls")
      print(f"{self.__name} é limítrofe do comparado")
      os.system("pause")
      os.system("cls")
    else: 
      os.system("cls")
      print(f"{self.__name} não é limítrofe do comparado")
      os.system("pause")
      os.system("cls")
  
  def density(self):
    os.system("cls")
    print(f"A desidade do(a) {self.__name} é de: {self.__populacion/self.__dimension:.2f} habitantes por km²")
    os.system("pause")
    os.system("cls")
  
  def common_neighbors(self, contry):
    common = []
    for i in range(len(self.__border)):
      if(contry.__border.count(self.__border[i]) == 1):
        common.append(self.__border[i])
    os.system("cls")
    print(f"lista de vizinhos comuns aos dois países: {common}")
    os.system("pause")
    os.system("cls")
