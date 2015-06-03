template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')

def index(error=''):
    ret=template.afficherHautPage(error, titre='Accueil')
    ret += afficherAccueil()
    ret += corps_accueil()
    ret += template.afficherBasPage()
    return ret

def corps_accueil():
    html = """
        <div class="container">
            <div class="sixteen columns main-content">
                <div class="sixteen columns">
                    <div class="tagline">
                        <p>Bienvenue sur le site de l'<strong>ASA Sourdoire</strong>, le site de gestion de l'irrigation par internet.<br />
                        Simple. Minimal. Easy-to-use.</p>
                    </div>
                    <hr />
                    <p style ="font-size: large; text-align: justify;">(Re)Découvrez l'ASA Sourdoire désormais connecté ! Vous pouvez désormais rentrer vos relevés de chez vous par internet,
                     votre consommation est alors mise à jour en direct, et les dialogues avec le gestionnaire sont désormais plus simples.</p>
                     <br />
                    <hr />
                    <section><div class="container">

        <div class="one-third column" style ="text-align: center;" >
        <img src="../images/logo_conso.png" height="60px" alt="logo_conso" />
            <h3> Consommation</h3>
            <p style ="text-align: justify;">Vous pouvez consulter votre consommation quand vous voulez, suivre l'évolution de celle ci et garder un suivi personnalisé de vos bornes et parcelles.</p>
        </div>
        <div class="one-third column" style ="text-align: center;">
        <img src="../images/logo_releve.png" height="60px" alt="logo_releve" />
            <h3> Finie la galère des relevés </h3>
            <p style ="text-align: justify;">Grâce à ce nouveau système vous pouvez entrer vous même un relevé, plus besoin d'intermédiaire !</p>
        </div>
        <div class="one-third column" style ="text-align: center;">
        <img src="../images/signal.png" height="60px" alt="signal" />
            <h3> Signalez les problèmes</h3>
            <p style ="text-align: justify;">Maintenant vous pouvez signalez quand il y a un soucis sur une des bornes, un relevé, consulter l'état du réseau et bien plus encore...</p>
        </div>

        </div></section>

                     <br/>
                     <fieldset>
                        <legend style="font-size:20px; margin-bottom:20px; margin-top:10px;">Aide</legend>
                        <p>Commencez à l'utiliser dès maintenant ! Si vous rencontrez des difficultés, consultez nos tutoriels vidéo en <a href="../page_tuto.py">cliquant ici !</a></p>
                    </fieldset>
                </div>
            </div>
        </div>
    """
    return html

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)   #le 1er paramètre est la référence sur la fonction à appeler

# fonctions AFFICHAGE
def afficherAccueil():
    ret='''
        <div style="padding:0px; margin:0px; font-family:Arial, Verdana;background-color:#fff;">

    <script type="text/javascript" src="../js/jssor.js"></script>
    <script type="text/javascript" src="../js/jssor.slider.js"></script>
    <script type="text/javascript" src="../js/jquery-2.1.3.js"></script>
    <script type="text/javascript" src="../js/picture_slider.js"></script>

    <!-- Jssor Slider Begin -->
    <!-- To move inline styles to css file/block, please specify a class name for each element. -->
    <div id="slider1_container" style="position: relative; margin: 0 auto;
        top: 0px; left: 0px; width: 1300px; height: 300px; overflow: hidden; max-height:300px; margin-top:-30px;">
        <!-- Loading Screen -->
        <div id="loading" style="position: absolute; top: 0px; left: 0px;">
            <div style="filter: alpha(opacity=70); opacity: 0.7; position: absolute; display: block;
                top: 0px; left: 0px; width: 100%; height: 100%;">
            </div>
            <div style="position: absolute; display: block; background: url(../images/accueil/picture_slider/loading.gif) no-repeat center center;
                top: 0px; left: 0px; width: 100%; height: 100%;">
            </div>
        </div>
        <!-- Slides Container -->
        <div u="slides" style="cursor: move; position: absolute; left: 0px; top: 0px; width: 1300px;
            height: 300px; overflow: hidden;">


            <div>
                <img u="image" src="../images/accueil/pousses.jpg" />
                <div style="position: absolute; width: 480px; height: 120px; top: 30px; left: 30px; padding: 5px;
                    text-align: left; line-height: 60px; text-transform: uppercase; font-size: 50px;
                        color: #FFFFFF;">Maïs
                </div>
                <div style="position: absolute; width: 480px; height: 120px; top: 300px; left: 30px; padding: 5px;
                    text-align: left; line-height: 36px; font-size: 30px;
                        color: #FFFFFF;">
                        Build your slider with anything, includes image, content, text, html, photo, picture
                </div>
            </div>

            <div>
                <img u="image" src="../images/accueil/bles.jpg" />
                <div style="position: absolute; width: 480px; height: 120px; top: 30px; left: 30px; padding: 5px;
                    text-align: left; line-height: 60px; text-transform: uppercase; font-size: 50px;
                        color: #FFFFFF;">Blé
                </div>
                <div style="position: absolute; width: 480px; height: 120px; top: 300px; left: 30px; padding: 5px;
                    text-align: left; line-height: 36px; font-size: 30px;
                        color: #FFFFFF;">
                        Build your slider with anything, includes image, content, text, html, photo, picture
                </div>
            </div>

            <div>
                <img u="image" src="../images/accueil/jardin.jpg" />
                <div style="position: absolute; width: 480px; height: 120px; top: 30px; left: 30px; padding: 5px;
                    text-align: left; line-height: 60px; text-transform: uppercase; font-size: 50px;
                        color: #FFFFFF;">Potager
                </div>
                <div style="position: absolute; width: 480px; height: 120px; top: 300px; left: 30px; padding: 5px;
                    text-align: left; line-height: 36px; font-size: 30px;
                        color: #FFFFFF;">
                        Build your slider with anything, includes image, content, text, html, photo, picture
                </div>
            </div>

            <div>
                <img u="image" src="../images/accueil/noyers1.jpg" />
                <div style="position: absolute; width: 480px; height: 120px; top: 30px; left: 30px; padding: 5px;
                    text-align: left; line-height: 60px; text-transform: uppercase; font-size: 50px;
                        color: #FFFFFF;">Noyers
                </div>
                <div style="position: absolute; width: 480px; height: 120px; top: 300px; left: 30px; padding: 5px;
                    text-align: left; line-height: 36px; font-size: 30px;
                        color: #FFFFFF;">
                        Build your slider with anything, includes image, content, text, html, photo, picture
                </div>
            </div>

            <div>
                <img u="image" src="../images/accueil/noyers2.jpg" />
                <div style="position: absolute; width: 480px; height: 120px; top: 30px; left: 30px; padding: 5px;
                    text-align: left; line-height: 60px; text-transform: uppercase; font-size: 50px;
                        color: #FFFFFF;">Noyers
                </div>
                <div style="position: absolute; width: 480px; height: 120px; top: 300px; left: 30px; padding: 5px;
                    text-align: left; line-height: 36px; font-size: 30px;
                        color: #FFFFFF;">
                        Build your slider with anything, includes image, content, text, html, photo, picture
                </div>
            </div>


        </div>

        <!--#region Bullet Navigator Skin Begin -->
        <!-- Arrow Left -->
        <span u="arrowleft" class="jssora21l" style="top: 123px; left: 8px;">
        </span>
        <!-- Arrow Right -->
        <span u="arrowright" class="jssora21r" style="top: 123px; right: 8px;">
        </span>
        <!--#endregion Arrow Navigator Skin End -->

    </div>
    <!-- Jssor Slider End -->
</div>
        '''
    return ret

