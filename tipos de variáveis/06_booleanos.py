# Booleanos comportam 'true' e 'false'

verdadeiro = True

if verdadeiro == True:
    print("A condição é verdadeira")

else:
    print("Condição fala")

# Operadores lógicos AND e OR

# AND será execultado apeas se as duas condições forem verdadeiras
if True and True:
    print("Bloco será execultado")

if True and False:
    print("Bloco não será execultado")

if False and False:
    print("Bloco não será execultado")

# OR será execultado se ao menos uma das condições forem verdadeiras
if True or True:
    print("Bloco será execultado")

if True or False:
    print("Bloco será execultado")

if False or False:
    print("Bloco não será execultado")