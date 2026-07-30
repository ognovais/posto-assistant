import re

def desmascarar_cnpj(cnpj: str) -> str:
    return re.sub(r"\D", "", cnpj)

def mascarar_cnpj(cnpj_limpo: str) -> str:
    return f"{cnpj_limpo[0:2]}.{cnpj_limpo[2:5]}.{cnpj_limpo[5:8]}/{cnpj_limpo[8:12]}-{cnpj_limpo[12:14]}"

if __name__ == "__main__":
    print(desmascarar_cnpj("11.222.333/0001-81"))
    print(mascarar_cnpj("11222333000181"))
