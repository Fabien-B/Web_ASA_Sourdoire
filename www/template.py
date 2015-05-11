rep = 'asa/'  # sous-repertoire d'installation de cet exemple dans www

def afficherHautPage(error = '', titre=''):
    ret = '''
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <title>Test WEB python sous Karrigell</title>
            <meta http-equiv="content-type" content="text/html; charset=utf-8" />
            <meta name="language" content="FR"/>
            <meta name="viewport" content="initial-scale=1.0,width=device-width,user-scalable=yes" />
            <meta name="description" content="Test python web" />
            <link rel="stylesheet" href="../stylesheets/base.css">
            <link rel="stylesheet" href="../stylesheets/skeleton.css">
            <link rel="stylesheet" href="../stylesheets/layout.css">
            <link rel="stylesheet" href="../stylesheets/flexslider.css">
            <link rel="stylesheet" href="../stylesheets/prettyPhoto.css">
            <link rel="stylesheet" href="../stylesheets/perso.css">
            <link rel="stylesheet" href="../stylesheets/leaflet.css">
	    <link rel="stylesheet" href="../stylesheets/jquery_ui.min.css">
            <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
            <script type="text/javascript" src="../js/jquery-2.1.3.js"></script>
            <script type="text/javascript" src="../js/jquery.flexslider-min.js"></script>
            <script type="text/javascript" src="../js/scripts.js"></script>
            <script type="text/javascript" src="../js/leaflet.js"></script>
	    <script type="text/javascript" src="../js/jquery-ui.min.js"></script>
        </head>
        <body>
            <header id="header" class="site-header" role="banner">
                <div class="sixteen columns over" style="height:80px;">
                    <div class="tree columns alpha" style="float:left; margin-top:10px;height:80px;">
                            <a href="../index.py" id="logo"><img src="../images/logo.png" alt="Icebrrrg logo" height="100" /></a>
                    </div>
                    <div class="eight columns alpha">
                </div>
                <div id="login" class="five columns omega" style="float:right;height:80px;">
                '''+afficherFormulaireConnexion(error)+'''
                </div>
            </div>
            <div id="header-inner" class="container sixteen columns over">
					<nav id="main-nav">
						<ul id="main-nav-menu" class="nav-menu">'''
    ret += create_link('menu-item-1', 'Accueil', titre,'index.py')
    ret += create_link('menu-item-2', 'Ma Conso', titre,'page_conso.py')
    ret += create_link('menu-item-3', 'Entrer un relevé', titre,'page_releves.py')
    ret += create_link('menu-item-4', 'Mes parcelles', titre,'page_parcelles.py')
    ret += create_link('menu-item-5', 'Signaler un évenement', titre,'page_evenements.py')
    ret += create_link('menu-item-6', 'Voir le réseau', titre,'page_reseau.py')
    ret += create_link('menu-item-7', 'Contacter l\'Admin', titre, 'page_contact.py')

    ret += '''          </ul>
					</nav>
            </div>
        </header>'''
    return ret

def create_link(position, titre, current_page,fichier):
    current = ' class="current"' if titre == current_page else ''
    return '''
    <li id="{0}"{1}>
        <a href="../{2}">{3}</a>
    </li>'''.format(position,current,fichier, titre)



def afficherFormulaireConnexion(error=''):

    if "login" not in Session():
        ret='''
        <form id="connect" action="traiterFormulaireConnexion" METHOD="POST">
            <br />
                <input name="login" size=10 maxlength=10 type="text" value="" placeholder="Identifiant" required />'''
        if error == 'error':
            ret += '<div class="input-error">login ou mot de passe incorrect</div>'
        ret+= '''<input type="submit" name="choix" value="Ok" />
                <div>
                    <input name="password" type="password" placeholder="Mot de passe" required />
                </div>
        '''
    else: # utilisateur connecte
        ret='''
         <div id="connexion">
         <form action="traiterFormulaireConnexion" METHOD="get">
             <h1 style="display:inline-block;">'''+Session()['nom']+'''</h1> connecte  <br />
             <button name="choix" value="deconnecter"> Deconnecter </button>
         </form>
         </div>
         '''
    return ret


def afficherBasPage():
    return '''
    <div id="bas">Exemple d'appli web  python-html / CSS / Jquery</div>
    </body>
    </html>
   '''


