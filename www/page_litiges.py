template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
releve = Import('releve.py')
parcelle = Import('parcelle.py')
compteur = Import('compteur.py')
exploitant = Import('Exploitant.py')
litige = Import('litige.py')

def index(error=''):
    ret=template.afficherHautPage(error, titre='Litiges')
    if "login" in Session() and not Session()["Id_exploitant"]:
        ret += corps_page_connecte()
    else:
        ret += corps_page_deconnecte()
    ret += template.afficherBasPage()
    return ret

def corps_page_connecte():
    html = '''
        <div class="container">
            <article class="ten columns main-content">
                <div>
                    <h2>Litiges</h2>'''

    html += get_litiges()
    html += '''</article>'''
    html += '''<div class="sidebar-widget">
                    <aside class="six columns right-sidebar"> '''
    html += inspector()
    html += '''<input type="submit" name="submit" value="Valider" onclick="get_litige_params()" /></aside></div></div>
    '''
    return html

def corps_page_deconnecte():
    html = """
    <div class="container">
                        <div style="text-align:center;" class="sixteen columns main-content">
                            <div class="sixteen columns">
                                Bonjour! Merci de vous connecter !
                            </div>
                        </div>
                </div>
    """
    return html

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)

def get_litiges():
    html ='''
            <select style="width:60%;min-width:250px;" id="litiges_select" size="10" name="id_litige" onchange="update_inspector_litige(this.value)">
            {0}
            </select>'''.format(get_litige_options())
    return html


def get_litige_options():
    litiges = litige.Litige.get_all_litiges()
    options = ''
    for lit in litiges:
        rel1 = releve.Releve(lit.id_rel1)
        rel2 = releve.Releve(lit.id_rel2)
        ex1 = exploitant.Exploitant(rel1.exploitant)
        ex2 = exploitant.Exploitant(rel2.exploitant)
        comp = compteur.Compteur(rel1.compteur)
        line = '<option value="{}" >{} : {} et {}</option>\n'.format(lit.id, comp.nom, ex1.nom, ex2.nom)
        options += line
    return options


def inspector(id_lit=0):
    id_lit = int(id_lit)
    if id_lit:
        lit = litige.Litige(id_lit)
        id_rel1 = lit.id_rel1
        id_rel2 = lit.id_rel2
        (id_rel1,id_rel2) = (int(id_rel1),int(id_rel2))
        rel1 = releve.Releve(id_rel1)
        rel2 = releve.Releve(id_rel2)


    index_deb1 = rel1.index_deb if id_lit else None
    index_deb2 = rel2.index_deb if id_lit else None
    index_fin1 = rel1.index_fin if id_lit else None
    index_fin2 = rel2.index_fin if id_lit else None

    html = '<div id="litige_inspector">'
    html += '''
    <h2>Corriger le litige:</h2>
    <p>
    Index début relevé 1: {0}</br></br>
    Index fin relévé 1 :
    <input id="litige_rel1" name="index_fin_rel1" type="text" value="{1}" required></p></br>
    '''.format(index_deb1,index_fin1)
    html += '''
    <p>Index début relevé 2 :
    <input id="litige_rel2" name="index_debut_rel2"type="text" value="{0}" required></p></br>
    Index fin relévé 2 : {1}</br></br>
    </div>'''.format(index_deb2,index_fin2)
    return html

def update_litige_releves(id_lit, index_fin1, index_deb2):
    id_lit = int(id_lit)
    lit = litige.Litige(id_lit)
    id_rel1 = lit.id_rel1
    id_rel2 = lit.id_rel2
    releve.update_releves(id_rel1,index_fin=index_fin1)
    releve.update_releves(id_rel2,index_deb=index_deb2)
    if index_fin1 == index_deb2:
        lit.delete()
    return 'Mise à jour effectuée'