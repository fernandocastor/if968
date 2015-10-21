numero = int(input())

numerosLidos = []

maioresQueN = 0
menoresQueN = 0

while numero != 0 :
  numerosLidos.append(numero)
  numero = int(input())

N = int(input())

achouNEntreNumerosLidos = False

for x in numerosLidos :
  if x == N :
    achouNEntreNumerosLidos = True
  if x < N:
    menoresQueN = menoresQueN + 1
  elif x > N:
    maioresQueN = maioresQueN + 1

if not achouNEntreNumerosLidos :
  print("O numero", N, "nao foi fornecido antes.")
else :
  i = 1
  maior = numerosLidos[0]
  while i < len(numerosLidos):
    if numerosLidos[i] > maior:
      maior = numerosLidos[i]
    i = i + 1

  print(maioresQueN)
  print(menoresQueN)
  print(maior)
