import pyautogui
from time import sleep
import webbrowser
import os
import ctypes
from datetime import date, timedelta
import pygetwindow as gw

# Tempo de espera entre uma ação e outra
pyautogui.PAUSE = 2

# Definição de data para iniciação de Variável
data = date.today()
data_de = data.strftime('%d/%m/%Y')
data_ate = data.strftime('%d/%m/%Y')


def att_data():
    global data, data_de, data_ate
    
    data_de = '01/12/2023'
    
    data = date.today() - timedelta(1)
    data_ate = data.strftime('%d/%m/%Y')

# Função para desligar o Numlock e permitir o pyautogui selecionar as células nas planilhas
def desligar_numlock():
    user32 = ctypes.windll.user32
    VK_NUMLOCK = 0x90

    if user32.GetKeyState(VK_NUMLOCK) & 1:
        print("Num Lock está ativado")
        pyautogui.press("numlock")


# Código em teste
# Ajustar coordenadas para funcionar em todos os tamanhos de resolução
width_atual, height_atual = pyautogui.size()
dif_width = width_atual / 1920
dif_height = height_atual / 1080
print(dif_width, dif_height)

# Função para maximizar a tela atual
def maximus():
    sleep(5)
    try:
        mx = gw.getActiveWindow()
        mx.maximize()
        return mx.title
    except Exception as e:
        print(f"Erro ao maximizar a janela: {e}")

# Apagar os itens na pasta de Downloads para garantir a abertura dos itens novos
def apagar_pst_download():
    sleep(5)
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    os.startfile(downloads_folder)
    maximus()
    pyautogui.click(1000, 500, duration=1)
    pyautogui.hotkey('ctrl', 'a')   
    pyautogui.hotkey('delete') 
    sleep(10)

# Abrir o navegador padrão no site do GW Sistemas
def abrir_pagina_login():
    url = "https://webtrans.saas.gwsistemas.com.br/"
    webbrowser.open(url)
    sleep(20)
    maximus()

# Movimento de clicks na tela, login na empresa gl
def login_gl():
    abrir_pagina_login()
    sleep(10)
    pyautogui.click(1415, 687)
    sleep(10)
    pyautogui.click(1396, 706)
    sleep(10)
    pyautogui.click(942, 838)
    sleep(10)
    pyautogui.click(1283, 446)
    sleep(10)

# Movimento de clicks na tela, login na empresa NF
def login_nf():
    abrir_pagina_login()
    sleep(10)
    pyautogui.click(1415, 687)
    sleep(10)
    pyautogui.click(1414, 765)
    sleep(10)
    pyautogui.click(942, 838)
    sleep(10)
    pyautogui.click(1283, 446)
    sleep(10)

# Abrir a guia Histórico e clicar na guia personalizado
def guia_historico_personalizado():
    url = "https://webtrans.saas.gwsistemas.com.br/relhistorico.jsp?acao=iniciar&modulo=webtrans"
    webbrowser.open(url)
    sleep(20)
    maximus()
    pyautogui.click(961, 316, duration=2)
    sleep(10)

# Extração do relatório: xy
def extracao_relatorio_gl():
    att_data()
    guia_historico_personalizado()

    # Primeiro relatório
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('N_06_DESPESAS_PAGAS_-_WS')
    pyautogui.press('esc')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('space')
    sleep(15)
    pyautogui.press('tab', presses=2)
    pyautogui.write(data_de)
    pyautogui.press('tab')
    pyautogui.write(data_ate)
    pyautogui.press('tab', presses=3)
    pyautogui.press('enter')
    sleep(20)



# Extração do relatório: xy - WS na empresa nf
def extracao_relatorio_nf():
    att_data()
    guia_historico_personalizado()

    # Primeiro relatório
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('N_07_DESPESAS_PAGAS_-_WS_')
    pyautogui.press('esc')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('space')
    sleep(15)
    pyautogui.press('tab', presses=2)
    pyautogui.write(data_de)
    pyautogui.press('tab')
    pyautogui.write(data_ate)
    pyautogui.press('tab', presses=3)
    pyautogui.press('enter')
    sleep(20)

    
# Movimento de colar na pasta
def movimento_colar_pst():
    sleep(5)
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    os.startfile(downloads_folder)
    maximus()
    pyautogui.click(1000, 500, duration=1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    sleep(10)

    pst_br = os.path.join(os.path.expanduser('~'), r'E:br')
    os.startfile(pst_br)
    sleep(10)
    maximus()
    pyautogui.hotkey('ctrl', 'v')
    sleep(5)
    pyautogui.hotkey('enter')
    sleep(10)

# Saída do sistema
def saida_sistema():
    url = "https://webtrans.saas.gwsistemas.com.br/"
    webbrowser.open(url)
    sleep(10)

    pyautogui.click(1902, 992, duration=2)
    sleep(3)
    pyautogui.click(1279, 448, duration=2)
    sleep(3)
    pyautogui.click(1281, 411, duration=2)
    sleep(3)

def fechar_janelas():
    for i in range(7):
        pyautogui.click(1890, 27, duration=2)
        sleep(2)

def main():

    apagar_pst_download()
    login_gl()
    extracao_relatorio_gl()
    saida_sistema()
    login_nf()
    extracao_relatorio_nf()
    saida_sistema()
    movimento_colar_pst()
    fechar_janelas()



if __name__ == '__main__':
    main()
