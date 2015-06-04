template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
releve = Import('releve.py')
parcelle = Import('parcelle.py')
compteur = Import('compteur.py')
exploitant = Import('Exploitant.py')

def index(error=''):
    if "login" in Session() and not Session()["Id_exploitant"]:
        ret=template.afficherHautPage(error, titre='Consos')
    else:
        ret=template.afficherHautPage(error, titre='Ma Conso')
    if "login" in Session():
        ret += corps_page_connecte()
    else:
        ret += corps_page_deconnecte()
    ret += template.afficherBasPage()
    return ret

def corps_page_connecte2():
    html = """
        <div class="container">

            <div class="sixteen columns main-content">"""
    if Session()["Id_exploitant"]:
        html +='''<h2>Ma Consommation</h2>'''
    else:
        html += '''<h2>Consommation</h2><form>'''
        options = get_exploitant_options()
        html += '''<select id="combo_ex_conso" name="exploitants" onchange="change_exploitant_conso(this,this.selectedIndex)">
        {0}
        </select>'''.format(options)

    html += """<script>
  $(function() {
    $( "#datepicker" ).datepicker();
  });
  </script><form>
        <label for="date_debut">Date de début:</label>
        <input type="text" name="date_debut" id="date_debut" onchange="update_conso()">
        <label for="date_fin">date de fin:</label>
        <p style="display:inline-flex;"><input style="margin-right:20px;" type="text" name="Date_fin" id="date_fin" onchange="update_conso()">
        <button type="button" id="update_releves" >Ok</button></p>
    </form>"""
    html += conso_table(id_ex=1)
    html += """</div>
    </div>"""
    return html

def corps_page_connecte():
    id_compteurs =compteur.Compteur.get_compteurs_id(Session()["Id_exploitant"])
    script = '''
  <script>
  $(function() {
    $( "#date_fin" ).datepicker();
  });
  </script>
    <script>
  $(function() {
    $( "#date_debut" ).datepicker();
  });
  </script>
  
'''

    html = '''
    <div class="container">

        <aside class="six columns left-sidebar">'''

    if Session()["Id_exploitant"]:
        html +='''<h2>Ma Consommation</h2>'''
    else:
        html += '''<h2>Consommation</h2>'''
        options = get_exploitant_options()
        html += '''<select id="combo_ex_conso" name="exploitants" onchange="change_exploitant_conso(this,this.selectedIndex)">
        {0}
        </select>'''.format(options)


    html+='''<label for="date_debut">Date de début:</label>
        <input type="text" name="date_debut" id="date_debut" onchange="update_conso()">
        <label for="date_fin">Date de fin:</label>
        <p style="display:inline-flex;"><input style="margin-right:20px;" type="text" name="Date_fin" id="date_fin" onchange="update_conso()">
        <button type="button" id="update_releves" >Ok</button></p>


    </aside>


        <article class="ten columns main-content">'''
    html += conso_table(id_ex=1)
    html+='''
        <head>
    <script type="text/javascript" src="../js/jquery-2.1.3.js"></script>
    </head>
        <link rel="stylesheet" href="../stylesheets/jquery-ui.min.css">
        <script src="../js/jquery-ui.min.js"></script>
{0}

        </article>
    </div>
    '''.format(script)
    return html


def corps_page_deconnecte():
    html = """
    <div class="container">
            <div style="text-align:center;" class="sixteen columns main-content">
                <div class="sixteen columns">
                    Bonjour! Merci de vous connecter !
                </div>
            </div>
    </div>
    """
    return html

def conso_table(date_debut=None, date_fin=None, id_ex = None):
    if not id_ex:
        id_ex = Session()["Id_exploitant"]
    dico_parc_rels = get_releves(id_ex, date_debut, date_fin)    #TODO: ajouter la date de début et celle de fin.
    debut = date_debut if date_debut else 'plus ancien'
    fin = date_fin if date_fin else 'plus récent'
    html = """
    <table id="conso_content">
    <caption>Votre consommation depuis le {} jusqu'au {} :</caption>
    <tr class="titre">
        <th>Parcelle</th>
        <th>Compteur</th>
        <th>Consommation (m<sup>3</sup>)</th>
    </tr>""".format(debut, fin)
    for (i, champ) in enumerate(dico_parc_rels.keys()):
        (line,conso) = add_line(champ, dico_parc_rels[champ], i)
        html += line


    html += '</table>'
    return html


def add_line(parc, rels, i):
    '''add_line(<Parcelle>, [<Releve1>,<Releve2>, ...]'''
    conso = 0
    nom_compteur = compteur.Compteur(parc.compteur).nom
    for rel in rels:
        conso += 10 * (rel.index_fin - rel.index_deb)
        if i%2 == 1:
            parite = "impair"
        else:
            parite = "pair"

        line = """
        <tr class="{}">
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>""".format(parite, str.capitalize(parc.nom), nom_compteur, conso)
    return (line, conso)

def get_releves(Id_exploitant, date_debut=None, date_fin=None):
    releves_list = releve.Releve.get_releves_id(Id_exploitant,date_debut,date_fin)
    dico = {}           #{<Parcelle>:[<Releve1>,<Releve2>], ... }
    parcelles = {}      #{id:<Parcelle> , ...}
    for (id_releve,id_parcelle) in releves_list:
        if id_parcelle == -1:
            return dico
        if id_parcelle in parcelles.keys():
            dico[parcelles[id_parcelle]].append(releve.Releve(id_releve))
        else:
            parcelles[id_parcelle] = parcelle.Parcelle(id_parcelle)
            dico[parcelles[id_parcelle]] = [releve.Releve(id_releve)]
    return dico

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)

def get_exploitant_options():
    exploits = exploitant.Exploitant.get_all_exploitants()
    options = ''
    for ex in exploits:
        line = '<option value="{}" >'.format(ex.id) + ex.nom + '</option>\n'
        options += line
    return options