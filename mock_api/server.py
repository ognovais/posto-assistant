"""
Servidor fictício que simula a API do parceiro PetroMax
(PETROMAX_TOKEN_URL / PETROMAX_API_URL usados em modules/ativacao/api.py).

Existe apenas para permitir rodar e demonstrar a tela "Validar componentes
PETROMAX" localmente, sem depender de nenhuma API real. Não faz parte da
lógica original do projeto — é só um utilitário de demonstração/portfólio.

Usa somente a biblioteca padrão do Python (nenhuma instalação extra).

Como rodar:
    python mock_api/server.py

Ele sobe em http://127.0.0.1:5000 e fica rodando até você apertar Ctrl+C.
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

# "oilfast" abaixo está com aceiteProgramaFidelidade=False de propósito, para
# mostrar a tela também detectando um componente pendente. Troque para True se
# quiser um print com os 3 componentes 100% aptos.
COMPONENTES_EXEMPLO = [
    {
        "descricaoTipoComponente": "area de abastecimento - petromax",
        "situacao": "A",
        "aceites": [
            {"nome": "aceitePainelPrecos", "status": True},
            {"nome": "aceiteProgramaFidelidade", "status": True},
        ],
    },
    {
        "descricaoTipoComponente": "quickmart",
        "situacao": "A",
        "aceites": [
            {"nome": "aceitePainelPrecos", "status": True},
            {"nome": "aceiteProgramaFidelidade", "status": True},
        ],
    },
    {
        "descricaoTipoComponente": "oilfast",
        "situacao": "A",
        "aceites": [
            {"nome": "aceitePainelPrecos", "status": True},
            {"nome": "aceiteProgramaFidelidade", "status": False},
        ],
    },
]


class MockHandler(BaseHTTPRequestHandler):
    def _send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if urlparse(self.path).path == "/oauth/token":
            self._send_json({"access_token": "token-ficticio-de-demonstracao"})
        else:
            self._send_json({"erro": "endpoint nao encontrado"}, status=404)

    def do_GET(self):
        if urlparse(self.path).path == "/v1/componentes":
            self._send_json({"listaComponente": COMPONENTES_EXEMPLO})
        else:
            self._send_json({"erro": "endpoint nao encontrado"}, status=404)

    def log_message(self, format, *args):
        print("[mock-petromax]", format % args)


if __name__ == "__main__":
    servidor = HTTPServer(("127.0.0.1", 5000), MockHandler)
    print("Mock PetroMax rodando em http://127.0.0.1:5000 (Ctrl+C para parar)")
    servidor.serve_forever()
