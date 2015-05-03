template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')

def index(error=''):
    ret=template.afficherHautPage(error, titre='Accueil')
    ret += afficherAccueil()
    ret += template.afficherBasPage()
    return ret

def corps_accueil():
    html = """
    <p>Un petit paragraphe</p>
    """
    return html

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)   #le 1er paramètre est la référence sur la fonction à appeler



# fonctions AFFICHAGE
def afficherAccueil():
    ret='''
        <div class="container">
            <div class="sixteen columns">
                <div class="flex-container">
                    <div class="flexslider">
                        <ul class="slides">
                            <li>
                                <a href="#"><img src="../images/accueil1.jpeg" alt="Random Penguin Photo" /></a>
                                <div class="flex-caption">
                                    <h5><a href="#">Fully Responsive</a></h5>
                                    <p>Icebrrrg adapts to any screen size to optimize your user's experience.</p>
                                   </div>
                            </li>
                            <li>
                                <a href="#"><img src="images/penguin2.jpeg" alt="Random Penguin Photo" /></a>
                                <div class="flex-caption" style="display:none;">
                                    <h5><a href="#">Multiple layouts</a></h5>
                                    <p>Easily create multiple different layouts with the simple grid setup - one column, two column, three column, more.</p>
                                </div>
                            </li>
                            <li>
                                <a href="#"><img src="images/penguin3.jpeg" alt="Random Penguin Photo" /></a>
                                <div class="flex-caption" style="display:none;">
                                    <h5><a href="#">Contact form</a></h5>
                                    <p>Not a developer? No problem. Icebrrrg comes complete with a PHP contact form ready to rock.</p>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        '''
    return ret

