#variável que armazena um valor digitado
valor = float(input("Digite um valor: "))

#inicialização de variáveis
soma = 0
quantidade = 0
media = 0

#estrutura de repetição enquanto "valor" for maior que zero
while valor > 0.0:
    #incremento com os valores inseridos
    soma = soma + valor
    #incremento em quantidade de números digitados
    quantidade = quantidade + 1
    #input para continuar o ciclo
    valor = float(input("Digite um valor: "))

#obs.: caso o usuário digite um número negativo, o ciclo se encerra

#cálculo da media
media = soma / quantidade

#print das informações
print("\n Total da Soma:", soma)
print("\n Quantidade de valores digitados:", quantidade)
print("\n Média dos valores:", media)

