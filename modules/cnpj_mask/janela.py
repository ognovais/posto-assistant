from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout, QPushButton
from modules.cnpj_mask.service import desmascarar_cnpj, mascarar_cnpj
from modules.utils.janela import centralizar_janela

def abrir_janela_cnpj_mask():
    janela = QWidget()
    janela.setWindowTitle("Editar CNPJ")
    janela.resize(350, 200)
    centralizar_janela(janela)

    layout = QVBoxLayout()

    campo_texto = QLineEdit()
    campo_texto.setPlaceholderText("Cole aqui o CNPJ para ser editado")

    campo_resultado = QLineEdit()
    campo_resultado.setReadOnly(True)

    def ao_clicar_mascarar():
        resultado = mascarar_cnpj(campo_texto.text())
        campo_resultado.setText(resultado)
        QApplication.clipboard().setText(resultado)

    def ao_clicar_desmascarar():
        resultado = desmascarar_cnpj(campo_texto.text())
        campo_resultado.setText(resultado)
        QApplication.clipboard().setText(resultado)

    botao_mascarar = QPushButton("Mascarar")
    botao_mascarar.clicked.connect(ao_clicar_mascarar)
    botao_mascarar.setFixedHeight(75)

    botao_desmascarar = QPushButton("Desmascarar")
    botao_desmascarar.clicked.connect(ao_clicar_desmascarar)
    botao_desmascarar.setFixedHeight(75)

    layout.addWidget(campo_texto)
    layout.addWidget(botao_mascarar)
    layout.addWidget(botao_desmascarar)
    layout.addWidget(campo_resultado)

    janela.setLayout(layout)
    janela.show()

    return janela
