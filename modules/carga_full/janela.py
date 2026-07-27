import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox
from services.parser import extrair_dados, validar_dados, formatar_erros
from services.gmail import abrir_gmail
from services.email_generator import gerar_assunto, gerar_corpo
from modules.utils.janela import centralizar_janela

def abrir_janela_carga_full():
    janela = QWidget()
    janela.setWindowTitle("Gerador de Carga Full SGA")
    janela.resize(600, 400)
    centralizar_janela(janela)

    layout = QVBoxLayout()

    campo_texto = QTextEdit()
    campo_texto.setPlaceholderText("Cole aqui os dados recebidos...")

    def ao_clicar_gerar():
        texto = campo_texto.toPlainText()
        dados = extrair_dados(texto)
        campos_faltando = validar_dados(dados)

        if campos_faltando:
            erros = formatar_erros(campos_faltando)
            mensagem = "\n".join(erros)
            return QMessageBox.warning(janela, "Campos faltando", mensagem)

        abrir_gmail(
            destinatario="cliente.contato@example.com",
            cc="suporte@techposto.example.com,parceiro@petromax.example.com,equipe@techposto.example.com",
            assunto=gerar_assunto(dados),
            corpo=gerar_corpo(dados)
        )

    botao_gerar = QPushButton("Gerar E-mail")
    botao_gerar.clicked.connect(ao_clicar_gerar)

    layout.addWidget(campo_texto)
    layout.addWidget(botao_gerar)

    janela.setLayout(layout)
    janela.show()

    return janela
