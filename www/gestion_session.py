import bcrypt           #commenter / decommenter cette ligne pour utiliser ou non le hashage du mot de passe
exploitant = Import('Exploitant.py')

def Connexion(page, choix, login='',password=''):
    if choix=='Déconnecter':
        if "login" in Session(): del Session()["login"]
        return page('Deconnecte')
    else:
        id_ex = exploitant.Exploitant.exist_login(login)
        if id_ex == -1:
            return page('error')
        target_ex = exploitant.Exploitant(id_ex)
        pw_base = target_ex.password
        salt = target_ex.salt
        pw_user = bcrypt.hashpw(password,salt)
        if pw_user == pw_base:
            Session()["login"] = target_ex.login
            Session()["Id_exploitant"] = target_ex.id
            Session()["nom"] = target_ex.nom
            return  page()
        else:
            return page('error')

def Connexion_without_bcrypt(page, choix, login='',password=''):
    '''Fonction de connection sans haschage du mot de passe ==> mot de passe en clair dans la BDD !!!'''
    if choix=='Déconnecter':
        if "login" in Session(): del Session()["login"]
        return page('Deconnecte')
    else:
        id_ex = exploitant.Exploitant.exist_login(login)
        if id_ex == -1:
            return page('error')
        target_ex = exploitant.Exploitant(id_ex)
        pw_base = target_ex.password
        if password == pw_base:
            Session()["login"] = target_ex.login
            Session()["Id_exploitant"] = target_ex.id
            Session()["nom"] = target_ex.nom
            return  page()
        else:
            return page('error')