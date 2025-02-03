# Descrição do Código: Script de Automação para Extração e Atualização de Dados

Este repositório contém um script Python projetado para automatizar a extração de dados de um sistema web (GW Sistemas) e atualizá-los em planilhas do Google Sheets. O código foi desenvolvido para ser executado em um ambiente controlado, garantindo que os dados sejam processados e organizados de forma eficiente.

## Funcionalidades Principais

### 1. **Importação de Módulos**
O script utiliza bibliotecas como `pyautogui`, `pygetwindow`, `datetime`, e módulos personalizados (`app.script_excel_p_sheets` e `app.script_gw_p_drive`) para realizar as seguintes tarefas:
- Automatizar interações com interfaces gráficas.
- Manipular janelas do navegador.
- Gerenciar datas e horários.
- Extrair dados de relatórios e atualizá-los em planilhas do Google Sheets.

---

### 2. **Função `hr_chamada`**
A função `hr_chamada` registra o horário de término de uma chamada ou processo. Ela utiliza a biblioteca `datetime` para capturar a hora atual e exibi-la no formato `HH:MM`. Essa função é útil para monitorar o progresso do script e identificar possíveis gargalos durante a execução.

**Exemplo de Saída:**
```
 - - - - - - - - - Termino da chamada: 14:30  - - - - - - - - - -
```

---

### 3. **Função `maximus`**
A função `maximus` maximiza a janela ativa do navegador para garantir que as interações automatizadas ocorram corretamente. Ela utiliza a biblioteca `pygetwindow` para localizar a janela ativa e aplicar o método `maximize()`. Caso ocorra algum erro durante o processo, uma mensagem de erro será exibida.

**Propósito:**
- Garantir que a interface gráfica esteja do tamanho adequado para as coordenadas de interação.

---

### 4. **Função `main`**
A função `main` é o núcleo do script e coordena a execução de duas operações principais:
1. **Extração de Dados do GW Sistemas**:
   - A função `gwpd.main()` (importada do módulo `app.script_gw_p_drive`) é responsável por:
     - Acessar o sistema web do GW Sistemas.
     - Realizar o login em diferentes empresas.
     - Extrair relatórios específicos (`N_09_BD_ALE_EMI_CTE` e `N_09_BD_ALE_EMI_CTE_NT`).
     - Salvar os relatórios em uma pasta local.

2. **Atualização de Planilhas do Google Sheets**:
   - A função `eps.main_eps()` (importada do módulo `app.script_excel_p_sheets`) é responsável por:
     - Ler os dados dos relatórios salvos.
     - Atualizar as informações em planilhas do Google Sheets.
     - Adicionar uma coluna "EMPRESA" para identificar a origem dos dados.

**Tratamento de Erros:**
- Caso ocorra algum erro durante a execução, o script fecha as janelas abertas usando `pyautogui.hotkey('ctrl', 'w')` e continua a execução. Isso garante que o processo não seja interrompido abruptamente.

---

### 5. **Fluxo de Execução**
O fluxo geral do script pode ser resumido nos seguintes passos:
1. **Inicialização**:
   - O script começa chamando a função `main()`.

2. **Extração de Dados**:
   - A função `gwpd.main()` realiza o login no sistema GW Sistemas, extrai os relatórios necessários e salva-os em uma pasta local.

3. **Atualização de Planilhas**:
   - A função `eps.main_eps()` lê os dados dos relatórios salvos e atualiza as planilhas do Google Sheets com as informações mais recentes.

4. **Monitoramento**:
   - A função `hr_chamada()` registra o horário de término do processo para facilitar o acompanhamento.

---

### 6. **Considerações Finais**
Este script foi desenvolvido para otimizar a extração e atualização de dados, reduzindo a necessidade de intervenção manual. Ele é especialmente útil em cenários onde os dados precisam ser atualizados diariamente ou em intervalos regulares.

**Pontos Importantes:**
- Certifique-se de que as credenciais de acesso ao sistema GW Sistemas e ao Google Sheets estejam configuradas corretamente.
- Execute o script em um ambiente controlado para evitar interferências externas.
- Monitore os logs gerados para identificar possíveis erros ou falhas.

---

### Exemplo de Uso
Para executar o script, basta chamar a função `main()`:

```python
if __name__ == "__main__":
    main()
```

---

### Observações
- Este script foi projetado para funcionar em um ambiente específico. Alterações nas coordenadas de cliques (`pyautogui.click`) ou na estrutura das pastas podem ser necessárias para adaptá-lo a outros ambientes.
- Certifique-se de que os arquivos manipulados (`N_09_BD_ALE_EMI_CTE`, `N_09_BD_ALE_EMI_CTE_NT`) não contenham informações sensíveis antes de compartilhar ou processá-los.

---

Com este script, você poderá automatizar processos repetitivos e garantir que seus dados estejam sempre atualizados e organizados.
