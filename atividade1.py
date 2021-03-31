def pega_entrada():
  entrada = []
  entrada = input("Insira os numeros com espaco entre eles: ").split(sep=" ")
  return entrada

def converte_entrada(numeros_em_texto):
  lista=[]
  for num in numeros_em_texto:
   num = int(num)
   lista.append(num)
  return lista

def media_da_lista(lista_de_numeros):
  quantidade_de_elementos = len(lista_de_numeros)
  soma=0
  for num in lista_de_numeros:
   soma+=num
   media=soma/quantidade_de_elementos
  return media

def main():
 entrada=pega_entrada()
 entrada_convertida=converte_entrada(entrada)
 print(media_da_lista(entrada_convertida))


main()
