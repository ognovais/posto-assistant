import os

def gerar_assunto(dados: dict) -> str:
    return f"TechPosto Sistemas - Solicitação de Carga Full SGA {dados['ID_SISTEMA']}"

def gerar_corpo(dados: dict) -> str:
    caminho_template = os.path.join(os.path.dirname(__file__), "..", "templates", "carga_full_sga.txt")
    with open(caminho_template, "r", encoding="utf-8") as arquivo:
        template = arquivo.read()

    valores = {
        "ID_SISTEMA": dados["ID_SISTEMA"],
        "CNPJ": dados["CNPJ"],
        "RAZAO": dados["Razão Social"],
        "NOME": dados["Nome do Cliente"],
        "TELEFONE": dados["Telefone"],
        "EMAIL": dados["E-mail"],
        "DATA": dados["Data da implantação"],
    }

    corpo = template.format(**valores)
    return corpo
