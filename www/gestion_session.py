import bcrypt
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