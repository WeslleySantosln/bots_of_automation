# Descrição do Código: Script de Automação para Extração de Relatórios e Movimentação de Arquivos

Este script foi desenvolvido para automatizar a extração de relatórios de um sistema web (GW Sistemas) e movê-los para uma pasta específica no computador. Ele utiliza a biblioteca `pyautogui` para simular interações com a interface gráfica, como cliques e pressionamentos de teclas, além de outras bibliotecas para manipular arquivos e gerenciar datas. Abaixo está uma descrição detalhada do funcionamento do código.

---

## **Objetivo do Script**
O principal objetivo deste script é:
1. Acessar o sistema GW Sistemas e realizar login em duas empresas diferentes (`GL` e `NF`).
2. Extrair relatórios específicos com base em um intervalo de datas.
3. Mover os arquivos baixados para uma pasta designada.
4. Encerrar o processo de forma segura, fechando todas as janelas abertas.

---

## **Funcionalidades Principais**

### 1. **Configuração Inicial**
- **Tempo de Espera**:
  - O script define um tempo de espera padrão entre as ações usando `pyautogui.PAUSE = 2`. Isso garante que cada ação tenha tempo suficiente para ser concluída antes da próxima.

- **Definição de Datas**:
  - As variáveis `data_de` e `data_ate` são usadas para definir o intervalo de datas dos relatórios. A função `att_data()` ajusta essas datas para um valor fixo (`01/12/2023`) para `data_de` e para o dia anterior ao atual para `data_ate`.

```python
def att_data():
    global data, data_de, data_ate
    data_de = '01/12/2023'
    data = date.today() - timedelta(1)
    data_ate = data.strftime('%d/%m/%Y')
```

---

### 2. **Desligar Num Lock**
A função `desligar_numlock()` desativa o Num Lock para permitir que o `pyautogui` selecione células em planilhas sem problemas. Isso é útil em sistemas onde o Num Lock pode interferir nas interações automatizadas.

```python
def desligar_numlock():
    user32 = ctypes.windll.user32
    VK_NUMLOCK = 0x90
    if user32.GetKeyState(VK_NUMLOCK) & 1:
        print("Num Lock está ativado")
        pyautogui.press("numlock")
```

---

### 3. **Maximização de Janelas**
A função `maximus()` maximiza a janela ativa para garantir que as interações automatizadas ocorram corretamente. Ela usa a biblioteca `pygetwindow` para localizar e maximizar a janela.

```python
def maximus():
    sleep(5)
    try:
        mx = gw.getActiveWindow()
        mx.maximize()
        return mx.title
    except Exception as e:
        print(f"Erro ao maximizar a janela: {e}")
```

---

### 4. **Limpeza da Pasta de Downloads**
A função `apagar_pst_download()` limpa a pasta de Downloads para evitar conflitos com arquivos antigos. Ela abre a pasta, seleciona todos os arquivos e os exclui.

```python
def apagar_pst_download():
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    os.startfile(downloads_folder)
    maximus()
    pyautogui.click(1000, 500, duration=1)
    pyautogui.hotkey('ctrl', 'a')   
    pyautogui.hotkey('delete') 
    sleep(10)
```

---

### 5. **Login no Sistema GW**
As funções `login_gl()` e `login_nf()` realizam o login no sistema GW Sistemas para duas empresas diferentes (`GL` e `NF`). Elas simulam cliques nos botões e campos de login.

```python
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
```

---

### 6. **Extração de Relatórios**
As funções `extracao_relatorio_gl()` e `extracao_relatorio_nf()` extraem relatórios específicos (`N_06_DESPESAS_PAGAS_-_WS` e `N_07_DESPESAS_PAGAS_-_WS_`) com base no intervalo de datas definido. Elas navegam até a página de histórico, preenchem os campos de data e iniciam o download.

```python
def extracao_relatorio_gl():
    att_data()
    guia_historico_personalizado()
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
```

---

### 7. **Movimentação de Arquivos**
A função `movimento_colar_pst()` move os arquivos baixados da pasta de Downloads para uma pasta específica (`E:br`). Ela copia os arquivos e cola-os na pasta de destino.

```python
def movimento_colar_pst():
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
```

---

### 8. **Encerramento do Sistema**
As funções `saida_sistema()` e `fechar_janelas()` encerram o sistema e fecham todas as janelas abertas. Elas simulam cliques nos botões de saída e fechamento.

```python
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
```

---

### 9. **Fluxo Principal**
A função `main()` coordena a execução de todas as etapas:
1. Limpa a pasta de Downloads.
2. Realiza o login na empresa `GL` e extrai o relatório correspondente.
3. Sai do sistema.
4. Repete o processo para a empresa `NF`.
5. Move os arquivos baixados para a pasta de destino.
6. Fecha todas as janelas abertas.

```python
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
```

---

