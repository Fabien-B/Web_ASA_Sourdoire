
def Connexion(page, choix, login='',password=''):
    if choix=='deconnecter':
        if "login" in Session(): del Session()["login"]
        return page('Deconnecte')
    else:
        if password != 'test':
            Session()["login"] = login;
            return  page()
        else:
            return page('error')