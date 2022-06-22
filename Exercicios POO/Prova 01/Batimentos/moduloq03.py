class BatimentosCardiacos:

  def __init__(self, firstName = None, lastName = None, birthDate = None, age = None):
    self.__firstName = firstName
    self.__lastName = lastName
    self.__birthDate = birthDate
    self.__age = age

  def get_firstName(self):
    return self.__first_name
  def set_firstName(self):
    self.__firstName = str(input("Digite o seu primeiro nome: ")).strip()
  
  def get_lastName(self):
    return self.__lastName
  def set_lastName(self):
    self.__lastName = str(input("Digite o seu sobrenome: ")).strip()

  def get_birthDate(self):
    return self.__birthDate
  def set_birthDate(self):

    date = BirthDate()
    date.set_month()
    date.set_day()
    date.set_year()
    self.__birthDate = date

  def age(self):
    from datetime import datetime

    anything = datetime.now()

    present_month = anything.month
    present_day = anything.day
    present_year = anything.year

    age = present_year - self.__birthDate.get_year()

    if present_month < self.__birthDate.get_month():
      age = age -1
    elif present_day < self.__birthDate.get_day() and present_month == self.__birthDate.get_month():
      age = age - 1

    self.__age = age
    print(f"A sua idade é de {age} anos")

  def heart_rate_max(self):
    print(f"A sua frequêcia cardíaca máxima {self.__firstName} {self.__lastName}\n por minuto é: {220 - self.__age}")

  def target_heart_rate(self):
    print(f"A sua frequêmcia cardíaca alvo {self.__firstName} {self.__lastName}\né de: {(220 - self.__age) * 0.85}")


class BirthDate:
  def __init__(self, month = None, day = None, year = None):
    self.__month = month
    self.__day = day
    self.__year  = year

  def get_month(self):
    return self.__month
  def set_month(self):
    self.__month = int(input("Digite o mês em que você nasceu: "))
  
  def get_day(self):
    return self.__day
  def set_day(self):
    self.__day = int(input("Digite o dia em que você nasceu: "))

  def get_year(self):
    return self.__year
  def set_year(self):
    self.__year = int(input("Digite o ano em que você nasceu: "))