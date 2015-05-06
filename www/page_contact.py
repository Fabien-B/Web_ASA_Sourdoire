template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')


def index(error=''):
    ret=template.afficherHautPage(error, titre='Contacter l\'Admin')
    ret += corps_page()
    ret += template.afficherBasPage()
    return ret


def corps_page_connecte():
    html = """
    <div>Numéro de téléphone du gérant : 06 XX XX XX XX</div>
    <br />
    """
    html += contenu_contact()
    return html


def corps_page_deconnecte():
    return contenu_contact()


def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)


def contenu_contact():
    html = """
    <h2>Formulaire de contact</h2>
    <form id=contact action=traiterFormulaireContact METHOD="get">
    <br />
    <input name="topic" size=20 maxlength=30 type="text" value="Objet de la demande" placeholder="Topic" required />
    <textarea NAME="demande" ROWS="6" COLS="200"></textarea>
    <br />
    <div>Combien font 2+2 ?</div>
    <input type="text" name="captcha" size=5 maxlength=5 value="" placeholder="Captcha" required />
    <br />
    <input type=submit value=Envoyer>
    <input type=reset value=Annuler>
    </form>
    """
    return html

def traiterFormulaireContact(page, id="", pwd=""):
    