template = Import('template.py' ) # import du fichier template (entete, pieds de page...)

def index(error=''):
    ret=template.afficherHautPage(error, titre='Voir le réseau')
    ret += corps_page()
    ret += template.afficherBasPage()
    return ret

def corps_page():
    html = """
    <p>Voici le réseau</p>
    """
    return html