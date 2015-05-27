template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
exploitant = Import('Exploitant.py')
import hashlib
import binascii
import uuid


def index(error=''):
    ret=template.afficherHautPage(error)
    if "login" in Session():
        ret += corps_page()
    else:
        ret+= corps_page_deco()
    ret += template.afficherBasPage()
    return ret

def corps_page():

        nom, login, email, tel = get_info_exploitant()
        html = """
        <div class="container">
            <div class="sixteen columns main-content">
                <div class="sixteen columns">
                    <h2 style="text-align:center;">Votre profil</h2>
                </div>
                <form action="updateProfile" method="POST">
                    <div class="one-third column alpha">
                        <label>Votre nom :</label>
                        <h3>{0}</h3>
                        <label>Changer de nom :</label>
                        <input name="nom" type="text" placeholder="Nouveau nom" />
                        <hr>
                        <label>Votre numéro de téléphone :</label>
                        <h3>{3}</h3>
                        <label>Changer de numéro de téléphone :</label>
                        <input type="tel" name="tel" placeholder="Nouveau numéro de téléphone" />
                    </div>
                    <div class="one-third column alpha">
                        <label>Votre identifiant :</label>
                        <h3>{1}</h3>
                        <label>Changer d'identifiant :</label>
                        <input name="login" type="text" maxlength=10 placeholder="Nouvel identifiant" />
                        <hr>
                        <label>Changer votre mot de passe :</label>
                        <input name="password" type="password" placeholder="Nouveau mot de passe" />
                        <input name="password_confirm" type="password" placeholder="Confirmer le nouveau mot de passe" />
                    </div>
                    <div class="one-third column omega">
                        <label>Adresse mail :</label>
                        <h3>{2}</h3>
                        <label>Changer d'adresse mail :</label>
                        <input name="email" type="email" placeholder="Nouvelle adresse mail" />
                        <hr>
    </div>
    <hr>
    <div class="two-thirds column omega offset-by-five">
    <label>Entrer votre mot de passe actuel (pour confirmation) :</label>
    <input type="password" name="old_password" placeholder="Mot de passe actuel" required />
    <input type="submit" name="submit" value="Valider" />
    </div>
    </form>
    </div>
    </div>
    """.format(nom, login, email, tel)
        return html


def corps_page_deco():
        html='''
         <div class="container">
            <div class="sixteen columns main-content">
                <div class="sixteen columns over" style="text-align:center">
                    <h1> Veuillez vous identifier</h1>
                </div>
            </div>
        </div>
        '''
        return html


def get_info_exploitant():
    myexploitant = exploitant.Exploitant(Session()["Id_exploitant"])
    nom = myexploitant.nom
    login = myexploitant.login
    email = myexploitant.mail
    tel =myexploitant.tel
    if not email: email = "Non renseignée"
    if not tel: tel = "Non renseigné"
    return nom, login, email, tel

def updateProfile(nom=0, tel=0, login=0, password=0, password_confirm=0, email=0, old_password=0, submit=0):
    myexploitant = exploitant.Exploitant(Session()["Id_exploitant"])
    if binascii.hexlify(hashlib.pbkdf2_hmac('sha256', bytes(old_password, 'utf-8'), bytes(myexploitant.salt, 'utf-8'), 100000)).decode() == myexploitant.password:
        salt = uuid.uuid4().hex
        if not nom: nom = myexploitant.nom
        if not tel: tel = myexploitant.tel
        if not login: login = myexploitant.login
        if not password:
            password = myexploitant.password
        elif password != password_confirm:
            return index()
        else:
            password = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', password.encode('UTF-8'), bytes(salt, 'utf-8'), 100000)).decode()
        if not email: email = myexploitant.mail
        myexploitant.update(nom, email, tel, login, password, salt)
        Session()["login"] = login
        Session()["nom"] = nom
        return index('Profil mis à jour')
    else:
        return index("Mot de passe incorrect, modifications annulées")

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)