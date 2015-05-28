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
                        <p>Bienvenue sur le site de l'<strong>ASA Sourdoire</strong>, le site de gestion de l'irrigation par internet.<br>
                        Simple. Minimal. Easy-to-use.</p>
                    </div>
                    <hr>
                    <p style ="font-size: large; text-align: justify;">(Re)Découvrez l'ASA Sourdoire désormais connecté ! Vous pouvez désormais rentrer vos relevés de chez vous par internet,
                     votre consommation est alors mise à jour en direct, et les dialogues avec le gestionnaire sont désormais plus simples.</p>
                     <br />
                    <hr>
                    <section class="container">

        <div class="one-third column" style ="text-align: justify;">
            <h3><i class="icon-heart rounded"></i> Consommation</h3>
            <p>Vous pouvez consulter votre consommation quand vous voulez,suivre l'évolution de celle ci et garder un suivi personnalisé de vos bornes et parcelles.</p>
        </div>
        <div class="one-third column" style ="text-align: justify;">
            <h3><i class="icon-cog rounded"></i> Fini la galère des relevés </h3>
            <p>Grâce à ce nouveau système vous pouvez entrer vous même un relevé, plus besoin d'intermédiaire !</p>
        </div>
        <div class="one-third column" style ="text-align: justify;">
            <h3><i class="icon-resize-full rounded"></i> Signalez les problèmes</h3>
            <p>Maintenant vous pouvez signalez quand il y a un soucis sur une des bornes, un relevé, consulter l'état du réseau et bien plus encore...</p>
        </div>

        </section>

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
        <body style="padding:0px; margin:0px; font-family:Arial, Verdana;background-color:#fff;">

    <script type="text/javascript" src="../js/jssor.js"></script>
    <script type="text/javascript" src="../js/jssor.slider.js"></script>
    <script type="text/javascript" src="../js/jquery-2.1.3.js"></script>
    <script type="text/javascript" src="../js/picture_slider.js"></script>

    <!-- Jssor Slider Begin -->
    <!-- To move inline styles to css file/block, please specify a class name for each element. -->
    <div id="slider1_container" style="position: relative; margin: 0 auto;
        top: 0px; left: 0px; width: 1300px; height: 300px; overflow: hidden; max-height:300px; margin-top:-30px;">
        <!-- Loading Screen -->
        <div u="loading" style="position: absolute; top: 0px; left: 0px;">
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

        <style>
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
        <!-- bullet navigator container -->
        <div u="navigator" class="jssorb21" style="bottom: 26px; right: 6px;">
            <!-- bullet navigator item prototype -->
            <div u="prototype"></div>
        </div>
        <!--#endregion Bullet Navigator Skin End -->

        <!--#region Arrow Navigator Skin Begin -->

        <style>
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
        <!-- Arrow Left -->
        <span u="arrowleft" class="jssora21l" style="top: 123px; left: 8px;">
        </span>
        <!-- Arrow Right -->
        <span u="arrowright" class="jssora21r" style="top: 123px; right: 8px;">
        </span>
        <!--#endregion Arrow Navigator Skin End -->

    </div>
    <!-- Jssor Slider End -->
</body>
        '''
    return ret

