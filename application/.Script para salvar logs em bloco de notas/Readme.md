# Descrição do Código: Script de Logging e Execução Contínua

Este script foi desenvolvido para executar uma tarefa contínua enquanto registra logs em um arquivo. Ele utiliza uma classe personalizada chamada `Logger` para redirecionar a saída padrão (`stdout`) para um arquivo de log, permitindo que todas as mensagens exibidas no terminal também sejam gravadas em um arquivo. Abaixo está uma descrição detalhada do funcionamento do código.

---

## **Objetivo do Script**
O principal objetivo deste script é:
1. Executar uma tarefa repetidamente (ex.: imprimir "script" no terminal).
2. Registrar todos os logs gerados durante a execução em um arquivo chamado `Log_agendador.log`.
3. Garantir que o script seja interrompido de forma segura pelo usuário ou em caso de erro, fechando corretamente o arquivo de log.

---

## **Funcionalidades Principais**

### 1. **Classe `Logger`**
A classe `Logger` é responsável por redirecionar a saída padrão (`sys.stdout`) para um arquivo de log. Ela implementa os métodos necessários para garantir que as mensagens sejam exibidas tanto no terminal quanto gravadas no arquivo.

#### Métodos da Classe:
- **`__init__(self, filename)`**:
  - Inicializa a classe, abrindo o arquivo de log no modo de anexação (`append`).
  - Armazena a saída padrão original (`sys.stdout`) para continuar exibindo mensagens no terminal.

- **`write(self, message)`**:
  - Escreve a mensagem tanto no terminal quanto no arquivo de log.
  - Chama o método `flush()` para garantir que os dados sejam gravados imediatamente.

- **`flush(self)`**:
  - Força a gravação dos dados no terminal e no arquivo de log.

- **`close(self)`**:
  - Fecha o arquivo de log quando a execução do script termina.

---

### 2. **Redirecionamento da Saída Padrão**
O script redireciona a saída padrão (`sys.stdout`) para uma instância da classe `Logger`. Isso significa que qualquer chamada à função `print()` será registrada no arquivo de log além de ser exibida no terminal.

```python
sys.stdout = Logger("Log_agendador.log")
```

---

### 3. **Execução Contínua**
O script entra em um loop infinito (`while True`) onde imprime continuamente a palavra `"script"` no terminal e no arquivo de log. Esse loop simula uma tarefa contínua que pode ser usada para monitorar ou processar algo repetidamente.

```python
while True:
    print("script")
```

---

### 4. **Tratamento de Exceções**
O script inclui tratamento de exceções para lidar com possíveis interrupções ou erros durante a execução:

#### a) **Interrupção pelo Usuário**
Se o usuário interromper o script pressionando `Ctrl+C`, o bloco `except KeyboardInterrupt` captura essa ação e exibe uma mensagem informando que a execução foi interrompida.

```python
except KeyboardInterrupt:
    print("interrompido pelo usuário.")
```

#### b) **Erros Fatais**
Se ocorrer qualquer outro erro durante a execução, o bloco `except Exception as e` captura a exceção e registra uma mensagem de erro fatal no log.

```python
except Exception as e:
    print(f"Erro fatal: {e}")
```

#### c) **Fechamento Seguro do Log**
Independentemente de como o script termina (interrupção pelo usuário ou erro), o bloco `finally` garante que o arquivo de log seja fechado corretamente.

```python
finally:
    sys.stdout.close()
```

---

## **Fluxo de Execução**
1. **Inicialização**:
   - O script redireciona a saída padrão para a classe `Logger`, que começa a registrar todas as mensagens no arquivo `Log_agendador.log`.

2. **Loop Infinito**:
   - O script entra em um loop infinito, imprimindo a palavra `"script"` no terminal e no arquivo de log.

3. **Interrupção ou Erro**:
   - Se o usuário interromper o script pressionando `Ctrl+C`, uma mensagem de interrupção é registrada no log.
   - Se ocorrer um erro inesperado, uma mensagem de erro fatal é registrada no log.

4. **Encerramento**:
   - O arquivo de log é fechado no bloco `finally`, garantindo que todos os dados sejam salvos corretamente.

---

## **Exemplo de Saída no Arquivo de Log**
Suponha que o script seja executado e interrompido após alguns segundos. O conteúdo do arquivo `Log_agendador.log` seria semelhante ao seguinte:

```
script
script
script
interrompido pelo usuário.
```

---
