template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
exploitant = Import('Exploitant.py')
message_file = Import('message.py')
import datetime

def index(error=''):
    ret=template.afficherHautPage(error, titre='Contacter l\'Admin')
    if "login" in Session():
        if Session()["Id_exploitant"] == 0:
            ret=template.afficherHautPage(error, titre='Messages')
            ret += consulter_contact()
        else:
            ret += afficherFormulaireContact_connecte()
    else:
        ret=template.afficherHautPage(error, titre='Contacter l\'Admin')
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
    <form class=contactform action=../page_contact.py/traiterFormulaireContact METHOD="POST">
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
            new_message.date =  str(datetime.datetime.now())
            new_message.tel = my_exp.tel
            new_message.objet = topic.replace("\"", "\\\"")
            new_message.corps = demande.replace("\"", "\\\"")
            new_message.id_exploitant = my_exp.id
            new_message.save()
        else:
            new_message.nom = nom
            new_message.date =  str(datetime.datetime.now())
            new_message.tel = numero
            new_message.objet = topic.replace("\"", "\\\"")
            new_message.corps = demande.replace("\"", "\\\"")
            new_message.id_exploitant = '0'
            new_message.save()

    else:
        return index(error="Captcha invalide")

    return remerciements()


def remerciements(error=''):
    ret=template.afficherHautPage(error="L'administrateur vous contactera sous peu", titre='Remerciements')
    ret += """
        <div class="sixteen columns main-content" style="text-align:center;min-height:400px;">
            Merci de votre requête, l'administrateur du réseau d'irrigation vous contactera sous peu
        </div>
    """
    ret += template.afficherBasPage()
    return ret


def consulter_contact(error=''):
    ret = """
            <div class="sixteen columns over" style="text-align:center">
                <h1>Messages</h1>
            </div>
        """
    message_list = message_file.Message.get_all_messages()
    if message_list:
        ret += """<div class="container"
        <div class="sixteen columns main-content" style="min-height:200px;">
                    <form action = "../page_contact.py/effacer_demandes"  style="margin:25px">
            """
        for my_mail in reversed(message_list):
            myexp = exploitant.Exploitant(my_mail.id_exploitant)
            my_mail.tel = myexp.tel if my_mail.id_exploitant else my_mail.tel
            my_mail.update()
            tel = "Téléphone non renseigné" if my_mail.tel is None else "Téléphone : "+str(my_mail.tel)
            auth = "" if my_mail.id_exploitant else "(Utilisateur NON authentifié)"
            ret+="""
                <div id="event"><h4>Message {0}
                Le <b>{1}</b> </h4>
                Objet : {5}<br />
                <blockquote class="testimonial">
                {6}
                <cite>
                   {7}<strong>{2}</strong>{8} <i>{4}</i><br />
                    {3}
                </cite>
                </blockquote>
                    <div style="text-align:center;">
                        <button type="submit" value={0} name="mailid">Supprimer</button><br />
                    </div>
                </div>
                """.format(my_mail.id, my_mail.date, my_mail.nom,
                           str(tel), auth, my_mail.objet, my_mail.corps, "<a href='../page_gestion_exploitant.py/corps_page_exploitant?exploitant="+str(myexp.id)+"'>" if my_mail.id_exploitant else "", "</a>"if my_mail.id_exploitant else "")


        ret += """
            </form>
            </div>
            </div>
        """
    else:
        ret+="""
        <div class="sixteen columns main-content" style="min-height:200px; text-align:center;">
            <h4>Vous n'avez aucun message</h4>
        </div>
        """
    return ret

def effacer_demandes(mailid=0):
    message_file.Message(int(mailid)).delete()
    return index()