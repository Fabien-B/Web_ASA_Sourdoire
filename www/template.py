rep = 'exempleWebPython/'  # sous-repertoire d'installation de cet exemple dans www


def afficherHautPage(error = ''):
    return '''
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
        <script type="text/javascript" src="/'''+rep+'''js/jquery-2.1.3.js"></script>
        <script type="text/javascript" src="/'''+rep+'''js/monSite.js"></script>
    </head>
    <body>
        <header id="header" class="site-header" role="banner">
            <div id="header-inner" class="container sixteen columns over">
                <hgroup class="four columns alpha">
                    <h1 id="site-title" class="site-title">
                        <a href="index" id="logo"><img src="images/icebrrrg-logo.png" alt="Icebrrrg logo" height="63" width="157" /></a>
                    </h1>
                </hgroup>
                <nav id="main-nav" class="eight columns alpha">
                    <ul id="main-nav-menu" class="nav-menu">
                        <li id="menu-item-1" class="current">
                            <a href="index.html">Accueil</a>
                        </li>
                        <li id="menu-item-2">
                            <a href="three-column.html">Ma Conso</a>
                        </li>
                        <li id="menu-item-3">
                            <a href="sidebar-right.html">Relevés</a>
                        </li>
                        <li id="menu-item-4">
                            <a href="sidebar-left.html">Évènements</a>
                        </li>
                        <li id="menu-item-5">
                            <a href="full-width.html">Le Réseau</a>
                        </li>
                        <li id="menu-item-6">
                        </li>
                    </ul>
                </nav>
                <div id="login" class="four columns omega">
                '''+afficherFormulaireConnexion(error)+'''
                </div>
            </div>
        </header>

    '''


def afficherFormulaireConnexion(error = ''):
    if "login" not in Session():
        ret= '''
        <div id="connexion">
        <form action="traiterFormulaireConnexion" METHOD="get">
        <br />
            <input name="login" size=10 maxlength=10 type="text" value="" placeholder="Identifiant" required />
            '''
        if error == 'error':
            ret += '<div class="input-error">login ou mot de passe incorrect</div>'
        ret += '''<input name="choix" type="submit" value="Ok" style="float: right" />
            <div style="overflow: hidden; padding-right: .5em;">
                <input name="password" type="password" style="width: 100%;" placeholder="Mot de passe" required />
            </div>

        </form>
        </div>
        '''
    else:
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


