from PySide6.QtWidgets import QApplication

def centralizar_janela(janela):
    tela = QApplication.primaryScreen().availableGeometry()

    x = (tela.width() - janela.width()) // 2
    y = (tela.height() - janela.height()) // 2

    janela.move(x, y)
