template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
compteur = Import('compteur.py')
import json

def index(error=''):
    ret=template.afficherHautPage(error, titre='Voir le réseau')
    ret += corps_page()
    ret += template.afficherBasPage()
    return ret

def corps_page():
    html = """
    <div class = container>
        <div class="sixteen columns over" style="text-align: center;">
            <h1>Le réseau d'irrigation</h1>
        </div>
    	<aside class="six columns main-content">
	        <h2>Compteur séléctionné</h2>
	        <span>
	            <img src="../images/pompe.png" height=100px style="border:2px; border-color:#004A4D; border-style:groove; padding:5px;"></img>
	            <h3>Nom :</h3>
	        </span>
	    </aside>
        <article class="ten columns right-sidebar">
            <div id="map" style="height: 700px"></div>
            <script type="text/javascript" src="../js/map.js"></script>
	        <script type="text/javascript" src="../js/map_network.js"></script>
	    </article>
	</div>
    """
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
            dico_current["properties"] = {"id":current_com.id,"altitude": altitude}
            dico_current["geometry"]= {"type": "Point", "coordinates": [current_com.lon, current_com.lat]}
            list_json.append(dico_current)
    dico["features"] = list_json
    objects = json.dumps(dico)
    return objects





def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)
