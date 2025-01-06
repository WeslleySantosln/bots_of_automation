import sys
import time

class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout  # Para imprimir no terminal
        self.log_file = open(filename, 'a')  # Para salvar no arquivo
    
    def write(self, message):
        self.terminal.write(message)  # Imprimir no terminal
        self.log_file.write(message)  # Escrever no arquivo
    
    def flush(self):
        self.terminal.flush()
        self.log_file.flush()

# Redirecionar stdout e stderr para o logger
sys.stdout = Logger('meu_log_completo.log')


# Código com prints e exceções
print("Este é um log visível no terminal e salvo no arquivo.")
