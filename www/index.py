template = Import('template.py' ) # import du fichier template (entete, pieds de page...)

# fonctions CONTROLEUR (calculs, maj base, MAIS PAS D'AFFICHAGE)
def index(message=''):
    ret=template.afficherHautPage()
    ret += afficherAccueil()
    ret += template.afficherBasPage()
    return ret

def traiterFormulaireConnexion(choix, login='',password=''):
    if choix=='deconnecter':
        if "login" in Session(): del Session()["login"]
        return index('Deconnecte')
    else:
        if password != 'test':
            Session()["login"] = login;
            return  index('Login Ok <b>'+login+'</b><br/>Vous pouvez modifier')
        else:
            return index('login incorrect!')



# fonctions AFFICHAGE
def afficherAccueil():
    ret=template.afficherHautPage()
    ret+='''
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

