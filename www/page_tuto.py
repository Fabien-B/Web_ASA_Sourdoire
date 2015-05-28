template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')



def index(error=''):
    ret=template.afficherHautPage(error, titre='Page cv')
    ret += corps_page()
    ret += template.afficherBasPage()
    return ret


def corps_page():
    html = """
        <div class="container">
            <div style="text-align:center;" class="sixteen columns main-content">
                <div class="sixteen columns">
                    <h2>Connexion</h2>
                    <br />
                    <iframe src="https://player.vimeo.com/video/128964301" width="500" height="400" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="https://vimeo.com/128964301">Connexion</a> from <a href="https://vimeo.com/user40537367">ASA Sourdoire</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
                    <br />
                    <br />

                </div>
                <div class="sixteen columns">
                    <h2>Suivre sa consommation</h2>
                    <br />
                    <iframe src="https://player.vimeo.com/video/128964892" width="500" height="400" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="https://vimeo.com/128964892">Ma conso</a> from <a href="https://vimeo.com/user40537367">ASA Sourdoire</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
                    <br />
                    <br />
                </div>
                <div class="sixteen columns">
                    <h2>Entrer un relevé en ligne</h2>
                    <br />
                    <iframe src="https://player.vimeo.com/video/128964896" width="500" height="400" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="https://vimeo.com/128964896">Releve</a> from <a href="https://vimeo.com/user40537367">ASA Sourdoire</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
                    <br />
                    <br />
                </div>
                <div class="sixteen columns">
                    <h2>Modifier ses informations personnelles</h2>
                    <br />
                    <iframe src="https://player.vimeo.com/video/128964893" width="500" height="400" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="https://vimeo.com/128964893">Profil</a> from <a href="https://vimeo.com/user40537367">ASA Sourdoire</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
                    <br />
                    <br />
                </div>
                <div class="sixteen columns">
                    <h2>Contacter l'administrateur</h2>
                    <br />
                    <iframe src="https://player.vimeo.com/video/128964889" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="https://vimeo.com/128964889">contact</a> from <a href="https://vimeo.com/user40537367">ASA Sourdoire</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
                    <br />
                    <br />
                </div>
                <div class="sixteen columns">
                    <h2>Voir le réseau</h2>
                    <br />
                    <iframe src="https://player.vimeo.com/video/128964983" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="https://vimeo.com/128964983">Voir Reseau</a> from <a href="https://vimeo.com/user40537367">ASA Sourdroire</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
                    <br />
                    <br />
                </div>
                <div class="sixteen columns">
                    <h2>Créer un événement</h2>
                    <br />
                    <iframe src="https://player.vimeo.com/video/128964890" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="https://vimeo.com/128964890">Evenement</a> from <a href="https://vimeo.com/user40537367">ASA Sourdoire</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
                    <br />
                </div>
            </div>
        </div>
        """

    return html

