# Posto Assistant

Ferramenta desktop desenvolvida em **Python + PySide6** para automatizar rotinas repetitivas de suporte técnico em ambientes de automação comercial (ex.: postos de combustíveis e redes de varejo). O objetivo é reduzir o tempo gasto em tarefas manuais e repetitivas do time de suporte, como conferência de dados de ativação em APIs de parceiros e geração de e-mails padronizados de solicitação de serviço.

> Este é um projeto de portfólio. Nomes de empresas, clientes, parceiros, e-mails, CNPJs e credenciais originais foram substituídos por dados fictícios. Detalhes em [`PORTFOLIO_CHANGES.md`](./PORTFOLIO_CHANGES.md).

## Funcionalidades

- **Validação de componentes de automação**: cola-se o texto de um chamado de suporte (ou vários, um após o outro), a aplicação extrai CNPJ, razão social e os componentes solicitados (pista, loja, serviço de troca de óleo), consulta uma API externa de um parceiro de automação e mostra se cada componente está ativo e com os aceites necessários, indicando se o cliente está apto para a ativação.
- **Geração de e-mail de Carga Full**: cola-se os dados recebidos de um chamado, a aplicação extrai os campos (ID do sistema, CNPJ, razão social, nome do cliente, telefone, e-mail, data de implantação), valida se todos os campos obrigatórios foram informados e abre um rascunho de e-mail já preenchido (assunto, corpo e destinatários) direto no Gmail via navegador.
- **Interface gráfica simples**: janela principal com botões de acesso rápido a cada rotina, sem necessidade de uso de terminal no dia a dia.

## Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [PySide6](https://doc.qt.io/qtforpython/) — interface gráfica (Qt for Python)
- [Requests](https://docs.python-requests.org/) — consumo de API REST externa (OAuth2 client credentials)
- [PyInstaller](https://pyinstaller.org/) — empacotamento em executável Windows (`.spec` incluído)
- Expressões regulares (`re`) para extração e parsing de texto semiestruturado

## Estrutura do projeto

```
posto-assistant/
├── main.py                        # Ponto de entrada, janela principal
├── modules/
│   ├── ativacao/                  # Validação de componentes via API do parceiro
│   │   ├── api.py                 # Cliente HTTP (OAuth2 client credentials)
│   │   ├── janela.py              # Interface da tela de validação
│   │   ├── parser.py              # Extração de CNPJ, razão social e componentes do texto colado
│   │   ├── service.py             # Orquestração: parser + API + validator
│   │   └── validator.py           # Regras de negócio de ativação
│   ├── carga_full/
│   │   └── janela.py              # Interface da tela de geração de e-mail
│   └── utils/
│       └── janela.py              # Utilitário de centralização de janelas
├── services/
│   ├── parser.py                  # Extração dos campos do chamado (regex)
│   ├── email_generator.py         # Montagem do assunto/corpo a partir do template
│   └── gmail.py                   # Abertura de rascunho no Gmail via URL
├── templates/
│   └── carga_full_sga.txt         # Template do corpo do e-mail
├── ui/
│   └── janela_principal.py        # Reservado para evolução futura da UI
├── mock_api/
│   └── server.py                  # Mock local da API do parceiro, só para demonstração
├── config.py                      # Configuração de demonstração (aponta para o mock local)
├── config.py.example              # Modelo de configuração (para uso com uma API real)
├── requirements.txt
├── PostoAssistant.spec            # Configuração do PyInstaller
├── run.bat                        # Atalho para rodar em Windows
└── PORTFOLIO_CHANGES.md           # Relatório de sanitização deste repositório
```

## Como executar

### Pré-requisitos

- Python 3.10+
- pip

### Passo a passo

```bash
# 1. Clone o repositório
git clone <url-do-seu-fork>
cd posto-assistant

# 2. Crie e ative um ambiente virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as credenciais da API do parceiro
copy config.py.example config.py   # Windows
# cp config.py.example config.py   # Linux/macOS
# edite config.py com as suas credenciais (não é versionado)

# 5. Execute a aplicação
python main.py
```

No Windows, também é possível usar o atalho `run.bat`, que ativa o ambiente virtual e inicia a aplicação.

### Gerando o executável (opcional)

```bash
pip install pyinstaller
pyinstaller PostoAssistant.spec
```

O executável será gerado em `dist/PostoAssistant.exe`.

## Rodando com dados de demonstração (mock local)

A tela "Validar componentes PETROMAX" depende de uma API externa. Para testar o fluxo completo sem uma API real, o repositório inclui um mock simples em `mock_api/server.py` (só biblioteca padrão do Python, sem instalar nada a mais). O `config.py` já vem configurado para apontar para ele.

```bash
# Terminal 1 — sobe o mock em http://127.0.0.1:5000
python mock_api/server.py

# Terminal 2 — com o venv ativado
python main.py
```

Textos de exemplo para colar nas telas e tirar prints:

**Validar componentes PETROMAX:**
```
Posto Fictício Exemplo LTDA
12.345.678/0001-90
Pista Loja OilFast
```

**Gerar Email Carga FULL SGA:**
```
ID_SISTEMA: 000123
CNPJ: 12.345.678/0001-90
Razão Social: Posto Fictício Exemplo LTDA
Nome do Cliente: João da Silva
Telefone: (11) 99999-0000
E-mail: cliente.contato@example.com
Data da implantação: 01/08/2026
```

> Nota: `config.py` continua listado no `.gitignore` (boa prática mantida do projeto original). Ele já vem criado neste pacote só para você rodar localmente e tirar prints. Se quiser que qualquer pessoa que clonar o repositório no GitHub consiga rodar o mock sem passos extras, remova `config.py` do `.gitignore` antes de publicar — os valores nele são fictícios e apontam só para `127.0.0.1`, sem nenhum risco.

## Licença

Distribuído sob a licença MIT. Veja [`LICENSE`](./LICENSE) para mais detalhes.
