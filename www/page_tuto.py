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
                    <iframe src="https://player.vimeo.com/video/128964301" width="500" height="400" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="https://vimeo.com/128964301">Connexion</a> from <a href="https://vimeo.com/user40537367">Guillermo Pasdestress</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
                </div>
                <div class="sixteen columns">
                    <h2>Suivre sa consommation</h2>
                    <br />

                </div>
                <div class="sixteen columns">
                    <h2>Entrer un relevé en ligne</h2>
                    <br />

                </div>
                <div class="sixteen columns">
                    <h2>Modifier ses informations personnelles</h2>
                    <br />

                </div>
            </div>
        </div>
        """

    return html

