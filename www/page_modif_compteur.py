template = Import('template.py' ) # import du fichier template (entete, pieds de page...)
connexion = Import('gestion_session.py')
releve = Import('releve.py')
parcelle = Import('parcelle.py')
compteur = Import('compteur.py')
exploitant = Import('Exploitant.py')
litige = Import('litige.py')
page_reseau = Import('page_reseau.py')

def index(error='',compteur_id=12,submit=None):
    ret=template.afficherHautPage(error, titre='Modifier un compteur')
    if "login" in Session() and not Session()["Id_exploitant"]:
        ret += corps_page_connecte(compteur_id)
    else:
        ret += corps_page_deconnecte()
    ret += template.afficherBasPage()
    return ret

def corps_page_connecte(id_compt):
    html = '''
        <div class="container">
            <div class="sidebar-widget">
                <aside class="six columns left-sidebar">
                    <h2>Modifier un compteur</h2>
                    <form action="traiter_modif_compteur" method="POST">
                    <input type="hidden" name="id_compteur"  value="{}" />'''.format(id_compt)
    compt = compteur.Compteur(int(id_compt))
    html += '''Nom: <input name="nom_compteur" type="text" value="{0}"></br>'''.format(compt.nom)
    html += lat_lon(compt.lat, compt.lon)
    html += '''Altitude (m): <input name="alt_compteur" type="text" value="{0}"></br>'''.format(compt.altitude)
    html += '''<input type="submit" name="submit" value="Valider" />
                </form>
                <br />
                <h2>Modifier la photo du compteur</h2>
                <form method="post" action="Upload_img" method="POST", enctype="multipart/form-data">
    <label for="mon_fichier">Photo (tous formats | max. 5 Mo) :</label>
    <input type="hidden" name="id_compteur"  value="{}" />
            <input type="file" name="mon_fichier" id="mon_fichier" />

            <br /><br />

            <input type="submit" name="submit" value="Changer la photo" />
        </form>
        </aside>'''.format(id_compt)

    #MAP! a mettre à droite.
    html +='''<article class="ten columns main-content">
            <div id="map" style="height: 400px"></div>
            <script type="text/javascript" src="../js/map.js"></script>
            <script type="text/javascript" src="../js/map_modif_compteur.js"></script>
        </article>'''

    html += """</div>
    </div>"""
    return html

def corps_page_deconnecte():
    html = """
    <div class="container">
                        <div style="text-align:center;" class="sixteen columns main-content">
                            <div class="sixteen columns">
                                Bonjour! Merci de vous connecter en administrateur !
                            </div>
                        </div>
                </div>
    """
    return html

def lat_lon(lat,lon):
    html = '''<p id="input_lat_lon">
                Latitude: <input name="lat_compteur" type="text" value="{0}"></br>
                Longitude: <input name="lon_compteur" type="text" value="{1}"></br></p>'''.format(lat,lon)
    return html

def traiterFormulaireConnexion(choix, login='',password=''):
    return connexion.Connexion(index, choix, login, password)

def traiter_modif_compteur(id_compteur, nom_compteur, lat_compteur, lon_compteur, alt_compteur, submit):
    compt = compteur.Compteur(int(id_compteur))
    compt.nom = nom_compteur
    compt.lat = float(lat_compteur)
    compt.lon = float(lon_compteur)
    compt.altitude = int(alt_compteur)
    compt.update()
    return page_reseau.index()

def afficher_form_ajout_photo(id_compt):
    return '''
    <form method="post" action="Upload_img" method="POST", enctype="multipart/form-data">
    <label for="mon_fichier">Photo (tous formats | max. 5 Mo) :</label>
    <input type="hidden" name="id_compteur"  value="{}" />
            <input type="file" name="mon_fichier" id="mon_fichier" />

            <br /><br />

            <input type="submit" name="submit" value="Changer la photo" />
        </form>'''.format(id_compt)

def Upload_img(mon_fichier,id_compteur):
    if mon_fichier is not None:
        try:
            import PIL_perso
            from PIL
            if mon_fichier.filename != "" :
                file_ext = mon_fichier.filename.split('.').pop()
                f = mon_fichier.file # file-like object
                dest_name = "./asa/images/Compteurs/compteur_{}.{}".format(id_compteur, file_ext)
                im = PIL_perso.Image.open(f)
                im.save(dest_name)
                photo = "compteur_{}.{}".format(id_compteur, file_ext)

        except AttributeError:
            photo = "NULL"

        compteur.modif_img_compteur(id_compteur, photo)
        return index("Photo du compteur mis à jour")