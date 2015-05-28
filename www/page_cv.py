template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')


def index(error=''):
    ret=template.afficherHautPage(error, titre='Page cv')
    if "login" in Session():
            ret += corps_page_connecte()
    else:
        ret += corps_page_deconnecte()
    ret += template.afficherBasPage()
    return ret

def corps_page_deconnecte():
    html = """
    <p>Bonjour! Veuillez vous connecter.</p>
    """
    return html

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)

def corps_page_connecte():
    html = '''<style>
    #cvs img{max-height:250px;border:solid;border-width:6px;border-color:#006407; border-radius:3px;}
    </style>
        <div id="cvs" class="container">
            <div style="text-align:center;" class="sixteen columns main-content">
                <div class="sixteen columns">
                    <h2>Cv's</h2>
                </div>

                <div class="four columns alpha">
                <a href="../cv/cv_polo.py/index">
                <img src="../cv/polo.png" title="DZIECIOL Nicolas" width="75%">
                </a>
                <p> CV DZIECIOL Nicolas </p>
                </div>

                <div class="four columns alpha">
                <a href="../cv/cv_fabien.py/index">
                <img src="../cv/fabien.png" title="BONNEVAL Fabien" width="75%">
                </a>
                <p> CV BONNEVAL Fabien </p>
                </div>

                <div class="four columns alpha">
                <a href="../cv/cv_guillaume.py/index">
                <img src="../cv/Pastre.jpg" title="PASTRE Guillaume" width="75%">
                </a>
                <p> CV PASTRE Guillaume </p>
                </div>

                <div class="four columns omega">
                <a href="../cv/cv_guilhem.py/index">
                <img src="../cv/guilhem.png" title="BUISAN Guilhem" width="75%">
                </a>
                <p>CV BUISAN Guilhem</p>
                </div>
            </div>
        </div>
    </div>
    '''

    return html
