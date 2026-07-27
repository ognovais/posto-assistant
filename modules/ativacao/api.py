import requests
from config import PETROMAX_TOKEN_URL, PETROMAX_CLIENT_ID, PETROMAX_CLIENT_SECRET, PETROMAX_API_URL

class PetroMaxApiClient:
    def __init__(self):
        self.access_token = None

    def renovar_token(self):
        dados = {
            "grant_type": "client_credentials",
            "client_id": PETROMAX_CLIENT_ID,
            "client_secret": PETROMAX_CLIENT_SECRET,
        }

        resposta = requests.post(PETROMAX_TOKEN_URL, data=dados)
        resposta.raise_for_status()

        corpo = resposta.json()
        self.access_token = corpo["access_token"]

    def consultar_componentes(self, cnpj: str):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        params = {
            "cnpjComponente": cnpj
        }

        resposta = requests.get(PETROMAX_API_URL, headers=headers, params=params)
        resposta.raise_for_status()

        return resposta.json()

if __name__ == "__main__":
    client = PetroMaxApiClient()
    client.renovar_token()
    print("Token:", client.access_token)

    resultado = client.consultar_componentes("11222333000181")
    print(resultado)
