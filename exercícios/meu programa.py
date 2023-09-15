import PySimpleGUI as sg

def hora_sal():
    layout = [
        [sg.Text('Salário Mensal:'), sg.Input(key='-SALARIO-')],
        [sg.Text('Horas Trabalhadas por Dia:'), sg.Input(key='-HORAS-')],
        [sg.Text('Dias Trabalhados:'), sg.Input(key='-DIAS-')],
        [sg.Button('Calcular'), sg.Button('Sair')], #botoes
        [sg.Text('Resultado:'), sg.Text('', key='-RESULTADO-')]
    ]
#titulo do programa
    window = sg.Window('Cálculo do Salário Hora', layout)
# event loop no qual 
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Sair':#se apertar sair o app fecha
            break
#serão feito os calculos
        if event == 'Calcular':
            try:
                sal_mensal = float(values['-SALARIO-'])
                horas_trabalhadas = int(values['-HORAS-'])
                dias = int(values['-DIAS-'])
                horas_mes = horas_trabalhadas * dias
                sal_hora = sal_mensal / horas_mes

                window['-RESULTADO-'].update(f'Seu salário hora é de R$: {sal_hora:.2f}, Acorde cedo pra limpar a casa da velha ')# aqui foi inserido no layout
            except ValueError:
                sg.popup('Erro: Preencha todos os campos corretamente.')

    window.close()

hora_sal()
