import mysql.connector

class Evenement(object):
    database = 'asa'
    user = 'root'
    password = 'root'
    host = '127.0.0.1'

    def __init__(self,id_event,desciptif=None,createur=None,compteur=None,photo=None):
        if id_event > 0:
            self.load(id_event)
        else:
            maxId = self.get_last_id()
            self.id = maxId + 1
            self.descriptif = desciptif
            self.createur = createur
            self.compteur = compteur
            self.photo = photo


    def save(self):     #TODO vérifier les NULL et None / BDD
        if self.descriptif == None or self.createur == None or self.compteur == None:
            raise EvenementError("Miss desciptif, createur or compteur for saving evenement")

        if self.photo != None:
            photo = "'{}'".format(self.photo)
        else:
            photo = 'NULL'

        descriptif = "{}".format(self.descriptif)
        createur = "'{}'".format(self.createur)
        compteur = "'{}'".format(self.compteur)

        connection = mysql.connector.connect(user=Evenement.user, password=Evenement.password,host=Evenement.host,database=Evenement.database)
        curseur = connection.cursor()
        requete = "INSERT INTO Evenement VALUES ({0},'{1}',{2},{3},{4});".format(self.id, descriptif, createur, compteur, photo)
        curseur.execute(requete)
        connection.commit()

    def load(self, id_event):
        connection = mysql.connector.connect(user=Evenement.user, password=Evenement.password,host=Evenement.host,database=Evenement.database)
        curseur = connection.cursor()
        requete = 'select * from Evenement where Id_event={};'.format(id_event)
        curseur.execute(requete)
        try:
            (_, descriptif, createur, compteur, photo) = curseur.fetchall()[0]
        except IndexError:
            raise EvenementError("Evenement with id {} doesn't exist".format(id_event))

        self.id = id_event
        self.descriptif = descriptif
        self.createur = createur
        self.compteur = compteur
        self.photo = photo

    def update(self, descriptif, createur, compteur, photo):
        connection = mysql.connector.connect(user=Evenement.user, password=Evenement.password,host=Evenement.host,database=Evenement.database)
        curseur = connection.cursor()
        requete = "UPDATE Evenement SET Descriptif='{0}', Createur='{1}', Compteur='{2}', Photo='{3}' WHERE Id_event={4};".format(descriptif, createur, compteur, photo, self.id)
        curseur.execute(requete)
        connection.commit()

    @staticmethod
    def get_last_id():
        connection = mysql.connector.connect(user=Evenement.user, password=Evenement.password,host=Evenement.host,database=Evenement.database)
        curseur = connection.cursor()
        requete = 'select max(Id_Event) from Evenement;'
        curseur.execute(requete)
        (maxId,)=curseur.fetchall()[0]
        if maxId is None:
            maxId = 0
        return maxId

    @staticmethod
    def get_event_from_compteurid(compteurid):
        connection = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database=Evenement.database)
        curseur = connection.cursor()
        requete = 'select Id_Event from Evenement where Compteur = {0};'.format(compteurid)
        curseur.execute(requete)
        eventid = curseur.fetchall()
        curseur.close()
        connection.close()
        return eventid


class EvenementError(Exception):
    pass