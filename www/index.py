
template = Import('template.py' ) # import du fichier template (entete, pieds de page...)

def index(error=''):
    ret=template.afficherHautPage(error, titre='Accueil')
    ret += corps_accueil()
    ret += template.afficherBasPage()
    return ret

def corps_accueil():
    html = """
    <p>Un petit paragraphe</p>
    """
    return html

def traiterFormulaireConnexion(choix, login='',password=''):
    if choix=='deconnecter': 
        if "login" in Session(): del Session()["login"]
        return index('Deconnecte')
    else:
        if password != 'test':
            Session()["login"] = login;
            return  index()
        else:
            return index('error')
