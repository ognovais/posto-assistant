import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from modules.ativacao.janela import abrir_janela_ativacao
from modules.carga_full.janela import abrir_janela_carga_full
from modules.utils.janela import centralizar_janela


app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle('Posto Assistant')
janela.resize(300, 500)
centralizar_janela(janela)

layout = QVBoxLayout()

janela_carga = None
janela_ativacao = None


def abrir_carga():
    global janela_carga
    janela_carga = abrir_janela_carga_full()

def abrir_ativacao():
    global janela_ativacao
    janela_ativacao = abrir_janela_ativacao()

botao_gerar = QPushButton("Gerar Email Carga FULL SGA")
botao_gerar.setFixedSize(300, 150)
botao_gerar.clicked.connect(abrir_carga)
botao_validar = QPushButton("Validar componentes PETROMAX")
botao_validar.setFixedSize(300, 150)
botao_validar.clicked.connect(abrir_ativacao)

layout.addWidget(botao_gerar)
layout.addWidget(botao_validar)

janela.setLayout(layout)
janela.show()

sys.exit(app.exec())
