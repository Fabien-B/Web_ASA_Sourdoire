import mysql.connector

class Parcelle(object):
    database = 'asa'

    def __init__(self,id_parc,compteur=None,nom=None,lat=None,lon=None,altitude=None):
        if  id_parc>0:
            self.load(id_parc)
        else:
            connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='asa')
            curseur = connection.cursor()
            requete = 'select max(Id_parcelle) from Parcelle;'
            curseur.execute(requete)
            (maxId,)=curseur.fetchall()[0]
            self.id = maxId + 1
            self.compteur = compteur
            self.nom = nom
            self.lat = lat
            self.lon = lon
            self.altitude = altitude
    
    def save(self):
        if self.compteur == None:
            raise ParcelleError("compteur missing for create parcelle")
        connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='asa')
        curseur = connection.cursor()
        requete = "INSERT INTO Parcelle VALUES ({0},{1},{2},{3},{4},{5});".format(self.id, self.compteur, self.nom, self.lat, self.lon, self.altitude)
        curseur.execute(requete)
        connection.commit()

    def load(self,id_parc):
        connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='asa')
        curseur = connection.cursor()
        requete = 'select * from Parcelle where Id_parcelle={};'.format(id_parc)
        curseur.execute(requete)
        try:
            (_,compteur,nom,lat,lon,altitude)=curseur.fetchall()[0]
        except IndexError:
            raise ParcelleError("Parcelle with id {} doesn't exist".format(id_parc))

        self.id = id_parc
        self.compteur = compteur
        self.nom = nom
        self.lat = lat
        self.lon = lon
        self.altitude = altitude

    @staticmethod
    def get_exploitant_parcelle_id(id_ex):
        connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='asa')
        curseur = connection.cursor()
        if id_ex == 0:
            requete = 'select Id_parcelle FROM Parcelle;'
        else:
            requete = 'select Parcelle.Id_parcelle FROM Parcelle,Propriete WHERE Propriete.Id_parcelle = Parcelle.Id_parcelle AND Id_exploitant = {};'.format(id_ex)
        curseur.execute(requete)
        id_parc = curseur.fetchall()
        id_parc_list = []
        for (id,) in id_parc:
            id_parc_list.append(id)
        return id_parc_list


class ParcelleError(Exception):
    pass