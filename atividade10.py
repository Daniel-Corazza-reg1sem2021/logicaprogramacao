#Função 1 ---------
def funcao1(N):
  for number in range(int(N)):
    if number % 5 == 0 and number % 2 != 0:
      print(number)

funcao1(input("Coloque o número aqui: "))

#Função 2 -------
def funcao2():
  num_entradas = int(input("Digite o numero de entradas: "))
  lista = []
  i = 0
  while i < num_entradas:
    lista.append(input("Adicione na lista por aqui: "))
    i += 1
  return lista


print (funcao2())



#Função 4 ---------
def menu_futebol():
  opcao = input("Insira aqui a sua opção:")
  while opcao != 'z':
    if opcao == 'a':
      print("PSG")
    elif opcao == 'b':
      print("BAYERN")
    elif opcao == 'd':
      break
    opcao = input()
    
print (menu_futebol())
