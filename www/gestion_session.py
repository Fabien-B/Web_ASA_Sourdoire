import hashlib
import binascii

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
        pw_user = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), bytes(salt, 'utf-8'), 100000)).decode()
        if pw_user == pw_base:
            Session()["login"] = target_ex.login
            Session()["Id_exploitant"] = target_ex.id
            Session()["nom"] = target_ex.nom
            return  page()
        else:
            return page('error')
