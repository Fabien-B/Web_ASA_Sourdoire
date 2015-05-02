template = Import('template.py' ) # import du fichier template (entete, pieds de page...)

def index(error=''):
    ret=template.afficherHautPage(error, titre='Contacter l\'Admin')
    ret += corps_page()
    ret += template.afficherBasPage()
    return ret

def corps_page():
    html = """
    <p>J'irais chercher le contact</p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/YUNtPBmQTR8" frameborder="0" allowfullscreen></iframe>
    """
    return html