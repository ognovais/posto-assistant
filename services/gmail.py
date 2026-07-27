import webbrowser
from urllib.parse import quote

def abrir_gmail(destinatario, cc, assunto, corpo):
    assunto_cod = quote(assunto)
    corpo_cod = quote(corpo)
    cc_cod = quote(cc)

    url = (
        f"https://mail.google.com/mail/?view=cm&fs=1"
        f"&to={destinatario}"
        f"&cc={cc_cod}"
        f"&su={assunto_cod}"
        f"&body={corpo_cod}"
    )

    webbrowser.open(url)
