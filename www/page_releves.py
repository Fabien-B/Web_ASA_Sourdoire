template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')

def index(error=''):
    ret=template.afficherHautPage(error, titre='Ma Conso')
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

def corps_page_connecte(date_debut=None, date_fin=None):
    html = """
    <div class="container">
    <h1 class="container sixteen columns over" style="text-align: center;margin-bottom:15px;">Entrer un relevé</h1>
		<aside class="six columns left-sidebar">
        <div class="sidebar-widget">
        <h2>Informations du relevé</h2>
        <p>Compteur :  <select name="Combo">1</select></p>
	<p>Index début :<input type="text"></p>
	<p>Index fin :<input type="text"></p>



<p>Date: <input type="text" id="datepicker"></p>   
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
</html>
      
        </article>
        <!-- End main Content -->
      
    
    </div>
    """
    return html

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)
