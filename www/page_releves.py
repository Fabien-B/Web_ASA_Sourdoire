template = Import('template.py' ) # import du fichier template (entete, pieds de page...)

def index(error=''):
    ret=template.afficherHautPage(error, titre='Entrer un relevé')
    ret += corps_page()
    ret += template.afficherBasPage()
    return ret

def corps_page():
    html = """
    <p>Je regarde mes relevés</p>
    """
    return html