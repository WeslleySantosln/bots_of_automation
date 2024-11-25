import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging

# Configurações do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuração de credenciais e escopo
def autenticar_google_sheets(json_path, scope):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
    return gspread.authorize(credentials)

# Variável para o escopo de autenticação
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Colunas selecionadas para importação
COLUNAS_SELECIONADAS = []

def atualizar_planilha(client, spreadsheet_id, sheet_name, excel_path, empresa):
    """
    Atualiza uma planilha do Google Sheets com dados de um arquivo Excel.
    """
    # Abrir a planilha e worksheet pelo ID e nome da aba
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)

    # Carregar dados do Excel
    df = pd.read_excel(excel_path, header=1)
    #df = df[COLUNAS_SELECIONADAS]
    #df = df[df['Descrição Unidade de Custo'] == 'COMERCIAL']


    # Adiciona a coluna "EMPRESA"
    df['EMPRESA'] = empresa
    
    # Converte todos os dados para string
    df = df.astype(str)  

    # Prepara os dados para inserir no Google Sheets
    data = [df.columns.values.tolist()] + df.values.tolist()

    # Atualiza os dados na planilha
    sheet.clear()
    sheet.update(data, "A1")

    logging.info(f"Dados atualizados com sucesso para a aba {sheet_name}.")

def main_eps():

    # Caminho para o arquivo de credenciais
    JSON_PATH = r'E:\.json\arquivo.json'

    # Credenciais e cliente do Google Sheets
    client = autenticar_google_sheets(JSON_PATH, SCOPE)

    # Atualizar cada planilha individualmente
    atualizar_planilha(
        client, 
        'id_planilha', 
        'aba_name', 
        r'E:\.data\N_09_BD_ALE_EMI_CTE.xlsx',
        'acrescentar_coluna_com_nome_da_empresa'
    )

    atualizar_planilha(
        client, 
        'id_planilha_shets', 
        'aba_name', 
        r'E:\.data\N_09_BD_ALE_EMI_CTE_NT.xlsx',
        'acrescentar_coluna_com_nome_da_empresa'
    )





    logging.info("Atualização das planilhas concluída.")


