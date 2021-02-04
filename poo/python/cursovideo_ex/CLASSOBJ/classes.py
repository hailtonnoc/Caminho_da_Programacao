
#atributos; numerador e denominaor

#Metodos; somar, subtrair, multiplicar, dividir, inverter, trocar de sinal e simplificar
class Fracao:
    def __init__(self, num, deno):
        self.numerador = num
        if deno == 0:
            self.denominador = 1
        else:
            self.denominador = deno

    #def somar(self):