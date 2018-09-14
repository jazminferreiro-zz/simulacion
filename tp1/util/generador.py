class GeneradorLinealCongruente:
  def __init__(self):
    """
    Crea una instancia de la clase GeneradorLinealCongruente
    """
    # Inicializa el valor actual del generador
    self.actual = 91867

    # Inicializa el incremento del generador
    self.incremento = 1664525

    # Inicializa el modulo del generador

    self.modulo = 2 ** 32

    # Inicializa el multiplicador del generador
    self.multiplicador = 1013904223

  def generar(self):
    """
    Genera un numero random entre 0 y 1

    :returns: El numero random generado
    """
    self.actual = (self.actual * self.multiplicador + self.incremento) % self.modulo

    return float(self.actual) / float(self.modulo)

  def generar_lista(self, cantidad):
    """
    Genera una lista de numeros random entre 0 y 1

    :param cantidad: La cantidad de numeros random a generar
    :returns: La lista de numeros random generados
    """
    lista = []

    for i in range(cantidad):
      lista.append(self.generar())

    return lista
