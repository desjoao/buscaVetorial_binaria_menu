def buscaBin (vetor, tam, valor):
    inicio = 0
    final = tam - 1
    while inicio <= final:
        meio = int((inicio + final)/2)
        if vetor[meio] == valor:
            return meio
        elif vetor[meio] < valor:
            inicio = meio + 1
        else:
            final = meio - 1
    return -1

def leitura(tam):
    vetor = [-1]*tam
    for i in range(tam):
        vetor[i] = int(input(f'Insira o {i + 1}º valor de uma sequência {tam} números positivos, ordenados do menor ao maior: '))
        while vetor[i] < 0 or vetor[i] < vetor[i-1] :
           vetor[i] = int(input(f'Insira o {i + 1}º valor de uma sequência {tam} números POSITIVOS, ORDENADOS DO MENOR AO MAIOR: '))
    return vetor

num = int(input(f'Insira o número correspondente à operação desejada: \n1 - Inserir valores a um vetor \n2 - Buscar um valor no vetor \n3 - Exibir lista \n4 - Sair \n'))
res = 'n'

while num < 5:
    if num == 1:
        qnt = int(input(f'Informe o tamanho do vetor a ser criado: '))
        while qnt <= 0:
            print('Valor inválido.')
            qnt = int(input(f'Informe o tamanho do vetor a ser criado: '))
        vet = leitura(qnt)
        res = input('Gostaria de realizar mais alguma operação? (digite <sim> para sim) ')
        if res == 's' or res == 'S' or res == 'sim' or res == 'Sim':
            num = int(input(f'Insira o número correspondente à operação desejada: \n1 - Inserir valores a um vetor \n2 - Buscar um valor no vetor \n3 - Exibir lista \n4 - Sair \n'))
        else:
            break

    elif num == 2:
        if res == 's' or res == 'S' or res == 'Sim' or res == 'sim':
            val = int(input('Informe o valor a ser buscado: '))
            busca = buscaBin(vet, qnt, val)
            if busca == -1:
                print(f'Valor {val} não foi encontrado.')
            else:
                print(f'Valor {val} foi encontrado na posição {busca} do vetor {vet}.')
        elif res == 'n':
            print('A busca não foi possível pois não há vetor.')
        else:
            print('Resposta não válida.')
        res = input('Gostaria de realizar mais alguma operação? (digite <sim> para sim) ')
        if res == 's' or res == 'S' or res == 'sim' or res == 'Sim':
            num = int(input(f'Insira o número correspondente à operação desejada: \n1 - Inserir valores a um vetor \n2 - Buscar um valor no vetor \n3 - Exibir lista \n4 - Sair \n'))
        else:
            break

    elif num == 3:
        if res == 's' or res == 'S' or res == 'Sim' or res == 'sim':
            print(f'A lista criada é a seguinte: {vet}, possuindo {qnt} posições')
        elif res == 'n':
            print('A busca não foi possível pois não há vetor.')
        else:
            print('Resposta não válida.')
        res = input('Gostaria de realizar mais alguma operação? (digite <sim> para sim) ')
        if res == 's' or res == 'S' or res == 'sim' or res == 'Sim':
            num = int(input(f'Insira o número correspondente à operação desejada: \n1 - Inserir valores a um vetor \n2 - Buscar um valor no vetor \n3 - Exibir lista \n4 - Sair \n'))
        else:
            break

    elif num == 4:
        print('FIM.')
        break
    
    else:
        print('Opção inexistente.')
        break
