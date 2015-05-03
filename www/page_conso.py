template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')

def index(error=''):
    ret=template.afficherHautPage(error, titre='Ma Conso')
    ret += corps_page()
    ret += template.afficherBasPage()
    return ret

def corps_page():
    html = """
    <p>Je bois de l'eauuuuuu!!!</p>
    """
    return html

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)