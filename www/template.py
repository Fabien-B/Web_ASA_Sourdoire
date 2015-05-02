rep = 'exempleWebPython/'  # sous-repertoire d'installation de cet exemple dans www


def afficherHautPage(titre=""):
    return '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>ASA Sourdoire</title>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <meta name="language" content="FR"/>
        <meta name="viewport" content="initial-scale=1.0,width=device-width,user-scalable=yes" />
        <meta name="description" content="Test python web" />
        <link rel="stylesheet" href="../stylesheets/base.css">
        <link rel="stylesheet" href="../stylesheets/skeleton.css">
        <link rel="stylesheet" href="../stylesheets/layout.css">
        <link rel="stylesheet" href="../stylesheets/flexslider.css">
        <link rel="stylesheet" href="../stylesheets/prettyPhoto.css">
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
        <script src="../js/jquery.flexslider-min.js"></script>
        <script src="../js/scripts.js"></script>

    </head>
    <body>
        <header id="header" class="site-header" role="banner">
            <div id="header-inner" class="container sixteen columns over">
                <hgroup class="two columns alpha">
                    <h1 id="site-title" class="site-title">
<<<<<<< HEAD
                        <a href="index.html" id="logo"><img src="images/accueil1.jpeg" alt="Icebrrrg logo" height="63" width="157" /></a>
=======
                        <a href="index" id="logo"><img src="images/icebrrrg-logo.png" alt="Icebrrrg logo" height="63" width="157" /></a>
>>>>>>> 74bc1534cdc2f79c9364fb0abbcb42ba039c7952
                    </h1>
                </hgroup>
                <nav id="main-nav" class="eleven columns alpha">
                    <ul id="main-nav-menu" class="nav-menu">
                        <li id="menu-item-1" class="current">
                            <a href="index.html">Accueil</a>
                        </li>
                        <li id="menu-item-2">
                            <a href="three-column.html">Ma Conso</a>
                        </li>
                        <li id="menu-item-3">
                            <a href="sidebar-right.html">Entrer un relevé</a>
                        </li>
                        <li id="menu-item-4">
                            <a href="sidebar-left.html">Mes Parcelles</a>
                        </li>
                        <li id="menu-item-5">
                            <a href="full-width.html">Signaler un évenement</a>
                        </li>
                        <li id="menu-item-6">
                            <a href="plop.py">Voir le Réseau</a>
                        </li>
                        <li id="menu-item-7">
                            <a href="contact.py">Contacter l'Admin</a>
                    </ul>
                </nav>
                <div id="login" class="three columns omega">
                '''+afficherFormulaireConnexion()+'''
                </div>
            </div>
        </header>

    '''


def afficherFormulaireConnexion():

    if "login" not in Session():
        ret='''
        <form id="connect" action="traiterFormulaireConnexion" METHOD="get">
            <br />
                <input name="nom" size=10 maxlength=10 type="text" value="" placeholder="Identifiant" required />
                <input type="submit" name="connect" value="Ok" />
                <div>
                    <input type="password" placeholder="Mot de passe" required />
                </div>
        '''
    else: # utilisateur non connecte
        ret='''
         <div id="connexion">
         <form action="traiterFormulaireConnexion" METHOD="get">
             <h1 style="display:inline-block;">'''+Session()['login']+'''</h1> connecte  <br />
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


