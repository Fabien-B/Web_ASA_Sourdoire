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
    <div id="map" style="height: 700px"></div>
	<script type="text/javascript" src="../js/map_network.js"></script>
	<script type="text/javascript" src="../js/network_content.js"></script>
    """
    return html

def get_json_compteurs(id_ex=-1):
    list_compteurs = compteur.Compteur.get_compteurs_id(id_ex)
    dico = {}
    dico["type"]="FeatureCollection"
    list_json = []
    for id_com in list_compteurs:
        current_com = compteur.Compteur(id_com)
        altitude = current_com.altitude if current_com.altitude != None else 'n/a'
        if current_com.lon != None and current_com.lat != None:
            dico_current = {}
            dico_current["type"] = "Feature"
            dico_current["properties"] = {"altitude": altitude}
            dico_current["geometry"]= {"type": "Point", "coordinates": [current_com.lon, current_com.lat]}
            list_json.append(dico_current)
    dico["features"] = list_json
    objects = json.dumps(dico)

    return objects





def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)
