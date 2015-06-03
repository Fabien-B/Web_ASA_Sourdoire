
def afficherHautPage(error = '', titre=''):
    ret = '''
<!doctype html>
        <html lang="fr">
        <head>
            <style type="text/css"> #connect td {padding: 15px;}</style>
            <title>ASA Sourdoire</title>
            <meta http-equiv="content-type" content="text/html; charset=utf-8" />
            <meta name="language" content="FR"/>
            <meta name="viewport" content="initial-scale=1.0,width=device-width,user-scalable=yes" />
            <meta name="description" content="WEB ASA Sourdoire" />
            <link rel="stylesheet" href="../stylesheets/base.css" />
            <link rel="stylesheet" href="../stylesheets/skeleton.css" />
            <link rel="stylesheet" href="../stylesheets/layout.css" />
            <link rel="stylesheet" href="../stylesheets/flexslider.css" />
            <link rel="stylesheet" href="../stylesheets/prettyPhoto.css" />
            <link rel="stylesheet" href="../stylesheets/perso.css" />
            <link rel="stylesheet" href="../stylesheets/leaflet.css" />
            <link rel="apple-touch-icon" href="../images/favicon/apple-icon-57x57.png" />
            <link rel="apple-touch-icon" href="../images/favicon/apple-icon-60x60.png" />
            <link rel="apple-touch-icon" href="../images/favicon/apple-icon-72x72.png" />
            <link rel="apple-touch-icon" href="../images/favicon/apple-icon-76x76.png" />
            <link rel="apple-touch-icon" href="../images/favicon/apple-icon-114x114.png" />
            <link rel="apple-touch-icon" href="../images/favicon/apple-icon-120x120.png" />
            <link rel="apple-touch-icon" href="../images/favicon/apple-icon-144x144.png" />
            <link rel="apple-touch-icon" href="../images/favicon/apple-icon-152x152.png" />
            <link rel="apple-touch-icon" href="../images/favicon/apple-icon-180x180.png" />
            <link rel="icon" type="image/png" href="../images/favicon/android-icon-192x192.png" />
            <link rel="icon" type="image/png" href="../images/favicon/favicon-32x32.png" />
            <link rel="icon" type="image/png" href="../images/favicon/favicon-96x96.png" />
            <link rel="icon" type="image/png" href="../images/favicon/favicon-16x16.png" />
            <link rel="manifest" href="../images/favicon/manifest.json" />

            <link rel="Stylesheet" media="screen and (max-width: 900px)" href="../stylesheets/menu_deroulant.css" />
            <link rel="Stylesheet" media="screen and (min-width: 900px)" href="../stylesheets/menu.css" />

            <link rel="stylesheet" href="../stylesheets/jquery_ui.min.css" />
            <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
            <script type="text/javascript" src="../js/jquery-2.1.3.js"></script>
            <script type="text/javascript" src="../js/jquery.flexslider-min.js"></script>
            <script type="text/javascript" src="../js/scripts.js"></script>
            <script type="text/javascript" src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.js"></script>
            <script type="text/javascript" src="../js/jssor.js"></script>
            <script type="text/javascript" src="../js/jssor.slider.js"></script>
        <script type="text/javascript" src="../js/jquery-ui.min.js"></script>
        <style type="text/css"> input[type="text"] { float: right; margin-right: 20px;} select{ float: right; margin-right: 20px;}</style>
         <style type="text/css">
            /* jssor slider bullet navigator skin 21 css */
            /*
            .jssorb21 div           (normal)
            .jssorb21 div:hover     (normal mouseover)
            .jssorb21 .av           (active)
            .jssorb21 .av:hover     (active mouseover)
            .jssorb21 .dn           (mousedown)
            */
            .jssorb21 {
                position: absolute;
            }
            .jssorb21 div, .jssorb21 div:hover, .jssorb21 .av {
                position: absolute;
                /* size of bullet elment */
                width: 19px;
                height: 19px;
                text-align: center;
                line-height: 19px;
                color: white;
                font-size: 12px;
                background: url(../images/accueil/picture_slider/b21.png) no-repeat;
                overflow: hidden;
                cursor: pointer;
            }
            .jssorb21 div { background-position: -5px -5px; }
            .jssorb21 div:hover, .jssorb21 .av:hover { background-position: -35px -5px; }
            .jssorb21 .av { background-position: -65px -5px; }
            .jssorb21 .dn, .jssorb21 .dn:hover { background-position: -95px -5px; }
        </style>
        <style  type="text/css">
            /* jssor slider arrow navigator skin 21 css */
            /*
            .jssora21l                  (normal)
            .jssora21r                  (normal)
            .jssora21l:hover            (normal mouseover)
            .jssora21r:hover            (normal mouseover)
            .jssora21l.jssora21ldn      (mousedown)
            .jssora21r.jssora21rdn      (mousedown)
            */
            .jssora21l, .jssora21r {
                display: block;
                position: absolute;
                /* size of arrow element */
                width: 55px;
                height: 55px;
                cursor: pointer;
                background: url(../images/accueil/picture_slider/a21.png) center center no-repeat;
                overflow: hidden;
            }
            .jssora21l { background-position: -3px -33px; }
            .jssora21r { background-position: -63px -33px; }
            .jssora21l:hover { background-position: -123px -33px; }
            .jssora21r:hover { background-position: -183px -33px; }
            .jssora21l.jssora21ldn { background-position: -243px -33px; }
            .jssora21r.jssora21rdn { background-position: -303px -33px; }
        </style>
        </head>
                <div id="header" class="site-header">
                    <div class="containner sixteen columns over" >

                        <div class="three columns alpha" style="float:left; margin-top:10px;">
                            <a href="../index.py" id="logo"><img src="../images/logo.png" alt="ASA_LOGO" height="100" /></a>
                        </div>
                        <div id="login" class="four columns omega" style="float:right;margin-top:10px;">
                        ''' + afficherFormulaireConnexion(error) + '''
                        </div>

                    </div>
            <div id="header-inner" class="containner sixteen columns over" style="position: relative; margin: 0 auto; padding: 0;">
                    <div id="main-nav">
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
            ret += create_link('menu-item-9', 'Messages', titre, 'page_contact.py')
        else:   #utilisateur classique
            ret += create_link('menu-item-2', 'Ma Conso', titre,'page_conso.py')
            ret += create_link('menu-item-3', 'Entrer un relevé', titre,'page_releves.py')
            ret += create_link('menu-item-4', 'Signaler un évenement', titre,'page_evenements.py')
            ret += create_link('menu-item-5', 'Voir le réseau', titre,'page_reseau.py')
            ret += create_link('menu-item-6', 'Contacter l\'Admin', titre, 'page_contact.py')
    else:
        ret += create_link('menu-item-2', 'Voir le réseau', titre,'page_reseau.py')
        ret += create_link('menu-item-3', 'Contacter l\'Admin', titre, 'page_contact.py')

    ret += '''
</ul></li></ul>
</div></div>
            </div>'''
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
        <form id="connect" action="traiterFormulaireConnexion" METHOD="post">
            <table id ='connect' style="border-style: solid; border-width: 5px 5px 5px 5px; -moz-border-image: url(bordure.png) 5 5 5 5round; -webkit-border-image: url(bordure.png) 5 5 5 5 round; -o-border-image: url(bordure.png) 5 5 5 5 round; border-image: url(bordure.png) 5 5 5 5 fill round;background: rgba(2,0,1,0.3);">
                <tr>
                    <td>
                    <p><input name="login" size=10 maxlength=10 type="text" value="" placeholder="Identifiant" style="margin-bottom:10px;" required /></p>
                    <p><input name="password" type="password" placeholder="Mot de passe" required /></p>
                    </td>

                    <td style="text-align:center;">
                        <p><input type="submit" name="choix" value="Ok" /></p>
                    </td>
                </tr>
            </table>
        </form>
        '''

        if option == 'error':
            ret += '<div class="input-error">Login ou mot de passe incorrect</div>'

    else: # utilisateur connecte
        ret = '''
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
                        <p><input style="width:100%;" type="submit" value="Profil" /></p>
                    </form>
                    <form action="traiterFormulaireConnexion" method="post">
                        <p><input type="submit" name="choix" value="Déconnecter" /></p>
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

    if "login" in Session():
        if Session()['Id_exploitant'] == 0: #admin
            return '''
            <footer>

            <div class="footer-inner container">

                <div class="footer-columns sixteen columns">
                    <br />
                    <h2><i></i>À propos</h2>
                    <p>L'Association syndicale autorisée de la sourdoire a été crée en 1987 et rend service à 80 adhérents en permettant d'irriger plus de 180 hectares.</p>
                </div>
                <div class="footer-columns sixteen columns">
                    <table class="footer-columns sixteen columns" style="border-collapse: unset; border-spacing: 10px; padding: 5px; display: table;">
                        <tr>
                            <td>
                                <a style= "color:black;" href="../page_tuto.py">Comment utiliser ce site internet ?</a>
                            </td>
                            <td>
                                <a style= "color:black;" href="../page_conso.py">Voir ma consommation d'eau </a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <a style= "color:black;" href="../page_releves.py">Entrer ses relevés</a>
                            </td>
                            <td>
                                <a style= "color:black;" href="../page_visu_releves.py">Voir les relevés déjà entrés </a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <a style= "color:black;" href="../page_conso.py">Voir mes parcelles et les compteurs</a>
                            </td>
                            <td>
                                <a style= "color:black;" href="../page_litiges.py">Voir les éventuels conflits</a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <a style= "color:black;" href="../page_reseau.py">Consulter les bornes du réseau d'irrigation</a>
                            </td>
                            <td>
                                <a style= "color:black;" href="../page_evenements.py">Signaler un événement sur le réseau</a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <a style= "color:black;" href="../page_profil.py">Voir/Modifier ses informations personnelles</a>
                            </td>
                            <td>
                                <a style= "color:black;" href="../page_contact.py">Contacter l'administrateur</a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <a style= "color:black;" href="../page_cv.py">Voir les CV</a>
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
            </html>
               '''
        else:
            return """
            <footer>

            <div class="footer-inner container">

                <div class="footer-columns sixteen columns">
                    <br />
                    <h2><i></i>À propos</h2>
                    <p>L'Association syndicale autorisée de la sourdoire a été crée en 1987 et rend service à 80 adhérents en permettant d'irriger plus de 180 hectares.</p>
                </div>
                <div class="footer-columns sixteen columns">
                    <table class="footer-columns sixteen columns" style="border-collapse: unset; border-spacing: 10px; padding: 5px; display: table;">
                        <tr>
                            <td>
                                <a style= "color:black;" href="../page_tuto.py">Comment utiliser ce site internet ?</a>
                            </td>
                            <td>
                                <a style= "color:black;" href="../page_conso.py">Voir ma consommation d'eau </a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <a style= "color:black;" href="../page_releves.py">Entrer ses relevés</a>
                            </td>
                            <td>
                                <a style= "color:black;" href="../page_conso.py">Voir mes parcelles et les compteurs</a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <a style= "color:black;" href="../page_reseau.py">Consulter les bornes du réseau d'irrigation</a>
                            </td>
                            <td>
                                <a style= "color:black;" href="../page_evenements.py">Signaler un événement sur le réseau</a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <a style= "color:black;" href="../page_profil.py">Voir/Modifier ses informations personnelles</a>
                            </td>
                            <td>
                                <a style= "color:black;" href="../page_contact.py">Contacter l'administrateur</a>
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
            </html>
               """
    else:
        return """
            <footer>

            <div class="footer-inner container">

                <div class="footer-columns sixteen columns">
                <br />
                    <h2><i></i>À propos</h2>
                    <p>L'Association syndicale autorisée de la sourdoire a été crée en 1987 et rend service à 80 adhérents en permettant d'irriger plus de 180 hectares.</p>
                </div>
                <div class="footer-columns sixteen columns">
                    <table class="footer-columns sixteen columns" style="border-collapse: unset; border-spacing: 10px; padding: 5px; display: table; text-align: center;">
                            <td>
                                <a style= "color:black;" href="../page_contact.py">Contacter l'administrateur</a>
                            </td>
                            <td>
                                <a style= "color:black;" href="../page_reseau.py">Consulter les bornes du réseau d'irrigation</a>
                            </td>
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
            </html>
               """
