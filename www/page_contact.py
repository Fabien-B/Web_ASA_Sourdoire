template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')

def index(error=''):
    ret=template.afficherHautPage(error, titre='Contacter l\'Admin')
    ret += corps_page()
    ret += template.afficherBasPage()
    return ret

def corps_page_connecte():
    html = """
    <p>J'irais chercher le contact</p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/YUNtPBmQTR8" frameborder="0" allowfullscreen></iframe>
    """
    return html

def corps_page_deconnecte():
    html = """
    <p>J'irais chercher le contact</p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/YUNtPBmQTR8" frameborder="0" allowfullscreen></iframe>
    """
    return html

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)
