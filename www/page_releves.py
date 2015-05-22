exploitant = Import('Exploitant.py')
compteur = Import('compteur.py')
releve = Import('releve.py')
template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
parcelle = Import('parcelle.py')
import mysql.connector
import datetime

def index(error=''):
    ret=template.afficherHautPage(error, titre='Entrer un relevé')
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
    id_compteurs =compteur.Compteur.get_compteurs_id(Session()["Id_exploitant"])
    script = '''<script>
  $(function() {
    $( "#datepicker" ).datepicker();
  });
  </script>
  <script>
  $(function() {
    $( "#timepicker" ).timepicker();
  });
  </script>
'''

    style='''<style> input[type="text"] { float: right; margin-right: 20px;} select{ float: right; margin-right: 20px;}</style>'''

    html = """
    {0}
    <div class="container">
    <h1 class="container sixteen columns over" style="text-align: center;margin-bottom:15px;">Entrer un relevé</h1>
        <aside class="six columns left-sidebar">
        <form action="ajout_releve" method="GET">
        <div class="sidebar-widget">
        <h2 style='margin-bottom:30px'>Informations du relevé :</h2>""".format(style)

    if not Session()["Id_exploitant"]:
        options_exploitant = get_options_exploitant()
        html +='''<p>Exploitant :
            <select id="combo_exploitant_releves" name="id_exploitant" onchange="update_exploitant_releve(this,this.selectedIndex)">
            {0}
            </select></p>'''.format(options_exploitant)

    html += get_compteur_combo_box(Session()["Id_exploitant"])

    html += part_index_debut(id_compteurs[0])
    verif = ''
    if Session()["Id_exploitant"]:
        verif = ' required onblur="verif_releve(this)"'

    html += '''<p>Index fin :<input name="index_fin" type="text"{0}></p>
            <p>Date : <input name="date" type="text" id="datepicker" required></p>
            <p>Heure : <input name="time" type="text" id="timepicker" required></p>
            <p style='float:right; margin-right:20px;'><input type="submit" name="submit" value="Valider" /></p>
            </form>
            </aside>
        <!-- End Left Sidebar -->


        <article class="ten columns main-content">
        <html>
    <head>
    <link rel="stylesheet" href="../stylesheets/leaflet.css" />
    <script type="text/javascript" src="../js/jquery-2.1.3.js"></script>
    <script src="../js/leaflet.js"></script>
    </head>

    <div>
        <div id="map" style="width: 100%; height: 400px"></div>
        <script type="text/javascript" src="../js/map.js"></script>
        <script type="text/javascript" src="../js/map_releves.js"></script>
    </div>
        <link rel="stylesheet" href="../stylesheets/jquery-ui.min.css">
        <link rel="stylesheet" href="../stylesheets/jquery.ui.timepicker.css">
        <script src="../js/jquery-ui.min.js"></script>
        <script src="../js/jquery.ui.timepicker.js"></script>
{1}
</html>
      
        </article>
        <!-- End main Content -->
    </div>
    '''.format(verif,script)
    return html

def part_index_debut(id_compteur=0):
    index = compteur.Compteur.get_last_index(id_compteur)
    html = '''
    <p id="index_debut_releves">Index début :
    <input id="index_debut" name="index_debut" type="text" value="{0}" required></p>
    '''.format(index)
    return html

def ajout_releve(id_compteur, index_debut, index_fin, date, time, submit):
    (index_debut,index_fin) = (int(index_debut),int(index_fin))
    if (index_fin - index_debut) < 0 and Session()["Id_exploitant"]:    #releve négatif autorisé pour l'admin.
        return index('IndexError')
    myreleve = releve.Releve(0)
    myreleve.compteur = int(id_compteur)
    myreleve.index_deb = index_debut
    myreleve.index_fin = index_fin
    myreleve.date = str(date + ' ' + time)
    if Session()["Id_exploitant"]:
        myreleve.exploitant = Session()["Id_exploitant"]
    else:   #administrateur
        myreleve.exploitant = 0#################################################################################################################################################################################
    myreleve.save()
    return index('Profil actualisé')

def recup_options(id_ex):
    options = ''
    compteurs_parc_id = compteur.Compteur.get_compteurs_parcelle_id(id_ex)
    for (id_compt, id_parc) in compteurs_parc_id:
        current_parc = parcelle.Parcelle(id_parc)
        current_compt = compteur.Compteur(id_compt)
        line = '<option value="{}"> '.format(id_compt) + str(id_compt) + ', ' + current_compt.nom + ': ' + current_parc.nom.capitalize() + ' </option>' + '\n'
        options += line
    return options

def get_options_exploitant():
    options = '<option value="0">0 - ADMINISTRATEUR</option>\n'
    exploitant_list = exploitant.Exploitant.get_all_exploitants()
    for exploit in exploitant_list:
        options += '<option value="'+str(exploit.id)+'">'+str(exploit.id)+' - '+exploit.nom+'</option>\n'
    return options

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)

def get_compteur_combo_box(id_ex):
    html = """<p>Compteur :
        <select id="combo_compteur_releves" name="id_compteur" onchange="update_index_deb_releve(this.selectedIndex)">
        {0}
        </select></p>""".format(recup_options(id_ex))
    return html