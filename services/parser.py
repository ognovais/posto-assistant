import re

def extrair_dados(texto: str) -> dict:
    campos = {
    "ID_SISTEMA": r"ID_SISTEMA:\s*(.+?)(?=\s*(?:CNPJ:|Razão Social:|Nome do Cliente:|Telefone:|E-mail:|Data da implantação:|$))",
    "CNPJ": r"CNPJ:\s*(.+?)(?=\s*(?:ID_SISTEMA:|Razão Social:|Nome do Cliente:|Telefone:|E-mail:|Data da implantação:|$))",
    "Razão Social": r"Razão Social:\s*(.+?)(?=\s*(?:ID_SISTEMA:|CNPJ:|Nome do Cliente:|Telefone:|E-mail:|Data da implantação:|$))",
    "Nome do Cliente": r"Nome do Cliente:\s*(.+?)(?=\s*(?:ID_SISTEMA:|CNPJ:|Razão Social:|Telefone:|E-mail:|Data da implantação:|$))",
    "Telefone": r"Telefone:\s*(.+?)(?=\s*(?:ID_SISTEMA:|CNPJ:|Razão Social:|Nome do Cliente:|E-mail:|Data da implantação:|$))",
    "E-mail": r"E-mail:\s*(.+?)(?=\s*(?:ID_SISTEMA:|CNPJ:|Razão Social:|Nome do Cliente:|Telefone:|Data da implantação:|$))",
    "Data da implantação": r"Data da implantação:\s*(.+?)(?=\s*(?:ID_SISTEMA:|CNPJ:|Razão Social:|Nome do Cliente:|Telefone:|E-mail:|$))",
    }

    dados = {}
    for nome_campo, padrao in campos.items():
        resultado = re.search(padrao, texto)
        if resultado:
            dados[nome_campo] = resultado.group(1).strip()
        else:
            dados[nome_campo] = None

    return dados

def validar_dados(dados: dict) -> list:
    campos_faltando = []
    for nome_campo, valor in dados.items():
        if valor is None:
            campos_faltando.append(nome_campo)

    return campos_faltando

def formatar_erros(campo_faltando: list) -> list:
    erros=[]
    for nome_campo in campo_faltando:
        erros.append(f'❌ Campo "{nome_campo}" não encontrado.')

    return erros
