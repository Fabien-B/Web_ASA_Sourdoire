template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
releve = Import('releve.py')
#parcelle = Import('parcelle.py')

def index(error=''):
    ret=template.afficherHautPage(error, titre='Ma Conso')
    if "login" in Session():
        ret += corps_page_connecte()
    else:
        ret += corps_page_deconnecte()
    ret += template.afficherBasPage()
    return ret

def corps_page_connecte():
    #dico_parc_rels = get_releves(Session()["Id_exploitant"])    #TODO: ajouter la date de début et celle de fin.
    html = """
    <p>Bonjour!</p>
    <table class="table_conso">
    <form action="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" METHOD="get">
        <label for="date_debut">date de début:</label>
        <input type="date" name="date_debut" id="date">
        <label for="date_fin" placeholder="2020-01-01">date de fin:</label>
        <input type="date" name="date_fin" id="date">
        <input type="submit" value="Ok" />
    </form>
    <caption>Votre consommation</caption>
    <tr>
        <th>Compteur</th>
        <th>Parcelle</th>
        <th>Consommation</th>
    </tr>"""
    #for champ in dico_parc_rels.keys():
    #    html += add_line(champ,dico_parc_rels[champ])

    html += '''</table>
    '''
    return html

def corps_page_deconnecte():
    html = """
    <p>Bonjour! Veuillez vous connecter.</p>
    """
    return html

def add_line(parc, rels):
    '''add_line(<Parcelle>, [<Releve1>,<Releve2>, ...]'''
    conso = 0
    for rel in rels:
        conso += rel.index_fin - rel.index_deb
    line = """
    <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
    </tr>""".format(parc.Nom,parc.Compteur,conso)
    return line

def get_releves(Id_exploitant, date_debut=None, date_fin=None):
    releves_list = releve.Releve.get_releves_id(Id_exploitant,date_debut,date_fin)
    dico = {}           #{<Parcelle>:[<Releve1>,<Releve2>], ... }
    parcelles = {}      #{id:<Parcelle> , ...}
    for (id_releve,id_parcelle) in releves_list:
        if id_parcelle in parcelles.keys():
            dico[parcelles[id_parcelle]].append(releve.Releve(id_releve))
        else:
            parcelles[id_parcelle] = parcelle.Parcelles(id_parcelle)
            dico[parcelles[id_parcelle]] = [releve.Releve(id_releve)]
    return dico

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)