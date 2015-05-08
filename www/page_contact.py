template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
exploitant = Import('Exploitant.py')


def index(error=''):
    ret=template.afficherHautPage(error, titre='Contacter l\'Admin')
    if "login" in Session():
        ret += afficherFormulaireContact_connecte()
    else:
        ret+= afficherFormulaireContact_non_connecte()
    ret += template.afficherBasPage()
    return ret


def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)


def afficherFormulaireContact_connecte():
    html = """
    <h1 id=contactformtitle>Formulaire de contact</h1>
    <br>
    <h2 id=numtel>Numéro de téléphone de l'administrateur : """ + str(exploitant.Exploitant(0).tel) + """</h2>
    <form id=contactform action=../page_contact.py/traiterFormulaireContact METHOD="get">
    <table id = contacttable>
    <tr>
    <td id = objetdemande><strong>Objet de la Demande :</strong></td><td id = formobjetdemande>
    <input name="topic" size=20 maxlength=70 type="text" value="" placeholder="Objet de la demande" required />
    </td></tr>
    <tr id = tr2><td colspan=2>
    <textarea NAME="demande" ROWS="10" cols="500" placeholder="Votre demande ici"></textarea>
    </td></tr></table>
    <br />
    <div>Combien font 2+2 ?</div>
    <input type="text" name="captcha" size=5 maxlength=5 value="" placeholder="Captcha" required />
    <br />
    <input type=submit value=Envoyer>
    <input type=reset value=Annuler>
    </form>
    """
    return html


def afficherFormulaireContact_non_connecte():
    html = """
    <h2>Formulaire de contact</h2>
    <br />
    <form id=contact action=../page_contact.py/traiterFormulaireContact METHOD="get">
    <table>
    <tr>
    <td> Votre Nom : </td>
    <td>
    <input name="nom" size=15 maxlength=40 type="text" value="Votre nom + prénom" placeholder="Name" required />
    </td>
    </tr>
    <tr>
    <td> Votre numéro de téléphone </td>
    <td>
    <input name="numero" size=10 maxlength=15 type="text" value="Votre numéro de téléphone" placeholder="NumeroTel" />
    </td>
    </tr>
    <tr>
    <td> L'objet de votre demande </td>
    <td>
    <input name="topic" size=20 maxlength=50 type="text" value="Objet de la demande" placeholder="Topic" required />
    </td>
    </tr>
    <tr><td colspan=2>Votre demande<br>
    <textarea name="demande" rows="6" cols="200"></textarea>
    </td></tr>
    </table>
    <br />
    <div>Combien font 2+2 ?</div>
    <input type="number" name="captcha" size=5 maxlength=5 value="" placeholder="Captcha" required />
    <br />
    <input type=submit value=Envoyer>
    <input type=reset value=Annuler>
    </form>
    """
    return html


def traiterFormulaireContact(page, nom='', numero='', topic='', demande='', captcha=''):
    if captcha == 4:

        if len(nom) >=1:
            """requête SQL"""
            result = Session()["nom"] + Session()["Id_exploitant"]
        else:
            result = """<br />Infos : <br />"""
            result += nom + numero + topic + demande
    return result

