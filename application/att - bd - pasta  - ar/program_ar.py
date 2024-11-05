import pyautogui #automação
from time import sleep, time #Tempo de Espera
import webbrowser, os #Browser e Pasta de Arquivo
import ctypes #Desligar numlook
import schedule
from schedule import repeat, every
from datetime import datetime
import pygetwindow as gw


pyautogui.PAUSE = 3 # Tempo de espera do pyautogui de uma ação e outra

#Método para as coordenadas funcionar em todos os tamanhos de resolução
width_atual, height_atual = pyautogui.size()
dif_width = 1 - ((1919 - (width_atual - 1)) / (width_atual - 1))
dif_height = 1 - ((1079 - (height_atual - 1)) / (height_atual - 1))


def apagar_pst_donwload():
    #Apagar os itens na pasta de Donwload
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads') #Abrir Pasta Download
    os.startfile(downloads_folder) #Abrir Pasta Donwload
    maximus()
    pyautogui.click(1000 * dif_width,500 * dif_height,duration=1) #Click na pasta
    pyautogui.hotkey('ctrl', 'a')   
    pyautogui.hotkey('delete')    


def maximus():
    sleep(5)

    try:
        # Encontre a janela do navegador
        mx = gw.getActiveWindow()

        # Maximize a janela
        mx.maximize()

        return mx.title

        
    except:
        print("Erro: ")


def login_sistemas():

    #Abrir o navegador padrão no site do x Sistemas 
    url="https://google.com.br/"
    webbrowser.open(url)
    sleep(20)
    maximus()
    
    
    pyautogui.click(1415 * dif_width, 687 * dif_height)#Login
    sleep(5)
    pyautogui.click(1396 * dif_width, 706 * dif_height)
    sleep(5)


def login_sistemasB():

    #Abrir o navegador padrão do sistemaB
    url="https://google.com.br/"
    webbrowser.open(url)
    sleep(20)
    maximus()
    
    pyautogui.click(1415 * dif_width, 687 * dif_height)#Login
    sleep(5)
    pyautogui.click(1414 * dif_width, 765 * dif_height)
    sleep(5)
   

def extracao_relatorio_x():

    sleep(10)
    #Extração do Relatorios
    pyautogui.click(1001 * dif_width,316 * dif_height,duration=1)
    sleep(10)
    pyautogui.click(110 * dif_width,441 * dif_height,duration=1)
    sleep(10)

    pyautogui.press('tab', presses=2)
    pyautogui.write('01/01/2010')
    pyautogui.press('tab')
    pyautogui.write('01/01/2050')
    pyautogui.press('tab', presses=9)#Gerar relatorio
    pyautogui.press('enter')
    sleep(60)



def extracao_relatorio_b():
    sleep(10)
    pyautogui.click(1001 * dif_width,316 * dif_height,duration=1)#Relatorios Personalizados
    sleep(10)
    pyautogui.click(144 * dif_width,414 * dif_height,duration=1)#
    sleep(10)
    
    pyautogui.press('tab', presses=2)
    pyautogui.write('01/01/2010')
    pyautogui.press('tab')
    pyautogui.write('01/01/2050')
    pyautogui.press('tab', presses=3)#Gerar relatorio
    pyautogui.press('enter')
    sleep(60)



def movimento():
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads') #Abrir Pasta Download
    os.startfile(downloads_folder) #Abrir Pasta Donwload
    sleep(5)
    maximus()
    pyautogui.click(1000 * dif_width,500 * dif_height,duration=1) #Click na pasta
    pyautogui.hotkey('ctrl', 'a')   
    pyautogui.hotkey('ctrl', 'c')    
    
    
    pst_ar_folder = os.path.join(os.path.expanduser('~'), r'E:/ar') #Abrir a pasta ar
    os.startfile(pst_ar_folder) #Abrir a pasta ar
    sleep(5)
    maximus()
    pyautogui.hotkey('ctrl', 'v')   
    pyautogui.hotkey('ctrl', 'enter')    


   

def saida_sistema():
    #Abrir o navegador padrão no site do x Sistemas 
    url="https://google.com.br/"
    webbrowser.open(url)
    sleep(10)

    #Saida do sistema
    pyautogui.click(1902 * dif_width,992 * dif_height,duration=2)
    sleep(3)
    pyautogui.click(1279 * dif_width,448 * dif_height,duration=2)
    sleep(3)
    pyautogui.click(1281 * dif_width,411 * dif_height,duration=2)
    sleep(3)
     


def main_x():
    
    apagar_pst_donwload()
    
    login_sistemas()
    
    #Pagina para baixar o relatorio
    url="https://google.com.br"
    webbrowser.open(url)
    sleep(20)

    extracao_relatorio_x()
    (20)

    saida_sistema()
    
    
def main_b():
    
    login_sistemasB()
    
    #Pagina para baixar o relatorio
    url="https://google.com.br"
    webbrowser.open(url)
    sleep(20)

    extracao_relatorio_b()
    sleep(20)

    saida_sistema()


def fechar_janelas():
    for i in range(4):
        pyautogui.click(1890 * dif_width,27 * dif_height,duration=2)#Fechar Janelas que estão abertas
        sleep(2)

#Repetir todos os dias as 09:00 horas AM
@repeat(every().day.at("09:00"))
def chamada_agendada():
    main_x()
    main_b()
    movimento()


if __name__ == '__main__':
    
    chamada_agendada()

    while True:
        schedule.run_pending()
        sleep(10)
        
