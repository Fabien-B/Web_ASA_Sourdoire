template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
compteur = Import('compteur.py')

def index(error=''):
    ret=template.afficherHautPage(error, titre='Voir le réseau')
    ret += corps_page()
    ret += template.afficherBasPage()
    return ret

def corps_page():
    html = """
    <p>Voici le réseau</p>
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
        dico_current = {}
        dico_current["type"] = "Feature"
        dico_current["properties"] = {"altitude": current_com.altitude}
        dico_current["geometry"]= {"type": "Point", "coordinates": [current_com.lat, current_com.lon]}
        list_json.append(dico_current)
    dico["features"] = list_json
    return dico





def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)
