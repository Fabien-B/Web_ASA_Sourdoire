import mysql.connector

class Compteur(object):
    database = 'asa'

    def __init__(self,id_compt,nom=None,lat=None,lon=None,altitude=None):
        if  id_compt>0:
            self.load(id_compt)
        else:
            connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='asa')
            curseur = connection.cursor()
            requete = 'select max(Id_compteur) from Compteur;'
            curseur.execute(requete)
            (maxId,)=curseur.fetchall()[0]
            self.id = maxId + 1
            self.nom = nom
            self.lat = lat
            self.lon = lon
            self.altitude = altitude

    def save(self):
        connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='asa')
        curseur = connection.cursor()
        requete = "INSERT INTO Compteur VALUES ({0},{1},{2},{3},{4});".format(self.id, self.nom, self.lat, self.lon, self.altitude)
        curseur.execute(requete)
        connection.commit()

    def load(self,id_compt):
        connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='asa')
        curseur = connection.cursor()
        requete = 'select * from Compteur where Id_compteur={};'.format(id_compt)
        curseur.execute(requete)
        try:
            (_,nom,lat,lon,altitude)=curseur.fetchall()[0]
        except IndexError:
            raise CompteurError("Compteur with id {} doesn't exist".format(id_compt))

        self.id = id_compt
        self.nom = nom
        self.lat = lat
        self.lon = lon
        self.altitude = altitude


class CompteurError(Exception):
    pass