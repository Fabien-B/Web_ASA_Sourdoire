rep = 'exempleWebPython/'  # sous-repertoire d'installation de cet exemple dans www


def afficherHautPage(titre=""):
    return '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Test WEB python sous Karrigell</title>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <meta name="language" content="FR"/>
        <meta name="viewport" content="initial-scale=1.0,width=device-width,user-scalable=yes" />
        <meta name="description" content="Test python web" />
        <link rel ="stylesheet"  href="/'''+rep+'''css/monSite.css" />
        <script type="text/javascript" src="/'''+rep+'''js/jquery-2.1.3.js"></script>
        <script type="text/javascript" src="/'''+rep+'''js/monSite.js"></script>
    </head>
    <body>
        <header id="header" class="site-header" role="banner">
            <div id="header-inner" class="container sixteen columns over">
                <hgroup class="one-third column alpha">
                    <h1 id="site-title" class="site-title">
                        <a href="index.html" id="logo"><img src="images/icebrrrg-logo.png" alt="Icebrrrg logo" height="63" width="157" /></a>
                    </h1>
                </hgroup>
                <nav id="main-nav" class="two thirds column omega">
                    <ul id="main-nav-menu" class="nav-menu">
                        <li id="menu-item-1" class="current">
                            <a href="index.html">Home</a>
                        </li>
                        <li id="menu-item-2">
                            <a href="three-column.html">Three Column</a>
                        </li>
                        <li id="menu-item-3">
                            <a href="sidebar-right.html">Sidebar Right</a>
                        </li>
                        <li id="menu-item-4">
                            <a href="sidebar-left.html">Sidebar Left</a>
                        </li>
                        <li id="menu-item-5">
                            <a href="full-width.html">Full Width</a>
                        </li>
                        <li id="menu-item-6">
                            <a href="contact.html">Contact</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </header>

    '''+afficherFormulaireConnexion()


def afficherFormulaireConnexion():
    ret=""
    if "nom" in Session(): # si l'utilisateur est connecte
        ret='''
        <div id="connexion">
        <form action="traiterFormulaireConnexion" METHOD="get">
            <h1 style="display:inline-block;">'''+Session()['nom']+'''</h1> connecte  <br />
            <button name="choix" value="deconnecter"> Deconnecter </button>
        </form>
        </div>
        '''
    else: # utilisateur non connecte
        ret= '''
        <div id="connexion">
        <form action="traiterFormulaireConnexion" METHOD="get">
        <h1>Connexion</h1>
                Veuillez entrer votre login<br />
                <input name="nom" size=10 maxlength=10 type="text" value="" required /><br />
                <button name="choix" value="maj"> Ok </button>
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


