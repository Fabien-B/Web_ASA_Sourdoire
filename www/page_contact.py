template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
exploitant = Import('Exploitant.py')
message_file = Import('message.py')
import datetime

def index(error=''):
    if "login" in Session() and not Session()["Id_exploitant"]:
        ret=template.afficherHautPage(error, titre='Demandes à l\'administrateur')
    else:
        ret=template.afficherHautPage(error, titre='Contacter l\'Admin')
    if "login" in Session():
        if Session()["Id_exploitant"] == 0:
            ret += consulter_contact()
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
    """
    return html


def afficherFormulaireContact_non_connecte():
    html = """
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
    """
    return html


def traiterFormulaireContact(nom='', numero='', topic='', demande='', captcha=''):
    result=""

    if captcha == '4':
        new_message = message_file.Message(0)
        if "login" in Session():
            my_exp = exploitant.Exploitant(int(Session()["Id_exploitant"]))
            new_message.nom = my_exp.nom
            new_message.date =  time.asctime()
            new_message.numero = my_exp.numero
            new_message.objet = topic
            new_message.corps = demande
            new_message.id_exploitant = my_exp.id
            new_message.save()
        else:
            new_message.nom = nom
            new_message.date =  str(datetime.datetime.now())
            new_message.numero = numero
            new_message.objet = topic
            new_message.corps = demande
            new_message.id_exploitant = 'NULL'
            new_message.save()

    else:
        return index(error="Captcha invalide")

    return remerciements()


def remerciements(error=''):
    ret=template.afficherHautPage(error, titre='Remerciements')
    ret += """
        <div class="sixteen columns main-content">
            Merci de votre requête, l'administrateur du réseau d'irrigation vous contactera sous peu
        </div>
    """
    ret += template.afficherBasPage()
    return ret


def consulter_contact(error=''):
    message_list = message_file.Message.get_all_messages()
    ret = """<div class="sixteen columns main-content" style="min-height:200px;">"""""
    for my_mail in reversed(message_list):
        ret += """<table class="sixteen columns main-content" style="margin:30px;"><tr><td>""" +"<br />Id n°:\t"+ str(my_mail.id)+"<br />Reçu le:\t"+str(my_mail.date)+"<br />De la part de:\t"+my_mail.nom+"<br />Tel:\t"+my_mail.numero+"<br />Objet:\t"+my_mail.objet+"<br /><br />Message:<br />"+my_mail.corps+"<br /><hr />"+ """</td></tr></table>"""
    ret += """
    </div>
    <div>
        <form action = "../page_contact.py/effacer_demandes" class="two-thirds.column" style="margin:25px">
            <input type="submit" value="Effacer les anciennes demandes" style="margin:30px;">
        </form>
    </div>
    """
    return ret

def effacer_demandes(error=''):
    message_file.Message.delete_all()
    return index()