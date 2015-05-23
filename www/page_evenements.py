exploitant = Import('Exploitant.py')
compteur = Import('compteur.py')
releve = Import('releve.py')
parcelle = Import('parcelle.py')
template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')


def index(error=''):
    ret=template.afficherHautPage(error, titre='Signaler un évènement')
    if "login" in Session():
            ret += corps_page_connecte()
    else:
        ret += corps_page_deconnecte()
    ret += template.afficherBasPage()
    return ret


def corps_page_deconnecte():
    html = """
    <p>Bonjour! Veuillez vous connecter.</p>
    """
    return html


def corps_page_connecte():
    html = '''
    <div class="container">
    <div class="container" ><h1 style="text-align: center;margin-bottom:15px;">Signaler un évènement</h1></div>
    <form method="post" action="reception">
        <div id="choose_compteur" style="margin-bottom:25px;">
            <h3>
                L'évènement concerne:
            </h3>
            <div style="display:inline-flex; width:100%;text-align:center;font-weight: bold;" >
                <form>
                    <div class="alpha" style="float:left;width:50%;text-decoration:bold;"><INPUT TYPE="radio" NAME= "choix" VALUE="0" CHECKED onclick="change_combo_box(this.value)">Un de vos compteur / parcelles </div>
                    <div class="alpha" style="float:right;width:50%;"><INPUT TYPE="radio" NAME= "choix" VALUE="1" onclick="change_combo_box(this.value)">Un autre compteur / parcelle </div>
                </form>
            </div>
        </div>'''

    html+=get_combo_box(0)

    html+='''
        <label for="description">Description de l'évènement :</label>

        <textarea name="description" id="description"></textarea>

        <label for="mon_fichier">Photo (tous formats | max. 5 Mo) :</label>

        <input type="hidden" name="MAX_FILE_SIZE" value="5242880" />

        <input type="file" name="mon_fichier" id="mon_fichier" />

        <br /><br />

        <input type="submit" name="submit" value="Envoyer" />
    </form>
    </div>
    '''
    return html


def recup_options(id_ex):
    options = ''
    compteurs_parc_id = exploitant.Exploitant.get_compteurs_parcelle_id(id_ex)
    for (id_compt, id_parc) in compteurs_parc_id:
        current_parc = parcelle.Parcelle(id_parc)
        current_compt = compteur.Compteur(id_compt)
        line = '<option value="{}"> '.format(id_compt) + str(id_compt) + ', ' + current_compt.nom + ': ' + current_parc.nom.capitalize() + ' </option>' + '\n'
        options += line
    return options


def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)


def reception():
    pass

def get_combo_box(opt_check = None):
    opt_check = int(opt_check)
    if not opt_check:
        options = recup_options(Session()["Id_exploitant"])
    else:
        options = recup_options(0)

    html='''
    <p id="combo_compteur_evenement"> Selectionner le compteur concerné :<select name="id_compteur">
    {0}
    </select></p>'''.format(options)
    return html
