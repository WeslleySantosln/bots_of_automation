# Descrição do Código: Script para Cálculo de Distância e Tempo entre Cidades em uma Planilha Google Sheets

Este script foi desenvolvido para automatizar o cálculo da distância e do tempo de viagem entre cidades em uma planilha do Google Sheets. Ele utiliza a API do Google Maps (`Maps.newDirectionFinder()`) para obter as informações de rota entre um ponto de origem e um ponto de destino, preenchendo automaticamente as colunas correspondentes na planilha.

---

## **Objetivo do Script**
O principal objetivo deste script é:
1. Ler os dados de origem e destino (cidade e estado) de uma planilha.
2. Consultar a API do Google Maps para calcular a distância e o tempo de viagem entre esses pontos.
3. Preencher automaticamente as colunas de distância e tempo na planilha com os valores obtidos.

---

## **Funcionalidades Principais**

### 1. **Estrutura da Planilha**
- A planilha deve estar organizada com as seguintes colunas:
  - **Coluna 1**: Nome da cidade de origem.
  - **Coluna 2**: Estado (UF) da cidade de origem.
  - **Coluna 3**: Nome da cidade de destino.
  - **Coluna 4**: Estado (UF) da cidade de destino.
  - **Coluna 5**: Distância (em km) – será preenchida pelo script.
  - **Coluna 6**: Tempo de viagem – será preenchida pelo script.

---

### 2. **Fluxo de Execução**
1. **Inicialização**:
   - O script acessa a planilha ativa usando `SpreadsheetApp.getActiveSpreadsheet()` e identifica a aba ativa (`getActiveSheet()`).
   - Define as variáveis iniciais:
     - `Inicio`: Linha inicial dos dados (ex.: linha 2).
     - `colDistancia`: Coluna onde a distância será armazenada (coluna 5).
     - `colTempo`: Coluna onde o tempo será armazenado (coluna 6).

2. **Iteração pelas Linhas**:
   - O script percorre todas as linhas da planilha, começando na linha definida por `Inicio` até a última linha com dados (`getLastRow()`).
   - Para cada linha, verifica se as células de distância e tempo estão vazias. Se estiverem, o script prossegue para calcular os valores.

3. **Consulta à API do Google Maps**:
   - O script monta a origem e o destino concatenando os valores das colunas de cidade e estado.
   - Utiliza a classe `Maps.newDirectionFinder()` para criar um objeto de direções e define a origem e o destino.
   - Chama o método `getDirections()` para obter as informações de rota.

4. **Preenchimento das Colunas**:
   - Se a API retornar resultados válidos:
     - Extrai a distância em quilômetros (`distance.value / 1000`).
     - Extrai o tempo de viagem formatado (`duration.text`).
     - Preenche as colunas correspondentes na planilha com os valores calculados.
   - Se ocorrer um erro ou a API não retornar resultados válidos, o script registra o erro no log.

---

### 3. **Tratamento de Erros**
O script inclui tratamento de exceções para lidar com possíveis problemas durante a consulta à API do Google Maps:
- **Erro na API**:
  - Se a API retornar uma resposta inesperada ou falhar, o script registra uma mensagem de erro detalhada no log, incluindo a linha afetada, a origem e o destino.

```javascript
catch (e) {
    Logger.log("Erro ao obter direções para linha " + i + ": " + e.message + ". Origem: " + origem + ", Destino: " + destino);
}
```

---

### 4. **Exemplo de Funcionamento**
Suponha que a planilha contenha os seguintes dados:

| CIDADE ORIGEM | UF ORIGEM | CIDADE DESTINO | UF DESTINO | DISTÂNCIA (KM) | TEMPO DE VIAGEM |
|---------------|-----------|----------------|------------|----------------|-----------------|
| São Paulo     | SP        | Rio de Janeiro | RJ         |                |                 |
| Belo Horizonte| MG        | Brasília       | DF         |                |                 |

Após a execução do script, as colunas de distância e tempo serão preenchidas com os valores calculados:

| CIDADE ORIGEM | UF ORIGEM | CIDADE DESTINO | UF DESTINO | DISTÂNCIA (KM) | TEMPO DE VIAGEM |
|---------------|-----------|----------------|------------|----------------|-----------------|
| São Paulo     | SP        | Rio de Janeiro | RJ         | 429            | 5h 30m          |
| Belo Horizonte| MG        | Brasília       | DF         | 716            | 8h 15m          |

---

## **Detalhes Técnicos**

### 1. **API do Google Maps**
- O script utiliza a classe `Maps.newDirectionFinder()` para consultar a API do Google Maps.
- Os métodos `setOrigin()` e `setDestination()` definem os pontos de origem e destino.
- O método `getDirections()` retorna um objeto JSON contendo as informações da rota, incluindo distância e tempo.

### 2. **Conversão de Unidades**
- A distância retornada pela API está em metros (`distance.value`). O script converte esse valor para quilômetros dividindo por 1000.

### 3. **Verificação de Células Vazias**
- Antes de realizar a consulta, o script verifica se as células de distância e tempo já estão preenchidas. Isso evita consultas desnecessárias e economiza cotas da API.

```javascript
if (distanciaCelula == "" && tempoCelula == "") {
    // Realiza a consulta à API
}
```

---

## **Considerações Finais**
Este script é uma ferramenta poderosa para automatizar o cálculo de distâncias e tempos de viagem em planilhas do Google Sheets. Ele pode ser usado em cenários como:
- Planejamento logístico.
- Cálculo de rotas para entregas.
- Análise de viagens.

### **Limitações**
1. **Cotas da API**:
   - A API do Google Maps tem limites de uso diárias. Certifique-se de monitorar o consumo para evitar bloqueios.
2. **Coordenadas Fixas**:
   - O script depende de nomes de cidades e estados para calcular as rotas. Endereços mal formatados ou ambíguos podem resultar em erros.
3. **Resolução de Tela**:
   - O script não funciona em ambientes onde a API do Google Maps não está disponível ou configurada corretamente.

