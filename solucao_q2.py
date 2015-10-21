string1 = input()
string2 = input()

i = 0

numero1 = []
numero2 = []

while i < len(string1) :
  # Os dois numeros tem o mesmo tamanho. Logo, podemos usar o mesmo laco.
  numero1.append(string1[i])
  numero2.append(string2[i])
  i = i + 1
  
vaiUm = 0

i = len(numero1) - 1

numeroFinal = []

while i >= 0 :
  resultado = int(numero1[i]) + int(numero2[i]) + vaiUm
  if int(numero1[i]) + int(numero2[i]) + vaiUm > 9 :
    vaiUm = 1
    resultado = resultado - 10
  else :
    vaiUm = 0
  numeroFinal.insert(0, resultado)    
  i = i - 1

print(numeroFinal)
