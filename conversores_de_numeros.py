romanoParaInt = {'I': 1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000};

intParaRomano = {'I': 1, 'IV':4, 'V':5, 'IX': 9, 'X':10, 'XL': 40, 'L': 50, 
            'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000};

def romano_for_real_arabic(romano):
    # Um dicionario para o encontrar e diferenciar os valores romanos

    total = 0
    prev_value = 0

    #Vai iterar o número romano da direita para esquerda
    for char in reversed(romano):
        #Obter o valor do simbolo, pois a string não converte para char, assim não encontrando o simbolo romano.
        valor = romanoParaInt.get(char, 0)

        #verificar se o valor deve ser subtraido ou adicionado
        if valor < prev_value:
            total -= valor
        else:
            total += valor

        #Atualiza o valor anterior
        prev_value = valor

    return total


def real_arabic_for_romano(num):

    #Verifica se o numero é menor ou igual a 0 ou maior ou igual a 4000, pois podem ocorrer bugs acimas de 4000
    if num <= 0 or num >= 4000:
        #Envia um erro dizendo que o número não deve passar do intervalo.
        raise ValueError("Número fora do intervalo válido (1-3999)")
    
    #Dicionario para entender qual numero representa ao simbolo romano, assim conseguindo realizar a conversão sem erro

    #String vazia para construir o número romano.
    romano = ''
    #Vai percorrer a lista dos simbolos do maior para o menor.
    for simbolo in reversed(intParaRomano):
        dictValue = intParaRomano.get(simbolo)

        #Enquanto o número solicitado não for igual a 0, vai continuar adicionando o simbolo e reduzindo o numero 
        # referente ao simbolo adicionado.
        while num >= dictValue:
            romano += simbolo
            num -= dictValue
    return romano
