exploitant = Import('Exploitant.py')
releve = Import('releve.py')
template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
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
    option = recup_options()[0]
    nom_compteur = recup_options()[1]
    try:
        index_debut = get_last_index(nom_compteur[0])
    except IndexError:
        index_debut = 0
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
    {2}
    <div class="container">
    <h1 class="container sixteen columns over" style="text-align: center;margin-bottom:15px;">Entrer un relevé</h1>
        <aside class="six columns left-sidebar">
        <form action="ajout_releve" method="GET">
        <div class="sidebar-widget">
        <h2 style='margin-bottom:30px'>Informations du relevé :</h2>
        <p>Compteur :  
        <select name="compteur">
        {0}
        </select></p>
    <p>Index début :
    <input name="index_debut" type="text" value="{3}" required></p>
    <p>Index fin :<input name="index_fin" type="text" required></p>

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
        <script type="text/javascript" src="../js/map_content.js"></script>
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
    """.format(option, script, style, index_debut)
    return html


def ajout_releve(compteur , index_debut, index_fin, date, time, submit):
    myexploitant = exploitant.Exploitant(Session()["Id_exploitant"])
    id_compteur = get_id_compteur_from_nom(compteur)
    myreleve = releve.Releve(0)
    myreleve.id = 0
    myreleve.compteur = id_compteur
    myreleve.index_deb = index_debut
    myreleve.index_fin = index_fin
    myreleve.date = str(date + ' ' + time)
    myreleve.exploitant = myexploitant.id
    myreleve.save()
    return index('Profil actualisé')


def recup_options():
    myexploitant = exploitant.Exploitant(Session()["Id_exploitant"])
    login = myexploitant.login
    option = []
    compteurs = []
    info = exploitant.Exploitant.get_his_parcelle(login)
    for (x, y) in info:
        option.append('<option> ' + x + ', ' + str.capitalize(str(y)) + ' </option>')
        compteurs.append(str(x))
    option = str(option).replace("',", "'\n").replace("'", "").replace("[", "").replace("]", "")
    return option, compteurs


def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)

def get_id_compteur_from_nom(nom):
    nom = nom.split()[0].replace(",", "")
    connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='asa')
    curseur = connection.cursor()
    requete = 'select Id_compteur as id from Compteur where Nom="{}";'.format(nom)
    curseur.execute(requete)
    id = curseur.fetchall()[0][0]
    return id

def get_last_index(nom_compteur):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='asa')
        curseur = connection.cursor()
        requete ='''select max(Index_fin) from Releve where Compteur in (select Id_compteur as id from Compteur where Nom="{}");'''.format(nom_compteur)
        curseur.execute(requete)
        result = curseur.fetchall()[0][0]
        return result
