
def afficherHautPage(error = '', titre=''):
    ret = '''
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
            <link rel="stylesheet" href="../stylesheets/perso.css">
            <link rel="stylesheet" href="../stylesheets/leaflet.css">
            <link rel="apple-touch-icon" sizes="57x57" href="../images/favicon/apple-icon-57x57.png">
            <link rel="apple-touch-icon" sizes="60x60" href="../images/favicon/apple-icon-60x60.png">
            <link rel="apple-touch-icon" sizes="72x72" href="../images/favicon/apple-icon-72x72.png">
            <link rel="apple-touch-icon" sizes="76x76" href="../images/favicon/apple-icon-76x76.png">
            <link rel="apple-touch-icon" sizes="114x114" href="../images/favicon/apple-icon-114x114.png">
            <link rel="apple-touch-icon" sizes="120x120" href="../images/favicon/apple-icon-120x120.png">
            <link rel="apple-touch-icon" sizes="144x144" href="../images/favicon/apple-icon-144x144.png">
            <link rel="apple-touch-icon" sizes="152x152" href="../images/favicon/apple-icon-152x152.png">
            <link rel="apple-touch-icon" sizes="180x180" href="../images/favicon/apple-icon-180x180.png">
            <link rel="icon" type="image/png" sizes="192x192"  href="../images/favicon/android-icon-192x192.png">
            <link rel="icon" type="image/png" sizes="32x32" href="../images/favicon/favicon-32x32.png">
            <link rel="icon" type="image/png" sizes="96x96" href="../images/favicon/favicon-96x96.png">
            <link rel="icon" type="image/png" sizes="16x16" href="../images/favicon/favicon-16x16.png">
            <link rel="manifest" href="../images/favicon/manifest.json">

            <link rel="Stylesheet" media="screen and (max-width: 900px)" href="../stylesheets/menu_deroulant.css" />
            <link rel="Stylesheet" media="screen and (min-width: 900px)" href="../stylesheets/menu.css" />

            <link rel="stylesheet" href="../stylesheets/jquery_ui.min.css">
            <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
            <script type="text/javascript" src="../js/jquery-2.1.3.js"></script>
            <script type="text/javascript" src="../js/jquery.flexslider-min.js"></script>
            <script type="text/javascript" src="../js/scripts.js"></script>
            <script src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.js"></script>
            <script type="text/javascript" src="../js/jssor.js"></script>
            <script type="text/javascript" src="../js/jssor.slider.js"></script>
        <script type="text/javascript" src="../js/jquery-ui.min.js"></script>
        </head>
        <body>
            <header id="header" class="site-header" role="banner">
                <div class="containner sixteen columns over" >

                    <div class="three columns alpha" style="float:left; margin-top:10px;">
                        <a href="../index.py" id="logo"><img src="../images/logo.png" alt="Icebrrrg logo" height="100" /></a>
                    </div>
                    <div id="login" class="four columns omega" style="float:right;margin-top:10px;">
                    ''' + afficherFormulaireConnexion(error) + '''
                    </div>

                </div>
            <div id="header-inner" class="containner sixteen columns over" style="position: relative; margin: 0 auto; padding: 0;">
                    <nav id="main-nav">
                        <ul id="main-nav-menu" class="nav-menu">
                        <li><a href="#" id='menu_der' style="height:0px;">Menu</a>
                            <a href="#" id='menu'></a>
                        <ul>'''
    ret += create_link('menu-item-1', 'Accueil', titre,'index.py')
    if "login" in Session():
        if Session()['Id_exploitant'] == 0: #admin
            ret += create_link('menu-item-2', 'Consos', titre,'page_conso.py')
            ret += create_link('menu-item-3', 'Entrer un relevé', titre,'page_releves.py')
            ret += create_link('menu-item-4', 'Voir les relevés', titre,'page_visu_releves.py')
            ret += create_link('menu-item-5', 'Signaler un évènement', titre,'page_evenements.py')
            ret += create_link('menu-item-6', 'Litiges', titre,'page_litiges.py')
            ret += create_link('menu-item-7', 'Voir le réseau', titre,'page_reseau.py')
            ret += create_link('menu-item-8', 'Gérer les membres', titre, 'page_gestion_exploitant.py')
            ret += create_link('menu-item-9', 'Demandes à l\'administrateur', titre, 'page_contact.py')
            ret += create_link('menu-item-10', 'Page cv', titre, 'page_cv.py')
        else:   #utilisateur classique
            ret += create_link('menu-item-2', 'Ma Conso', titre,'page_conso.py')
            ret += create_link('menu-item-3', 'Entrer un relevé', titre,'page_releves.py')
            ret += create_link('menu-item-4', 'Signaler un évenement', titre,'page_evenements.py')
            ret += create_link('menu-item-5', 'Voir le réseau', titre,'page_reseau.py')
            ret += create_link('menu-item-6', 'Contacter l\'Admin', titre, 'page_contact.py')
    else:
        ret += create_link('menu-item-2', 'Voir le réseau', titre,'page_reseau.py')
        ret += create_link('menu-item-3', 'Contacter l\'Admin', titre, 'page_contact.py')

    ret += '''          </ul></ul>
                    </nav>
            </div>
        </header>'''
    if error != "":
        ret +='''<BODY onLoad="alert('{}')">
'''.format(error)
    return ret

def create_link(position, titre, current_page,fichier):
    current = ' class="current"' if titre == current_page else ''
    return '''
    <li id="{0}"{1}>
        <a href="../{2}">{3}</a>
    </li>'''.format(position,current,fichier, titre)



def afficherFormulaireConnexion(option=''):

    if "login" not in Session():
        ret='''
        <style> #connect td {padding: 10px;}</style>
        <form id="connect" action="traiterFormulaireConnexion" METHOD="POST">
            <table id ='connect' style="border-style: solid; border-width: 5px 5px 5px 5px; -moz-border-image: url(bordure.png) 5 5 5 5round; -webkit-border-image: url(bordure.png) 5 5 5 5 round; -o-border-image: url(bordure.png) 5 5 5 5 round; border-image: url(bordure.png) 5 5 5 5 fill round;background: rgba(2,0,1,0.3);">
                <tr>
                    <td>
                    <input name="login" size=10 maxlength=10 type="text" value="" placeholder="Identifiant" style="margin-bottom:10px;" required />
                    <input name="password" type="password" placeholder="Mot de passe" required />
                    </td>

                    <td style="text-align:center;">
                        <input type="submit" name="choix" value="Ok" />
                    </td>
                </tr>
            </table>
        </form>
        '''

        if option == 'error':
            ret += '<div class="input-error">Login ou mot de passe incorrect</div>'

    else: # utilisateur connecte
        ret = '''
        <style> #connect td {padding: 15px;}</style>


         <table id ='connect' style="
                    border-style: solid;
border-width: 5px 5px 5px 5px;
-moz-border-image: url(bordure.png) 5 5 5 5round;
-webkit-border-image: url(bordure.png) 5 5 5 5 round;
-o-border-image: url(bordure.png) 5 5 5 5 round;
border-image: url(bordure.png) 5 5 5 5 fill round;background: rgba(2,0,1,0.3);">
            <tr>
                <td>
                <div></div>
                <h2 style="display: inherit;text-align:center;width:100%;">'''+Session()['nom']+'''</h2>
                </td>

                <td style="text-align:center;">
                    <form style="margin-bottom:10px;" action="../page_profil.py">
                        <input style="width:100%;" type="submit" value="Profil" />
                    </form>
                    <form action="traiterFormulaireConnexion" method="POST">
                        <input type="submit" name="choix" value="Déconnecter">
                    </form>
                </td>
            </tr>
        </table>
         '''
        if option == "profilUpdated":
            ret+='''
            <div class="greetings">Profil mis à jour</div>
            '''
    return ret


def afficherBasPage():
    return '''
<footer>

<div class="footer-inner container">

    <div class="footer-columns sixteen columns">
        <h2><i></i>À propos</h2>
        <p>L'Association syndicale autorisée de la sourdoire a été crée en 1973 et irrigue plus de 75356 hectares.</p>
    </div>
    <div class="footer-columns sixteen columns">
        <table style="border-collapse: unset; border-spacing: 10px;">
            <tr>
                <td>
                    <a href="../page_tuto.py">Comment utiliser ce site internet ?</a>
                </td>
                <td>
                    <a href="../page_conso.py">Voir ma consommation d'eau sur mes parcelles</aW
                </td>
            </tr>
            <tr>
                <td>
                    <a href="../page_releves.py">Entrer ses relevés</a>
                </td>
                <td>
                    <a href="../page_visu_releves.py">Voir les relevés déjà entrés</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="../page_parcelles.py">Voir mes parcelles et les compteurs</a>
                </td>
                <td>
                    <a href="../page_litiges.py">Voir les éventuels conflits dans lesquels vous êtes impliqué(e)</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="../page_reseau.py">Consulter les bornes du réseau d'irrigation</a>
                </td>
                <td>
                    <a href="../page_evenements.py">Voir les événements sur le réseau</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="../page_profil.py">Voir/Modifier ses informations personnelles</a>
                </td>
                <td>
                    <a href="../page_contact.py">Contacter l'administrateur du réseau d'irrigation</a>
                </td>
            </tr>
        </table>
    </div>
</div>

<div id="footer-base">
<div class="container">
<div class="eight columns">
ASA Sourdoire &copy; 2015
</div>
</div>
</div>

</footer>
<script src="js/jquery.prettyPhoto.js"></script>
</body>
</html>
   '''


