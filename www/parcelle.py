import mysql.connector

class Parcelle(object):
    database = 'asa'
    user = 'root'
    password = 'root'
    host = '127.0.0.1'

    def __init__(self,id_parc,compteur=None,nom=None,lat=None,lon=None,altitude=None):
        if  id_parc>0:
            self.load(id_parc)
        else:
            connection = mysql.connector.connect(user=Parcelle.user, password=Parcelle.password,host=Parcelle.host,database=Parcelle.database)
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
            curseur.close()
            connection.close()
    
    def save(self):
        if self.compteur == None:
            raise ParcelleError("compteur missing for create parcelle")
        connection = mysql.connector.connect(user=Parcelle.user, password=Parcelle.password,host=Parcelle.host,database=Parcelle.database)
        curseur = connection.cursor()
        requete = "INSERT INTO Parcelle VALUES ({0},{1},{2},{3},{4},{5});".format(self.id, self.compteur, self.nom, self.lat, self.lon, self.altitude)
        curseur.execute(requete)
        connection.commit()
        curseur.close()
        connection.close()

    def load(self,id_parc):
        connection = mysql.connector.connect(user=Parcelle.user, password=Parcelle.password,host=Parcelle.host,database=Parcelle.database)
        curseur = connection.cursor()
        requete = 'select * from Parcelle where Id_parcelle={};'.format(id_parc)
        curseur.execute(requete)
        try:
            (_,compteur,nom,lat,lon,altitude)=curseur.fetchall()[0]
        except IndexError:
            raise ParcelleError("Parcelle with id {} doesn't exist".format(id_parc))
        curseur.close()
        connection.close()

        self.id = id_parc
        self.compteur = compteur
        self.nom = nom
        self.lat = lat
        self.lon = lon
        self.altitude = altitude

    def release_my(self):
        connection = mysql.connector.connect(user=Parcelle.user, password=Parcelle.password,host=Parcelle.host,database=Parcelle.database)
        curseur = connection.cursor()
        requete = 'UPDATE Propriete SET Id_exploitant=NULL WHERE Id_parcelle={0};'.format(self.id)
        curseur.execute(requete)
        connection.commit()
        curseur.close()
        connection.close()

    @staticmethod
    def get_exploitant_parcelle_id(id_ex):
        connection = mysql.connector.connect(user=Parcelle.user, password=Parcelle.password,host=Parcelle.host,database=Parcelle.database)
        curseur = connection.cursor()
        if id_ex == 0:
            requete = 'select Id_parcelle FROM Parcelle;'
        elif id_ex == -1: #parcelles libres
            requete = 'select Parcelle.Id_parcelle FROM Parcelle,Propriete WHERE Propriete.Id_parcelle = Parcelle.Id_parcelle AND Propriete.Id_exploitant IS NULL;'
        else:
            requete = 'select Parcelle.Id_parcelle FROM Parcelle,Propriete WHERE Propriete.Id_parcelle = Parcelle.Id_parcelle AND Id_exploitant = {};'.format(id_ex)
        curseur.execute(requete)
        id_parc = curseur.fetchall()
        curseur.close()
        connection.close()
        id_parc_list = []
        for (id,) in id_parc:
            id_parc_list.append(id)
        return id_parc_list



class ParcelleError(Exception):
    pass