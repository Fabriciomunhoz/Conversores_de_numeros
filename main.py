from conversores_de_numeros import romano_for_real_arabic, real_arabic_for_romano
fechar = False

print('Bem vindo ao programa que converte Números romanos para Número real e Número real para Romano.\nAutor: Fabricio Munhoz Badeluk')
print('Avaliação Etapa 2 - Processo seletivo Atividade 2.1\n\n')

while fechar == False:
    print('Escolha a conversão \n1- Romano para número real.\n2- Numero real para Romano.\n')
    chose = input()

    if chose == '1':
        print('Numeros Romanos: ')
        roman_number = input()
        print(romano_for_real_arabic(roman_number))
    elif chose == '2':
        print('Números reais: ')
        real_number = input()
        try:
            if (real_number.isdigit() is False):
                raise ValueError("isso não é um int!");
            print(f"Número romano em real: {real_arabic_for_romano(int(real_number))}")
        except ValueError as e:
            print(e)
    else:
        print('Escolha invalida. Por favor insira 1 ou 2!\n')
    
    print('Deseja finalizar ou continuar?\n')
    print('1 - Continuar\n2 - Fechar')
    escolha = input()
    
    if escolha == '1':
        fechar = False
    if escolha == '2':
        fechar = True


