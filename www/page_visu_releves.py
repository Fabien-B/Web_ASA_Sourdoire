exploitant = Import('Exploitant.py')
compteur = Import('compteur.py')
releve = Import('releve.py')
template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
parcelle = Import('parcelle.py')
litige = Import('litige.py')

def index(error=''):
    ret=template.afficherHautPage(error, titre='Voir les relevés')
    if "login" in Session() and not Session()["Id_exploitant"]:
            ret += corps_page_connecte()
    else:
        ret += corps_page_deconnecte()
    ret += template.afficherBasPage()
    return ret


def corps_page_connecte():
    script = '''<script>
  $(function() {
    $( "#datepicker" ).datepicker();
  });
  </script>
  <script>
  $(function() {
    $( "#timepicker" ).timepicker();
  });
  </script>
'''

    style='''<style> input[type="text"] { float: right; margin-right: 20px;} select{ float: right; margin-right: 20px;} p{margin-bottom:35px;}</style>'''

    html = """
    {0}
    <div class="container">
    <h1 class="container sixteen columns over" style="text-align: center;margin-bottom:15px;">Informations du relevé</h1>
        <aside class="six columns left-sidebar">
        <div class="sidebar-widget">
        <h2 style='margin-bottom:30px'>Choisir un relevé :</h2>""".format(style)


    html +=inspector()

    html +=''' <p style='float:right; margin-right:20px;'><input type="submit" name="submit" value="Valider" onclick="get_releves_params()" /></p>
            </aside>
        <!-- End Left Sidebar -->


        <article class="ten columns main-content">
        <html>
    <head>
    <script type="text/javascript" src="../js/jquery-2.1.3.js"></script>
    </head>

    <div>

<form>
        <div class="sidebar-widget">'''

    html += get_compteur_combo_box(Session()["Id_exploitant"])

    html += get_releve_select()


    html += '''</div>
        <link rel="stylesheet" href="../stylesheets/jquery-ui.min.css">
        <script src="../js/jquery-ui.min.js"></script>
{}
</html>

        </article>
        <!-- End main Content -->
    </div>
    '''.format(script)
    return html


def recup_options(id_ex):
    options = ''
    compteurs_parc_id = exploitant.Exploitant.get_compteurs_parcelle_id(id_ex)
    for (id_compt, id_parc) in compteurs_parc_id:
        current_parc = parcelle.Parcelle(id_parc)
        current_compt = compteur.Compteur(id_compt)
        line = '<option value="{}"> '.format(id_compt) + str(id_compt) + ', ' + current_compt.nom + ': ' + current_parc.nom.capitalize() + ' </option>' + '\n'
        options += line
    return options

def get_options_releves(id_comteur = 0):
    id_comteur = int(id_comteur)
    options =''
    ids_releves = releve.Releve.get_releve_id_from_compteur(id_comteur)
    for id_rel in ids_releves:
        rel = releve.Releve(id_rel)
        expl = exploitant.Exploitant(rel.exploitant)
        options += '<option value="{0}">{0}: {1} - {2}</option>\n'.format(rel.id,expl.nom,rel.date)
    return options

def get_compteur_combo_box(id_ex):
    id_ex = int(id_ex)
    html = """<p>Compteur :
        <select id="combo_compteur_releves" name="id_compteur" onchange="update_releve_select(this,this.selectedIndex)">
        <option value="0"> Tout les compteurs </option>
        {0}
        </select></p>""".format(recup_options(id_ex))
    return html


def get_releve_select(id_compteur = 0):
    html ='''<p>Relevés :
            <select id="releves_select" size="10" name="id_releve" onchange="update_inspector_releve(this,this.selectedIndex)">
            {0}
            </select></p>'''.format(get_options_releves(id_compteur))
    return html


def inspector(id_rel = 10):
    id_rel = int(id_rel)
    rel = releve.Releve(id_rel)
    html = '<div id="releve_inspector">'
    html += '''
    <p>Index début :
    <input id="visu_rel_index_deb" name="index_debut" type="text" value="{0}" required></p>
    '''.format(rel.index_deb)
    html += '''
    <p>Index fin :
    <input id="visu_rel_index_fin" name="index_fin"type="text" value="{0}" required></p>
    </div>'''.format(rel.index_fin)
    return html

def update_releves(id_rel,index_deb,index_fin):
    (id_rel,index_deb,index_fin) = (int(id_rel),int(index_deb),int(index_fin))
    rel = releve.Releve(id_rel)
    releve_id_list =releve.Releve.get_releve_id_from_compteur(rel.compteur)
    try:
        id_rel_pred = releve_id_list[releve_id_list.index(rel.id)+1]
    except IndexError:
        id_rel_pred=0
    try:
        index_rel = releve_id_list.index(rel.id)-1
        id_rel_next = releve_id_list[index_rel] if index_rel>=0 else 0
    except IndexError:
        id_rel_next=0

    rel_next = releve.Releve(id_rel_next) if id_rel_next else None
    rel_pred = releve.Releve(id_rel_pred) if id_rel_pred else None

    rel.index_fin = index_fin
    rel.index_deb = index_deb
    rel.update()

    if rel_next:
        rel_next.index_deb = index_fin
        rel_next.update()
    if rel_pred:
        rel_pred.index_fin = index_deb
        rel_pred.update()

    return '''Relevés n° {}, {}, {} mis à jour:
    index début: {}
    index fin: {}'''.format(id_rel_pred, rel.id ,id_rel_next, rel.index_deb, rel.index_fin)
