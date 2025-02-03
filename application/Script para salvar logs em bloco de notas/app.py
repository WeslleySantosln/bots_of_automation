import sys

# Logger para registrar logs em arquivo
class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log_file = open(filename, 'a')
    
    def write(self, message):
        self.terminal.write(message)
        self.log_file.write(message)
        self.flush()
    
    def flush(self):
        self.terminal.flush()
        self.log_file.flush()
    
    def close(self):
        self.log_file.close()

sys.stdout = Logger("Log_agendador.log")


if __name__ == "__main__":
    try:

        while True:
            print("script")

    except KeyboardInterrupt:
        print("interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro fatal: {e}")
    finally:
        sys.stdout.close()