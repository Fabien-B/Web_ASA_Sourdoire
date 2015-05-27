import mysql.connector

class Evenement(object):
    database = 'asa'
    user = 'root'
    password = 'root'
    host = '127.0.0.1'

    def __init__(self,id_event,desciptif=None,createur=None,compteur=None,photo1=None,photo2=None,):
        if id_event > 0:
            self.load(id_event)
        else:
            maxId = self.get_last_id()
            self.id = maxId + 1
            self.descriptif = desciptif
            self.createur = createur
            self.compteur = compteur
            self.photo1 = photo1
            self.photo2 = photo2


    def save(self):     #TODO vérifier les NULL et None / BDD
        if self.descriptif == None or self.createur == None or self.compteur == None:
            raise EvenementError("Miss desciptif, createur or compteur for saving evenement")

        if self.photo1 != None:
            photo1 = "'{}'".format(self.photo1)
        else:
            photo1 = 'NULL'

        if self.photo2 != None:
            photo2 = "'{}'".format(self.photo2)
        else:
            photo2 = 'NULL'

        descriptif = "{}".format(self.descriptif)
        createur = "'{}'".format(self.createur)
        compteur = "'{}'".format(self.compteur)

        connection = mysql.connector.connect(user=Evenement.user, password=Evenement.password,host=Evenement.host,database=Evenement.database)
        curseur = connection.cursor()
        requete = "INSERT INTO Evenement VALUES ({0},'{1}',{2},{3},{4},{5});".format(self.id, descriptif, createur, compteur, photo1, photo2)
        curseur.execute(requete)
        connection.commit()

    def load(self, id_event):
        connection = mysql.connector.connect(user=Evenement.user, password=Evenement.password,host=Evenement.host,database=Evenement.database)
        curseur = connection.cursor()
        requete = 'select * from Evenement where Id_event={};'.format(id_event)
        curseur.execute(requete)
        try:
            (_, descriptif, createur, compteur, photo1, photo2) = curseur.fetchall()[0]
        except IndexError:
            raise EvenementError("Evenement with id {} doesn't exist".format(id_event))

        self.id = id_event
        self.descriptif = descriptif
        self.createur = createur
        self.compteur = compteur
        self.photo1 = photo1
        self.photo2 = photo2

    def update(self, descriptif, createur, compteur, photo1, photo2):
        connection = mysql.connector.connect(user=Evenement.user, password=Evenement.password,host=Evenement.host,database=Evenement.database)
        curseur = connection.cursor()
        requete = "UPDATE Evenement SET Descriptif='{0}', Createur='{1}', Compteur='{2}', Photo_1='{3}', Photo_2='{4}', WHERE Id_event={5};".format(descriptif, createur, compteur, photo1, photo2, self.id)
        curseur.execute(requete)
        connection.commit()

    @staticmethod
    def get_last_id():
        connection = mysql.connector.connect(user=Evenement.user, password=Evenement.password,host=Evenement.host,database=Evenement.database)
        curseur = connection.cursor()
        requete = 'select max(Id_Event) from Evenement;'
        curseur.execute(requete)
        (maxId,)=curseur.fetchall()[0]
        return maxId

class EvenementError(Exception):
    pass