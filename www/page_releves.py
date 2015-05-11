template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')

def index(error=''):
    ret=template.afficherHautPage(error, titre='Entrer un relevé')
    ret += corps_page()
    ret += template.afficherBasPage()
    return ret

def corps_page():
    html = """
    <div class="container">
    <h1 class="container sixteen columns over" style="text-align: center;margin-bottom:15px;">Entrer un relevé</h1>
		<aside class="six columns left-sidebar">
        <div class="sidebar-widget">
        <h2>Informations du relevé</h2>
        <p>Compteur :  <select name="Combo">1</select></p>
	<p>Index début :<input type="number"></p>
	<p>Index fin :<input type="number"></p>


<div>
	    <link rel="stylesheet" href="../stylesheets/jquery_ui.min.css">
  <script src="../js/jquery-1.10.2.js"></script>
  <script src="../js/jquery-ui.js"></script>
  <script>
  $(function() {
    $( "#datepicker" ).datepicker();
  });
  </script>
 
<p>Date: <input type="text" id="datepicker"></p></div>
	
        </div>        
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
