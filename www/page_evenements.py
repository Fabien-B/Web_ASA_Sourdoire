template = Import('template.py' ) # import du fichier template (entete, pieds de page...)

def index(error=''):
    ret=template.afficherHautPage(error, titre='Évènements')
    ret += corps_conso()
    ret += template.afficherBasPage()
    return ret

def corps_conso():
    html = """
    <p>Je consulte les évènements</p>
    """
    return html