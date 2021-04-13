def exerc1():
    nota1 = int(input("Digite a nota 1: "))
    nota2 = int(input("Digite a nota 2: "))
    nota3 = int(input("Digite a nota 3: "))

    soma_notas = nota1 + nota2 + nota3
    media_notas = soma_notas/3

    print(f'Média do aluno é {media_notas}')




def exerc2():
  num_entradas = int(input("Digite o tamanho da lista: "))
  lista_de_saida = []
  i = 0
  while i < num_entradas:
    lista_de_saida.append(input("Adicione na lista por aqui: "))
    i += 1
  return lista_de_saida


def exerc3():
  opcao = input("Entre com sua opção aqui: ")
  while opcao !='z' or opcao !='Z':
    if opcao == 'a':
      print("Globo")
    elif opcao == 'b':
      print('SBT')
    else:
      print("Inválido")
      break
    opcao = input()




def exerc4(lista):
  medias_inferiores_que_7 = 0
  for elemento in lista:
    if elemento < 7:
      medias_inferiores_que_7 += 1
  if medias_inferiores_que_7 * len(lista) > 0.25:
    return "Professor Coxa"
  else:
    return "Professor Padrão"    
lista = []


