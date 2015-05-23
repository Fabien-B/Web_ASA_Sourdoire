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
            <script src="http://cdn.leafletjs.com/leaflet-0.7.3/leaflet.js"></script>
            <script type="text/javascript" src="../js/jssor.js"></script>
            <script type="text/javascript" src="../js/jssor.slider.js"></script>
        <script type="text/javascript" src="../js/jquery-ui.min.js"></script>
        </head>
        <body>
            <header id="header" class="site-header" role="banner">
                <div class="sixteen columns over" style="height:120px;">

                    <div class="tree columns alpha" style="float:left; margin-top:10px;">
                        <a href="../index.py" id="logo"><img src="../images/logo.png" alt="Icebrrrg logo" height="100" /></a>
                    </div>

                    <div class="nine columns alpha">
                    </div>

                    <div id="login" class="four columns alpha" style="float:right;margin-top:10px;">

                    '''+afficherFormulaireConnexion(error)+'''
                    </div>

                </div>
            </div>
            <div id="header-inner" class="containner sixteen columns over" style="position: relative; margin: 0 auto; padding: 0;">
                    <nav id="main-nav">
                        <ul id="main-nav-menu" class="nav-menu">'''
    ret += create_link('menu-item-1', 'Accueil', titre,'index.py')
    if "login" in Session() and Session()['Id_exploitant'] == 0:
        ret += create_link('menu-item-2', 'Consos', titre,'page_conso.py')
        ret += create_link('menu-item-3', 'Entrer un relevé', titre,'page_releves.py')
        ret += create_link('menu-item-5', 'Signaler un évènement', titre,'page_evenements.py')
        ret += create_link('menu-item-6', 'Voir le réseau', titre,'page_reseau.py')
        ret += create_link('menu-item-8', 'Gérer les membres', titre, 'page_gestion_exploitant.py')
        ret += create_link('menu-item-7', 'Demandes à l\'administrateur', titre, 'page_contact.py')
    else:
        ret += create_link('menu-item-2', 'Ma Conso', titre,'page_conso.py')
        ret += create_link('menu-item-3', 'Entrer un relevé', titre,'page_releves.py')
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


<div class="social footer-columns one-third column">
<h2><i class="icon-bullhorn icon-large"></i> Get Social</h2>
<p>Want to stalk us? That would be super:</p>
<ul>
<li><a href="http://www.twitter.com/opendesigns/"><i class="icon-twitter-sign icon-large"></i> Twitter</a></li>
<li><a href="http://www.facebook.com/opendesigns"><i class="icon-facebook-sign icon-large"></i> Facebook</a></li>
<li><a href="https://plus.google.com/b/110224753971231624818/110224753971231624818/posts"><i class="icon-google-plus-sign icon-large"></i> Google+</a></li>
</ul>
</div>

<div class="footer-columns one-third column">
<h2><i class="icon-book icon-large"></i> License</h2>
<p>Icebrrrg is free under the <a href="http://creativecommons.org/licenses/by/3/">CC3.0 license</a>, which means you can do whatever the heck you like with it - even using it commercially.  All you have to do is leave the credit link in the footer intact.  Cool?</p>

</div>

<div class="footer-columns one-third column">
<h2><i class="icon-user icon-large"></i> About Us</h2>
<p>This is where you tell the world how awesome you are.  Us?  We're Open Designs, a community of web designers offering free templates and resources to people like you to use on your own websites.  We love design, code and tinkering.  What do you love?</p>
</div>

</div>

<div id="footer-base">
<div class="container">
<div class="eight columns">
ASA Sourdoire &copy; 2015
</div>

<div class="eight columns far-edge">
Design by <a href="http://www.opendesigns.org">OD</a>
</div>
</div>
</div>

</footer>
<script src="js/jquery.prettyPhoto.js"></script>
</body>
</html>
   '''


