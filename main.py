#calculadora de imc
# imc = peso/ (altura x altura)
# < 19: delgadez
# entre 20 y 25: normal
# >mas de 30: obesidad

def calcularIMC(peso, alturaEnMetros):
    imc = peso / (alturaEnMetros * alturaEnMetros)
    return imc

def pedirElImc():
    peso = float(input('Ingrese su peso en kg'))
    alturaEnCm = int(input('ingrese su altura en cm'))
    alturaEnMetros = alturaEnCm / 100
    imc = calcularIMC(peso, alturaEnMetros)

    print('su imc es de ' + str(imc))

    if imc <= 20:
        print('Delgado')
    if imc >= 20 and imc <26:
        print('Peso Normal')
    if imc >= 26 and imc <30:
        print('Sobrepeso')
    if imc <= 30:
        print('obesidad')

print("calcular el imc de la primer persona")
pedirElImc()
print("calcular el imc de la segunda persona")
pedirElImc()
print("calcular el imc de la tercer persona")
pedirElImc()