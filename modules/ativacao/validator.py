def parsear_componente(item: dict) -> dict:
    situacao = item["situacao"]
    ativo = situacao == "A"

    aceite_painel = False
    aceite_fidelidade = False

    for aceite in item["aceites"]:
        if aceite["nome"] == "aceitePainelPrecos":
            aceite_painel = aceite["status"]
        if aceite["nome"] == "aceiteProgramaFidelidade":
            aceite_fidelidade = aceite["status"]

    return {
        "ativo": ativo,
        "aceite_painel": aceite_painel,
        "aceite_fidelidade": aceite_fidelidade,
    }

def parsear_lista_componentes(lista_componentes: list) -> dict:
    resultado = {}

    for item in lista_componentes:
        descricao = item["descricaoTipoComponente"].strip().lower()

        if descricao == "area de abastecimento - petromax":
            nome_componente = "pista"
        elif descricao == "quickmart":
            nome_componente = "loja"
        elif descricao == "oilfast":
            nome_componente = "oilfast"
        else:
            continue

        resultado[nome_componente] = parsear_componente(item)

    return resultado


def validar_ativacao(componentes_solicitados: list, componentes_api: dict) -> dict:
    resultado = {}
    apto = True

    for componente in componentes_solicitados:
        dados = componentes_api.get(componente)

        if not dados:
            resultado[componente] = {"encontrado": False}
            apto = False
            continue

        valido = dados["ativo"] and dados["aceite_painel"] and dados["aceite_fidelidade"]
        resultado[componente] = {
            "encontrado": True,
            "ativo": dados["ativo"],
            "aceite_painel": dados["aceite_painel"],
            "aceite_fidelidade": dados["aceite_fidelidade"],
            "valido": valido,
        }

        if not valido:
            apto = False

    return {
        "componentes": resultado,
        "apto": apto,
    }
