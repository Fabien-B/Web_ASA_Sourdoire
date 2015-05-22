template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
releve = Import('releve.py')
parcelle = Import('parcelle.py')
compteur = Import('compteur.py')

def index(error=''):
    ret=template.afficherHautPage(error, titre='Ma Conso')
    if "login" in Session():
        ret += corps_page_connecte()
    else:
        ret += corps_page_deconnecte()
    ret += template.afficherBasPage()
    return ret


def corps_page_connecte():
    html = """<div class="container">
            <div class="sixteen columns main-content">
    <h2>Ma Consommation</h2>
    <form>
        <label for="date_debut">Date de début:</label>
        <input type="date" name="date_debut" id="date_debut">
        <label for="date_fin" placeholder="2020-01-01">Date de fin:</label>
        <input type="date" name="date_fin" id="date_fin">
        <button type="button" id="update_releves" >Ok</button>
    </form>

    """
    html += conso_table()
    return html

def corps_page_deconnecte():
    html = """
    <p>Bonjour! Veuillez vous connecter.</p>
    """
    return html

def conso_table(date_debut=None, date_fin=None):
    dico_parc_rels = get_releves(Session()["Id_exploitant"], date_debut, date_fin)    #TODO: ajouter la date de début et celle de fin.
    debut = date_debut if date_debut else 'plus ancien'
    fin = date_fin if date_fin else 'plus récent'
    html = """
    <table id="conso_content">
    <caption>Votre consommation depuis le {} jusqu'au {} :</caption>
    <tr class="titre">
        <th>Parcelle</th>
        <th>Compteur</th>
        <th>Consommation</th>
    </tr>""".format(debut, fin)
    for (i, champ) in enumerate(dico_parc_rels.keys()):
        (line,conso) = add_line(champ, dico_parc_rels[champ], i)
        html += line


    html += '</table>'
    html += """<div><link rel="stylesheet" href="../stylesheets/jquery-ui.min.css">
        <link rel="stylesheet" href="../stylesheets/jquery.ui.timepicker.css">
        <script src="../js/jquery-ui.min.js"></script>
        <script src="../js/jquery.ui.timepicker.js"></script>
        <script>
  $(function() {
    $( "#date_debut" ).datepicker();
  });
  $(function() {
    $( "#date_fin" ).datepicker();
  });
  </script></div>"""
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
        if id_parcelle in parcelles.keys():
            dico[parcelles[id_parcelle]].append(releve.Releve(id_releve))
        else:
            parcelles[id_parcelle] = parcelle.Parcelle(id_parcelle)
            dico[parcelles[id_parcelle]] = [releve.Releve(id_releve)]
    return dico

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)
