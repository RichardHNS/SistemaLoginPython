import PySimpleGUI as sg

# Defina o layout da janela
layout = [
    [sg.Text('Usuario:'), sg.Input(key='Usuario')],
    [sg.Text('Senha:'), sg.Input(key='Senha', password_char='*')],
    [sg.Button('Login')],
    [sg.Text('', key="mensagem")]
]

# Crie a janela diretamente com o layout
window = sg.Window('Login', layout)

# Loop principal para lidar com eventos da janela
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break

    elif event == 'Login':
        usuario_correto = "Richard"
        senha_correta = "123456"

        # Faça o que precisa ser feito quando o botão de login é pressionado
        username = values['Usuario']
        password = values['Senha']
        # Faça a validação do login, etc.
    if Senha == senha_correta and Usuario == usuario_correto:
        window['mensagem'].update('')
    else:
        window['mensagem'].update('senha ou usuário incorreto')    
# Feche a janela ao sair do loop principal
window.close()
