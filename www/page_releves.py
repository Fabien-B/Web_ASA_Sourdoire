exploitant = Import('Exploitant.py')

template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')

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
    option = recup_options()
    script='''<script>
  $(function() {
    $( "#datepicker" ).datepicker();
  });
  </script>'''
    style='''<style> input[type="text"] { float: right; margin-right: 20px;} select{ float: right; margin-right: 20px;}</style>'''
    html = """
    {2}
    <div class="container">
    <h1 class="container sixteen columns over" style="text-align: center;margin-bottom:15px;">Entrer un relevé</h1>
        <aside class="six columns left-sidebar">
        <div class="sidebar-widget">
        <h2 style='margin-bottom:30px'>Informations du relevé :</h2>
        <p>Compteur :  
        <select name="Combo">
        {0}
        </select></p>
    <p>Index début :<input type="text"></p>
    <p>Index fin :<input type="text"></p>
{1}
<p>Date : <input type="text" id="datepicker"></p>
<p style='float:right; margin-right:20px;'><input type="submit" name="submit" value="Valider" /></p>
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
        <link rel="stylesheet" href="../datepicker/jquery-ui.min.css">
  <script src="../datepicker/jquery-1.10.2.js"></script>
  <script src="../datepicker/jquery-ui.min.js"></script>

{1}
</html>
      
        </article>
        <!-- End main Content -->
      
    
    </div>
    """.format(option, script, style)
    return html


def recup_options():
    myexploitant = exploitant.Exploitant(Session()["Id_exploitant"])
    login = myexploitant.login
    option = []
    info = exploitant.Exploitant.get_his_parcelle(login)
    for (x, y) in info:
        option.append('<option> '+x + ', ' + str.capitalize(str(y)) + ' </option>')
    option = str(option).replace("',", "'\n").replace("'", "").replace("[", "").replace("]", "")
    return option


def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)
