template = Import('template.py' ) # import du fichier template (entete, pieds de page...)

def index(error=''):
    ret=template.afficherHautPage(error, titre='Le Réseau')
    ret += corps_conso()
    ret += template.afficherBasPage()
    return ret

def corps_conso():
    html = """
    <p>Voici le réseau</p>
    """
    return html