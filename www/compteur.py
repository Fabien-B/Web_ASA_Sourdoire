import mysql.connector

class Compteur(object):
    database = 'IENAC14_asa'
    user = 'root'
    password = 'root'
    host = '127.0.0.1'

    def __init__(self,id_compt,nom=None,lat=None,lon=None,altitude=None, photo=None):
        if  id_compt>0:
            self.load(id_compt)
        else:
            connection = mysql.connector.connect(user=Compteur.user, password=Compteur.password,host=Compteur.host,database=Compteur.database)
            curseur = connection.cursor()
            requete = 'select max(Id_compteur) from Compteur;'
            curseur.execute(requete)
            (maxId,)=curseur.fetchall()[0]
            self.id = maxId + 1
            self.nom = nom
            self.lat = lat
            self.lon = lon
            self.altitude = altitude
            self.photo = photo
            curseur.close()
            connection.close()

    def save(self):
        connection = mysql.connector.connect(user=Compteur.user, password=Compteur.password,host=Compteur.host,database=Compteur.database)
        curseur = connection.cursor()
        requete = "INSERT INTO Compteur VALUES ({0},'{1}',{2},{3},{4}, {5});".format(self.id, self.nom, self.lat, self.lon, self.altitude, self.photo)
        curseur.execute(requete)
        connection.commit()
        curseur.close()
        connection.close()

    def update(self):
        connection = mysql.connector.connect(user=Compteur.user, password=Compteur.password,host=Compteur.host,database=Compteur.database)
        curseur = connection.cursor()
        requete = "UPDATE Compteur SET Nom='{0}', GPS_LAT={1}, GPS_LON={2}, Altitude={3}, Photo={5} WHERE Id_compteur={4};".format(self.nom, self.lat, self.lon, self.altitude, self.id, self.photo)
        curseur.execute(requete)
        connection.commit()
        curseur.close()
        connection.close()

    def load(self,id_compt):
        connection = mysql.connector.connect(user=Compteur.user, password=Compteur.password,host=Compteur.host,database=Compteur.database)
        curseur = connection.cursor()
        requete = 'select * from Compteur where Id_compteur={};'.format(id_compt)
        curseur.execute(requete)
        try:
            (_,nom,lat,lon,altitude, photo)=curseur.fetchall()[0]
        except IndexError:
            raise CompteurError("Compteur with id {} doesn't exist".format(id_compt))

        self.id = id_compt
        self.nom = nom
        self.lat = lat
        self.lon = lon
        self.altitude = altitude
        self.photo = photo
        curseur.close()
        connection.close()

    @staticmethod
    def get_compteurs_id(id_ex):
        connection = mysql.connector.connect(user=Compteur.user, password=Compteur.password,host=Compteur.host,database=Compteur.database)
        curseur = connection.cursor()
        if id_ex == 0:
            requete = 'select Id_compteur FROM Compteur;'
        else:
            requete = 'select Compteur FROM Parcelle,Propriete WHERE Propriete.Id_parcelle = Parcelle.Id_parcelle AND Id_exploitant = {};'.format(id_ex)
        curseur.execute(requete)
        id_compt_tuple = curseur.fetchall()
        id_compt_list = []
        for (id_compt,) in id_compt_tuple:
            id_compt_list.append(id_compt)
        curseur.close()
        connection.close()
        return id_compt_list

    @staticmethod
    def get_last_index(id_compteur):
        connection = mysql.connector.connect(user=Compteur.user, password=Compteur.password,host=Compteur.host,database=Compteur.database)
        curseur = connection.cursor()
        requete ="select Index_fin,Id_releve from Releve where Id_releve = (select max(Id_releve) from Releve where Compteur = {});".format(id_compteur)
        curseur.execute(requete)
        try:
            result = curseur.fetchall()[0]
        except IndexError:
            result = (0,-1)
        curseur.close()
        connection.close()
        return result   #(Index_fin,Id_releve)

    @staticmethod
    def modif_img_compteur(id_compteur, photo):
        connection = mysql.connector.connect(user=Compteur.user, password=Compteur.password,host=Compteur.host,database=Compteur.database)
        curseur = connection.cursor()
        requete ="UPDATE Compteur SET Photo='{0}' WHERE Id_compteur={1};".format(photo,id_compteur)
        curseur.execute(requete)
        connection.commit()


class CompteurError(Exception):
    pass