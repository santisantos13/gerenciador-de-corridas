options = {
    1:'Registrar corrida',
    2:'Listar corrida',
    3:'Resumo do dia',
    4:'Resumo do mês',
    5:'Sair',
}
corridas = []

def RegistrarCorrida():
    print()

    while True:
        try:
            distancia_do_passageiro = float(input("Distância do passageiro: "))
            break
        except ValueError:
            print("Ops... digitou errado. Tente novamente.")

    while True:
        try:
            distancia_do_destino = float(input("Distância em corrida: "))
            break
        except ValueError:
            print("Ops... digitou errado. Tente novamente.")

    while True:
        try:
            valor_corrida = float(input("Valor pago: R$"))
            break
        except ValueError:
            print("Ops... digitou errado. Tente novamente.")

    km_total = distancia_do_passageiro + distancia_do_destino
    valor_km = valor_corrida / km_total

    print(f"{km_total:.2f} Kilometros")
    print(f"{valor_corrida:.2f}")
    print(f'R$/KM: {valor_km:.2f}')

    if valor_km < 1.50:
        print("Prejuizo😔")
    elif valor_km < 2.00:
        print("Aceitável😐")
    elif valor_km < 2.30:
        print("Boa corrida😊")
    else:
        print('Lucro alto😁')

    corridas.append({
        'Valor':valor_corrida,
        'Km':km_total,
        'R$/km':valor_km
    })
    print("Corrida Adicionada com Sucesso.✅\n")

def ListarCorrida():
    if not corridas:
        print("Nenhuma corrida registrada.")
        return

    for numero, corrida in enumerate(corridas, start=1):
        print(f"\n{'-' * 15} Corrida {numero} {'-' * 15}")

        print(f"Valor  : R$ {corrida['Valor']:.2f}")
        print(f"Km     : {corrida['Km']:.2f} km")
        print(f"R$/km  : R$ {corrida['R$/km']:.2f}")

    print('-' * 43)


while True:
    print(10 * '-','Gerenciador de Corridas', 10 * '-','\n')

    for chave, valor in options.items():
        print(chave,valor)
    print(45 * '-')
    choice = input('Escolha uma opção: ')

    if choice.isdigit() and int(choice) in options:
        choice = int(choice)

        if choice == 1:
            print(13 * '-',"Registrar corrida",13 * '-')
            RegistrarCorrida()
        
        
        elif choice == 2:
            print(15*'-', "Listar corrida",14*'-')
            ListarCorrida()
        
        
        elif choice == 3:
            print(10*'-', "Resumo do dia",10*'-')
        
        
        
        elif choice == 4:
            print(10*'-', "Resumo do mês",10*'-')
        
        
        
        elif choice == 5:
            print(10*'-', "Saindo...",10*'-')
            break
    else:
        print("Opção inválida.")