import sys, schedule, time
import webbrowser
import pygetwindow as gw
from datetime import datetime

sys.path.append(r'E:/')

import att_bd_margem



def hr_chamada():
    hr = datetime.now()
    hora = hr.strftime('%H:%M')
    print(f' - - - - - - - - - Termino da chamada: {hora}  - - - - - - - - - - ')





def selector_perfil():

    url= r'C:\Users\Fatur\Desktop\Robotic  (Robotic automation processes) - Chrome.lnk'
    webbrowser.open(url)
    time.sleep(5)
    # Encontre a janela do navegador
    browser_window = gw.getWindowsWithTitle('Google Chrome')[0]

    # Maximize a janela
    browser_window.maximize()
    time.sleep(2)


def maximus():
    time.sleep(5)

    try:
        # Encontre a janela do navegador
        mx = gw.getActiveWindow()

        # Maximize a janela
        mx.maximize()

        return mx.title

        
    except:
        print("Erro: ")



@schedule.repeat(schedule.every().day.at("02:30"))
def agendador():

    selector_perfil() 
    att_bd_margem.main_gl()
    att_bd_margem.main_nt()
    hr_chamada()



def agendador_secundario():
   
    
    selector_perfil()   
    att_bd_histo_margem_TODO.main_global()
    hr_chamada()





@schedule.repeat(schedule.every().day.at("04:30"))
def chamada_do_segundario():
    agendador_secundario()


@schedule.repeat(schedule.every().day.at("06:30"))
def chamada_do_segundario():
    agendador_secundario()

@schedule.repeat(schedule.every().day.at("08:30"))
def chamada_do_segundario():
    agendador_secundario()

@schedule.repeat(schedule.every().day.at("10:30"))
def chamada_do_segundario():
    agendador_secundario()

@schedule.repeat(schedule.every().day.at("12:30"))
def chamada_do_segundario():
    agendador_secundario()


@schedule.repeat(schedule.every().day.at("14:30"))
def chamada_do_segundario():
    agendador_secundario()


@schedule.repeat(schedule.every().day.at("16:30"))
def chamada_do_segundario():
    agendador_secundario()


@schedule.repeat(schedule.every().day.at("18:30"))
def chamada_do_segundario():
    agendador_secundario()






if __name__ == '__main__':
    print("start - agendador.py") 

    

    while True:
        schedule.run_pending()
        time.sleep(30)
    


    
