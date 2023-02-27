# Menu
while True:
    try:
        print('Menu:')
        print('1: Iniciar Calculadora')
        print('Qualquer tecla: Sair')
        option = input('Qual sua opção: ')
        if option != '1':
            print('Você escolheu sair')
            break
        else:
            print('Escolha dois números: ')
            x = float(input('x: '))
            y = float(input('y: '))
            print('Agora escolha a Operação Aritmética.')
            op = input('Escolha entre (+, -, *, /, **, raiz): ')
            if op == '+':
                print(f'A soma é {x + y}')
            elif op == '-':
                if x > y:
                    print(f'A diferença é {x - y}')
                else: 
                    print(f'A diferença é {y - x}')
            elif op == '*':
                print(f'A multiplicação é {x * y}')
            elif op == '/':
                print(f'A Divisão entre x e y é {x / y}')
            elif op == '**':
                print(f'X elavado à Y é {x ** y}')
            elif op == 'raiz':
                print(f'Raiz {y} de {x} é {x ** (1 / y)}')
            else:
                break
    except Exception as erro:
         print(f'ERRO: {erro}. Tente novamente!!!')