template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')

def index(error=''):
    ret=template.afficherHautPage(error, titre='Ma Conso')
    if "login" in Session():
        ret += corps_page_connecte()
    else:
        ret += corps_page_deconnecte()
    ret += template.afficherBasPage()
    return ret

def corps_page_connecte():
    html = """
    <p>Bonjour!</p>
    <table class="table_conso">
    <caption>Votre consommation</caption>
    <tr>
        <th>Compteur</th>
        <th>Parcelle</th>
        <th>Consommation</th>
    </tr>"""
    html += add_line('aze','bvcc','456')
    html += """
</table>
    """
    return html

def corps_page_deconnecte():
    html = """
    <p>Bonjour! Veuillez vous connecter.</p>
    """
    return html

def add_line(compteur='', parcelle='', conso=None):
    line = """
    <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
    </tr>""".format(compteur,parcelle,conso)
    return line

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)

# '''select Releve.Id_releve, Releve.Compteur, Releve.Exploitant, Releve.Index_début, Releve.Index_fin,Releve.Date FROM Releve WHERE Exploitant = 1 ORDER BY Compteur,Date;'''