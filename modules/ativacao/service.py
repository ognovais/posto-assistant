from modules.ativacao.parser import extrair_dados_ativacao
from modules.ativacao.api import PetroMaxApiClient
from modules.ativacao.validator import parsear_lista_componentes, validar_ativacao

def formatar_cnpj(cnpj_limpo: str) -> str:
    return f"{cnpj_limpo[0:2]}.{cnpj_limpo[2:5]}.{cnpj_limpo[5:8]}/{cnpj_limpo[8:12]}-{cnpj_limpo[12:14]}"

def validar_chamado(texto_chamado: str) -> dict:
    dados = extrair_dados_ativacao(texto_chamado)

    client = PetroMaxApiClient()
    client.renovar_token()
    resposta_api = client.consultar_componentes(dados["cnpj_limpo"])

    componentes_api = parsear_lista_componentes(resposta_api["listaComponente"])
    resultado_validacao = validar_ativacao(dados["componentes"], componentes_api)

    return {
        "razao_social": dados["razao_social"],
        "cnpj": formatar_cnpj(dados["cnpj_limpo"]),
        **resultado_validacao,
    }

def formatar_resultado(resultado: dict) -> str:
    linhas = []
    linhas.append(f"Razão Social: {resultado['razao_social']}")
    linhas.append(f"CNPJ: {resultado['cnpj']}")
    linhas.append("")

    for nome, dados in resultado["componentes"].items():
        linhas.append(nome.upper().replace("_", " "))

        if not dados["encontrado"]:
            linhas.append("  ❌ Componente não encontrado")
        else:
            linhas.append(f"  {'✔' if dados['ativo'] else '❌'} Ativo")
            linhas.append(f"  {'✔' if dados['aceite_painel'] else '❌'} Aceite Painel de Preços")
            linhas.append(f"  {'✔' if dados['aceite_fidelidade'] else '❌'} Aceite Programa Fidelidade")

        linhas.append("")

    if resultado["apto"]:
        linhas.append("Cliente APTO para ativação.")
    else:
        linhas.append("Cliente NÃO apto para ativação.")

    return "\n".join(linhas)




if __name__ == "__main__":
    print("Cole os chamados (um por linha) e aperte Enter duas vezes:")
    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha)

    for linha_chamado in linhas:
        try:
            resultado = validar_chamado(linha_chamado)
            print(formatar_resultado(resultado))
        except Exception as erro:
            print(f"Erro ao validar linha: {linha_chamado}")
            print(f"Motivo: {erro}")

        print("=" * 40)
