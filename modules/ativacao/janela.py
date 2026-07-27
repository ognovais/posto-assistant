import re
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QTextEdit
from modules.ativacao.service import validar_chamado, formatar_resultado
from modules.utils.janela import centralizar_janela

def abrir_janela_ativacao():
    janela = QWidget()
    janela.setWindowTitle("Validação Componentes PETROMAX")
    janela.resize(1200, 750)
    centralizar_janela(janela)

    layout = QVBoxLayout()

    campo_texto = QTextEdit()
    campo_texto.setPlaceholderText("Cole aqui os dados a serem validados...")

    campo_resultado = QTextEdit()
    campo_resultado.setReadOnly(True)

    def ao_clicar_validar():
        texto = campo_texto.toPlainText()
        linhas = re.split(r'(?<=Pista)\s+(?=[A-ZÀ-Ú])|(?<=Loja)\s+(?=[A-ZÀ-Ú])|(?<=OilFast)\s+(?=[A-ZÀ-Ú])', texto)
        linhas = [linha.strip() for linha in linhas if linha.strip()]

        campo_resultado.clear()

        for linha_chamado in linhas:
            try:
                resultado = validar_chamado(linha_chamado)
                campo_resultado.append(formatar_resultado(resultado))
            except Exception as erro:
                campo_resultado.append(f"Erro ao validar linha: {linha_chamado}\nMotivo: {erro}")

            campo_resultado.append("=" * 40)
            QApplication.processEvents()

    botao_gerar = QPushButton("Validar dados")
    botao_gerar.clicked.connect(ao_clicar_validar)

    layout.addWidget(campo_texto)
    layout.addWidget(botao_gerar)
    layout.addWidget(campo_resultado)

    janela.setLayout(layout)
    janela.show()

    return janela
