import re

def extrair_dados_ativacao(texto: str) -> dict:
    cnpj_pattern = r"\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}"
    cnpj_match = re.search(cnpj_pattern, texto)
    cnpj = cnpj_match.group() if cnpj_match else None
    cnpj_limpo = re.sub(r"\D", "", cnpj) if cnpj else None

    antes_cnpj = texto[:cnpj_match.start()] if cnpj_match else texto
    partes = [p.strip() for p in re.split(r"\t|\n", antes_cnpj) if p.strip()]
    razao_social = partes[0] if partes else None

    texto_lower = texto.lower()
    componentes = []

    if "pista" in texto_lower:
        componentes.append("pista")

    if "loja" in texto_lower:
        componentes.append("loja")

    if "oilfast" in texto_lower:
        componentes.append("oilfast")

    return {
        "razao_social": razao_social,
        "cnpj": cnpj,
        "cnpj_limpo": cnpj_limpo,
        "componentes": componentes
    }
