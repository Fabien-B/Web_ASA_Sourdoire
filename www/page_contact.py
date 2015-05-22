template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
exploitant = Import('Exploitant.py')
import time
import bcrypt


def index(error=''):
    ret=template.afficherHautPage(error, titre='Contacter l\'Admin')
    if "login" in Session():
        if Session()["Id_exploitant"] == "0":
            ret += afficherContact_admin()
        else:
            ret += afficherFormulaireContact_connecte()
    else:
        ret+= afficherFormulaireContact_non_connecte()
    ret += template.afficherBasPage()
    return ret


def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)


def afficherFormulaireContact_connecte():
    html = """
    <div class="container">
        <div class="sixteen columns main-content">
    <h1 class=contactformtitle>Formulaire de contact</h1>
    <br />
    <h2 id=numtel>Numéro de téléphone de l'administrateur : """ + str(exploitant.Exploitant(0).tel) + """</h2>
    <form class=contactform action=../page_contact.py/traiterFormulaireContact METHOD="POST">
    <table class = contacttable style="border:0px;">
    <tr>
    <td class = objetdemande><strong>Objet de la Demande :</strong></td><td id = formobjetdemande>
    <input id=topicinput name="topic" size=20 maxlength=70 type="text" value="" placeholder="Objet de la demande" required />
    </td></tr>
    <tr id = tr2><td colspan=2>
    <textarea class=topicarea NAME="demande" ROWS="10" cols="500" placeholder="Votre demande ici"></textarea>
    </td></tr></table>
    <br />
    <div class=captchadiv>Combien font 2+2 ? <br />
    <input class = captchainput type="text" name="captcha" size=5 maxlength=5 value="" placeholder="Captcha" required /></div>
    <br />
    <div class=captchadiv2>
    <input type=submit value=Envoyer>
    <input type=reset value=Annuler>
    </div>
    </form>
        </div>
    </div>
    """
    return html


def afficherFormulaireContact_non_connecte():
    html = """
    <div class="container">
        <div class="sixteen columns main-content">
    <h1 class=contactformtitle style="margin-top:40px">Formulaire de contact</h1>
    <br />
    <form class=contactform action=../page_contact.py/traiterFormulaireContact METHOD="POST" class="two-thirds.column" style="margin:25px">
    <table class = contacttable style="border:0px;">
    <tr>
    <td class = objetdemande> Votre Nom : </td>
    <td class = formobjetdemande>
        <input name="nom" size=15 maxlength=40 type="text" placeholder="Nom + prénom" placeholder="Name" required />
    </td>
    </tr>
    <tr>
    <td class = objetdemande> Votre numéro de téléphone </td>
    <td class = formobjetdemande>
        <input name="numero" size=10 maxlength=15 type="text" placeholder="Numéro de téléphone" placeholder="NumeroTel" />
    </td>
    </tr>
    <tr>
    <td class = objetdemande> L'objet de votre demande </td>
    <td class = formobjetdemande>
        <input name="topic" size=20 maxlength=50 type="text" placeholder="Objet de la demande" required />
    </td>
    </tr>
    <tr><td colspan=2>Votre demande<br>
    <textarea class=topicarea name="demande" placeholder="Votre demande ici" rows="10" cols="500" style="margin=20px"></textarea>
    </td></tr>
    </table>
    <br />
    <div class=captchadiv>Combien font 2+2 ? <br />
    <input class = captchainput type="text" name="captcha" size=5 maxlength=5 value="" placeholder="Captcha" required /></div>
    <br />
    <div class=captchadiv2>
    <input type=submit value=Envoyer>
    <input type=reset value=Annuler>
    </div>
    </form>
        </div>
    </div>
    """
    return html


def traiterFormulaireContact(nom='', numero='', topic='', demande='', captcha=''):
    result=""

    if captcha == '4':

        if "login" in Session():
            result += "Nom : " + str(Session()["nom"]) + "\n ;  Identifiant : " + str(Session()["Id_exploitant"])
            result += "\n ; Sujet : " + topic + "\n ; Demande : " + demande
        else:
            result += """<br />Infos : <br />"""
            result += nom + numero + topic + demande
        final = str(time.asctime() + result)

        with open("contact.txt", "a") as f:
            f.write(final)
            f.close()
    else:
        return index()

    return remerciements()


def remerciements(error=''):
    ret=template.afficherHautPage(error, titre='Remerciements')
    ret += """
    <div class="container">
        <div class="sixteen columns main-content">
            Merci de votre requête, l'administrateur du réseau d'irrigation vous contactera sous peu
        </div>
    </div>
    """
    ret += template.afficherBasPage()
    return ret

def afficherContact_admin():
    result = """
    <div class="container">
        <div class="sixteen columns main-content">
            <div>Le numéro de l'administrateur affiché est : """ + str(exploitant.Exploitant(0).tel) + """</div>
            <form action=../page_contact.py/changerNumero METHOD="POST" class="two-thirds.column" style="margin:25px">
            <div style="margin-top = 40px;">
                <div>Changer le numéro affiché : <input name="tel" size=10 maxlength=10 type="tel" value="" placeholder="Nouveau numéro de téléphone" required />
                </div>
            <div>
                <input name="mdp" size=20 maxlength=40 type="password" placeholder="Mot de passe administrateur" required />
            </div>
            <div>
                <input type=submit value=Envoyer>
                <input type=reset value=Annuler>
            </div>
        </div>
    </div>"""


def changerNumero(mdp='', tel=''):
    myexploitant = exploitant.Exploitant(Session()["Id_exploitant"])
    if bcrypt.hashpw(mdp, myexploitant.salt) == myexploitant.password:
        nom = myexploitant.nom
        login = myexploitant.login
        password = myexploitant.password
        email = myexploitant.mail
        salt = myexploitant.salt
        if not email: email = "Non renseignée"
        myexploitant.update(nom, email, tel, login, password, salt)

        result = template.afficherHautPage(error, titre='Contacter l\'Admin')
        result += """
        <div class="container">
            <div class="sixteen columns main-content">
                Merci de votre mise à jour, les utilisateurs du réseau pourront à nouveau vous contacter par téléphone
            </div>
        </div>
        """
        result += template.afficherBasPage()
        return result
    else:
        return index()



