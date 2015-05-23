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
    options = recup_options()
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

    style='''<style> input[type="text"] { float: right; margin-right: 20px;} select{ float: right; margin-right: 20px;} p{margin-bottom:35px;}</style>'''

    html = """
    {0}
    <div class="container">
    <h1 class="container sixteen columns over" style="text-align: center;margin-bottom:15px;">Entrer un relevé</h1>
        <aside class="six columns left-sidebar">
        <form action="ajout_releve" method="GET">
        <div class="sidebar-widget">
        <h2 style='margin-bottom:30px'>Informations du relevé :</h2>
        <p>Compteur :
        <select id="combo_compteur_releves" name="id_compteur" onchange="update_index_deb_releve(this.selectedIndex)">
        {1}
        </select></p>""".format(style,options)

    html += part_index_debut(id_compteurs[0])

    html += '''<p>Index fin :<input name="index_fin" type="text" required></p>
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
{0}
</html>
      
        </article>
        <!-- End main Content -->
      

    </div>
    '''.format(script)
    return html


def part_index_debut(id_compteur=0):
    index = compteur.Compteur.get_last_index(id_compteur)
    html = '''
    <p id="index_debut_releves">Index début :
    <input name="index_debut" type="text" value="{0}" required></p>
    '''.format(index)
    return html


def ajout_releve(id_compteur, index_debut, index_fin, date, time, submit):
    myreleve = releve.Releve(0)
    myreleve.compteur = int(id_compteur)
    myreleve.index_deb = index_debut    #todo: vérifier la cohérence
    myreleve.index_fin = index_fin
    myreleve.date = str(date + ' ' + time)
    myreleve.exploitant = Session()["Id_exploitant"]
    myreleve.save()
    return index('Profil actualisé')


def recup_options():
    options = ''
    compteurs_parc_id = compteur.Compteur.get_compteurs_parcelle_id(Session()["Id_exploitant"])
    for (id_compt, id_parc) in compteurs_parc_id:
        current_parc = parcelle.Parcelle(id_parc)
        current_compt = compteur.Compteur(id_compt)
        line = '<option value="{}"> '.format(id_compt) + str(id_compt) + ', ' + current_compt.nom + ': ' + current_parc.nom.capitalize() + ' </option>' + '\n'
        options += line
    return options


def traiterFormulaireConnexion(choix, login='', password=''):
    return connexion.Connexion(index, choix, login, password)
