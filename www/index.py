
template = Import('template.py' ) # import du fichier template (entete, pieds de page...)

def index(message=''):
    ret=template.afficherHautPage()
    ret += corps_accueil()
    ret += template.afficherBasPage()
    return ret

def corps_accueil():
    html = """
    <h1>Le titre d'accueil!</h1>
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
            return  index('Login Ok <b>'+login+'</b><br/>Vous pouvez modifier')
        else:
            return index('login incorrect!')
