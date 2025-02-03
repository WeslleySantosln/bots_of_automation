import pyautogui
from time import sleep
import webbrowser
import os
from datetime import date, timedelta
import pygetwindow as gw
import shutil


# Definição de data para iniciação de Variável
data = date.today()
data_de = data.strftime('%d/%m/%Y')
data_ate = data.strftime('%d/%m/%Y')

# Método para garantir a atualização da data quando o script estiver rodando
def att_data():
    global data, data_de, data_ate
    
    data = date.today() - timedelta(3)
    data_de = data.strftime('%d/%m/%Y')
    
    data = date.today()
    data_ate = data.strftime('%d/%m/%Y')


# Função para maximizar a tela atual
def maximus():
    sleep(5)
    try:
        mx = gw.getActiveWindow()
        mx.maximize()
        return mx.title
    except Exception as e:
        print(f"Erro ao maximizar a janela: {e}")

# Apagar os itens na pasta de Downloads para garantir dowload de itens com o nome original
def apagar_pst_download():
    sleep(5)
    # Definir o caminho da pasta Downloads
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    
    # Verificar se a pasta existe
    if os.path.exists(downloads_folder):
        # Apagar todo o conteúdo da pasta
        for filename in os.listdir(downloads_folder):
            file_path = os.path.join(downloads_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)  # Remove arquivos e links
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove pastas e seu conteúdo
                print("Pasta de downloads limpa.")
            except Exception as e:
                print(f'Erro ao tentar apagar {file_path}. Detalhes: {e}')
    else:
        print(f'A pasta {downloads_folder} não existe.')



# Abrir o navegador padrão no site do GW Sistemas
def abrir_pagina_login():
    url = "https://webtrans.saas.gwsistemas.com.br/"
    webbrowser.open(url)
    sleep(20)
    maximus()

# Movimento de clicks na tela, login na empresa 
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

# Movimento de clicks na tela, login na empresa
def login_nt():
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

# Abrir a guia Histórico
def guia_historico_personalizado():
    url = "https://webtrans.saas.gwsistemas.com.br/relhistorico.jsp?acao=iniciar&modulo=webtrans"
    webbrowser.open(url)
    sleep(20)
    maximus()
    pyautogui.click(961, 316, duration=2)
    sleep(10)

# Extração do relatório: N_09_BD_ALE_EMI_CTE

def extracao_relatorio_gl():
    att_data()
    guia_historico_personalizado()

    # Primeiro relatório
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('N_09_BD_ALE_EMI_CTE')
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



def extracao_relatorio_nt():
    att_data()
    guia_historico_personalizado()

    # Segundo relatório
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write('N_09_BD_ALE_EMI_CTE_NT')
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
    # Definir pastas
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    pst_data = os.path.join(os.path.expanduser('~'), r'E:\data')
    
    
    # Nomes dos arquivos que devem ser copiados
    arquivos_permitidos = ["N_09_BD_ALE_EMI_CTE", "N_09_BD_ALE_EMI_CTE_NT"]

    try:
        # Verificar se a pasta de destino existe, senão, retorna
        if not os.path.exists(pst_data):
            print(f"Pasta de destino {pst_data} não existe.")
            return

        # Verificar e copiar os arquivos permitidos
        for file_name in os.listdir(downloads_folder):
            full_file_name = os.path.join(downloads_folder, file_name)
            file_name_without_ext = os.path.splitext(file_name)[0]  # Remove a extensão do arquivo
            
            # Verificar se o arquivo é permitido
            if file_name_without_ext in arquivos_permitidos and os.path.isfile(full_file_name):
                shutil.copy(full_file_name, pst_data)  # Copia o arquivo para a pasta destino
                print(f"Arquivo {file_name} copiado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro ao copiar os arquivos: {e}")

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

    login_nt()
    extracao_relatorio_nt()
    saida_sistema()

    movimento_colar_pst()
    fechar_janelas()





