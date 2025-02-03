import pyautogui, time
import pygetwindow as gw
from datetime import datetime
import app.script_excel_p_sheets as eps
import app.script_gw_p_drive as gwpd



def hr_chamada():
    hr = datetime.now()
    hora = hr.strftime('%H:%M')
    print(f' - - - - - - - - - Termino da chamada: {hora}  - - - - - - - - - - ')


def maximus():
    try:
        # Encontre a janela do navegador
        mx = gw.getActiveWindow()
        # Maximize a janela
        mx.maximize()
        return mx.title
    except:
        print("Erro: ")

def main():
    try:
        gwpd.main()
        eps.main_eps()
        time.sleep(20)
    except Exception as e:
        pyautogui.hotkey('ctrl', 'w')
        pyautogui.hotkey('ctrl', 'w')
        print(f"Erro encontrado: {e}")
        # Continua a execução, mesmo após um erro




    


    
