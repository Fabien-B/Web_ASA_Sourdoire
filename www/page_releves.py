template = Import('template.py' ) # import du fichier template (entete, pieds de page...)

def index(error=''):
    ret=template.afficherHautPage(error, titre='Relevés')
    ret += corps_conso()
    ret += template.afficherBasPage()
    return ret

def corps_conso():
    html = """
    <p>Je regarde mes relevés</p>
    """
    return html