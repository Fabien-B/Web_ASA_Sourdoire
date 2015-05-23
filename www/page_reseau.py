template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
compteur = Import('compteur.py')
exploitant = Import('Exploitant.py')
import json
import os

def index(error=''):
    ret=template.afficherHautPage(error, titre='Voir le réseau')
    ret += corps_page()
    ret += template.afficherBasPage()
    return ret

def corps_page():
    html = '''
    <div class = container>
        <div class="sixteen columns over" style="text-align: center;">
            <h1>Le réseau d'irrigation</h1>
        </div>
        <aside class="six columns main-content">
            <h2>Compteur séléctionné</h2>
    '''
    html += detail(0)
    html += '''</aside>
        <article class="ten columns right-sidebar">
            <div id="map" style="height: 700px"></div>
            <script type="text/javascript" src="../js/map.js"></script>
            <script type="text/javascript" src="../js/map_network.js"></script>
        </article>
    </div>
    '''
    return html

def detail(id_compteur=1):
    id_compteur = int(id_compteur)
    selected_comp = compteur.Compteur(id_compteur)

    path = '../images/compteur_{0}.png'.format(id_compteur)
    if not os.path.exists(path):
        path = '../images/pompe.png'

    nom = selected_comp.nom if selected_comp.nom else 'Donnée manquante'
    latitude = selected_comp.lat if selected_comp.lat else 'Donnée manquante'
    longitude = selected_comp.lon if selected_comp.lon else'Donnée manquante'
    altitude = str(selected_comp.altitude) + ' m' if selected_comp.altitude else'Donnée manquante'

    Ids_ex = exploitant.Exploitant.get_compteur_exploitants_id(id_compteur)
    exploits = '</br>'
    for id_ex in Ids_ex:
        name = exploitant.Exploitant(id_ex).nom
        exploits += '    - ' + name + '</br>'
    conjug = '' if len(Ids_ex)==1 else 's'

    html = '''<span id="detail_compteur">
                <img src="{0}" height=100px style="border:2px; border-color:#004A4D; border-style:groove; padding:5px;"></img>
                 <h3>Nom : {1}</h3>
                 <h3>position : {2}, {3}</h3>
                 <h3>Altitude : {4}</h3>
                 <h3>Exploitant{5} : {6}</h3>
            </span>'''.format(path,nom,latitude,longitude,altitude,conjug,exploits)
    return html

def get_json_compteurs(ex=not None):
    if ex and "login" in Session():     #une recherche ciblée necessite d'être connecté pour aboutir
        id_ex = Session()["Id_exploitant"]
    else:
        id_ex = 0
    list_compteurs = compteur.Compteur.get_compteurs_id(id_ex)
    return compteurs_to_json(list_compteurs)

def compteurs_to_json(list_compteurs):
    dico = {}
    dico["type"]="FeatureCollection"
    list_json = []
    for id_com in list_compteurs:
        current_com = compteur.Compteur(id_com)
        altitude = current_com.altitude if current_com.altitude != None else 'n/a'
        if current_com.lon != None and current_com.lat != None:
            dico_current = {}
            dico_current["type"] = "Feature"
            dico_current["properties"] = {"id":current_com.id,"nom":current_com.nom,"altitude": altitude}
            dico_current["geometry"]= {"type": "Point", "coordinates": [current_com.lon, current_com.lat]}
            list_json.append(dico_current)
    dico["features"] = list_json
    objects = json.dumps(dico)
    return objects





def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)
