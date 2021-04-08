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
