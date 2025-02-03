# Descrição do Código: Script de Verificação e Alerta em Planilhas Google Sheets

Este script foi desenvolvido para monitorar uma planilha do Google Sheets e enviar alertas por e-mail sempre que determinadas condições forem atendidas. Ele é especialmente útil para identificar possíveis erros ou situações críticas em contratos, como valores inconsistentes, campos vazios ou valores acima de um limite específico. Abaixo está uma descrição detalhada do funcionamento do código.

---

## **Objetivo do Script**
O script verifica se certas colunas na planilha contêm a palavra `"SIM"`. Essas colunas representam funções que validam os dados dos contratos. Quando uma inconsistência é encontrada (indicada pela presença de `"SIM"`), o script envia um e-mail de alerta para uma equipe responsável e registra a linha correspondente em outra aba da planilha para evitar notificações duplicadas.

---

## **Funcionalidades Principais**

### 1. **Verificação de Dados**
- O script lê os dados da aba principal (`MAIN`) da planilha e verifica as seguintes colunas:
  - Coluna 23 (índice 22): Verifica se o valor do contrato de pagamento é maior que o valor de recebimento pelo cliente.
  - Coluna 24 (índice 23): Verifica se o valor da nota fiscal é acima de um limite específico (ex.: 1 milhão).
  - Coluna 25 (índice 24): Verifica se um campo obrigatório está vazio.

Se qualquer uma dessas colunas contiver a palavra `"SIM"`, significa que há um problema no contrato correspondente.

---

### 2. **Envio de E-mails de Alerta**
- Quando um problema é identificado, o script envia um e-mail para o endereço `alertaemissao@.com.br` com as seguintes informações:
  - **Assunto**: Contém o número do contrato e o tipo de problema encontrado.
    ```
    Exemplo: "Alerta: o contrato de N° 12345 está com o seguinte indicativo: Valor acima do limite"
    ```
  - **Corpo do e-mail**: Fornece mais detalhes sobre o problema, incluindo:
    - O tipo de problema encontrado.
    - O número do contrato.
    - O nome da pessoa que lançou o contrato.
    ```
    Exemplo: "O seguinte problema foi encontrado: Valor acima do limite, no contrato de N° 12345, foi lançado Por João Silva, Por favor, verifique!"
    ```

---

### 3. **Registro de Linhas Processadas**
- Para evitar o envio de e-mails duplicados, o script registra as linhas já processadas em uma aba separada chamada `JA_INFORMADO`.
- Os valores da linha são convertidos em strings (com apóstrofo inicial) para evitar problemas de formatação automática do Google Sheets.

---

### 4. **Fluxo de Execução**
1. **Abertura da Planilha**:
   - O script acessa a planilha usando o ID fornecido (`spreadsheetId`) e carrega os dados das abas `MAIN` e `JA_INFORMADO`.

2. **Leitura dos Dados**:
   - Os dados da aba `MAIN` são lidos em formato de matriz (`data`), onde cada linha representa um contrato e cada coluna representa um campo específico.

3. **Verificação de Condições**:
   - Para cada linha da planilha, o script verifica se alguma das colunas monitoradas contém `"SIM"`.
   - Se um problema for encontrado, o script gera um e-mail de alerta e registra a linha na aba `JA_INFORMADO`.

4. **Envio de E-mails**:
   - O e-mail é enviado usando a função `MailApp.sendEmail()`.

5. **Registro de Linhas Processadas**:
   - A linha processada é adicionada à aba `JA_INFORMADO` para evitar notificações futuras.

---

## **Detalhes Técnicos**

### 1. **Estrutura da Planilha**
- **Aba `MAIN`**:
  - Contém os dados principais dos contratos.
  - Cada linha representa um contrato, e as colunas monitoradas indicam possíveis problemas.
- **Aba `JA_INFORMADO`**:
  - Armazena as linhas já processadas para evitar e-mails duplicados.

### 2. **Colunas Monitoradas**
As colunas monitoradas estão definidas no array `columnsToCheck`:
```javascript
var columnsToCheck = [
  {index: 22, subject: "Alerta: o contrato de N° %s está com o seguinte indicativo: %s", body: "O seguinte problema foi encontrado: %s , no contrato de N° %s, foi lançado Por %s, Por favor, verifique!"},
  {index: 23, subject: "Alerta: o contrato de N° %s está com o seguinte indicativo: %s", body: "O seguinte problema foi encontrado: %s , no contrato de N° %s, foi lançado Por %s, Por favor, verifique!"},
  {index: 24, subject: "Alerta: o contrato de N° %s está com o seguinte indicativo: %s", body: "O seguinte problema foi encontrado: %s , no contrato de N° %s, foi lançado Por %s, Por favor, verifique!"}
];
```
- **Índices das Colunas**:
  - `22`: Verifica inconsistências no valor do contrato.
  - `23`: Verifica notas fiscais acima de um limite.
  - `24`: Verifica campos obrigatórios vazios.

### 3. **Função `checkIfRowExists`**
- Esta função (não mostrada no código) verifica se uma linha específica já foi registrada na aba `JA_INFORMADO`. Se sim, o script pula essa linha para evitar e-mails duplicados.

---

## **Exemplo de Uso**
Suponha que a planilha contenha os seguintes dados na aba `MAIN`:

| Contrato | Valor Pagamento | Valor Recebimento |Campor Obrigatorio| Valor NF incompativel    | Campo Obrigatório  |
|----------|-----------------|-------------------|------------------|--------------------------|--------------------|
| 12345    | 1000            | 800               |    preenchido    |          SIM             |                    |
| 67890    | 2000            | 2000              |                  |                          |       SIM          |

- Para o contrato `12345`, o script identifica que o valor do pagamento é maior que o valor de recebimento e envia um e-mail de alerta.
- Para o contrato `67890`, o script identifica que o campo obrigatório está vazio e também envia um e-mail de alerta.

---

