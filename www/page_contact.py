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
    <div class="container">
        <div class="sixteen columns main-content">
    <h1 class=contactformtitle>Formulaire de contact</h1>
    <br>
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
    <div class=captchadiv>
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
    <div class=captchadiv>Combien font 2+2 ?</div>
    <input class = captchainput type="number" name="captcha" size=5 maxlength=5 value="" placeholder="Captcha" required />
    <br />
    <input type=submit value=Envoyer>
    <input type=reset value=Annuler>
    </form>
        </div>
    </div>
    """
    return html


def traiterFormulaireContact(nom='', numero='', topic='', demande='', captcha=''):
    result=""
    if captcha == '4':

        if len(nom) >=1:
            """requête SQL"""
            result = Session()["nom"] + Session()["Id_exploitant"]
        else:
            result = """<br />Infos : <br />"""
            result += nom + numero + topic + demande
    return result

